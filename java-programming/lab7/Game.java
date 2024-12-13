import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;
import javax.swing.*;

public class Game {

    private static final int NUM_CELLS = 20;
    private static final int WINNING_BONUS = 50;

    private static int[] cells;
    private static Player player1;
    private static Player player2;
    private static Dice dice;
    private static GameBoardPanel gameBoardPanel;

    public static void main(String[] args) {
        // Initialize game components
        cells = initializeGameBoard();
        player1 = new Player();
        player2 = new Player();
        dice = new Dice();

        // Create the game window and board panel
        GameFrame frame = new GameFrame();
        gameBoardPanel = frame.getGameBoardPanel();

        // Main game loop
        boolean gameOver = false;
        int currentPlayer = 1; // 1 or 2

        while (!gameOver) {
            int roll = dice.roll();
            System.out.println("\n" + (currentPlayer == 1 ? player1.getName() : player2.getName()) + " бросает кость: " + roll);
            movePlayer(currentPlayer, roll);

            // Check for win condition
            if (player1.getPosition() >= NUM_CELLS -1 || player2.getPosition() >= NUM_CELLS -1) {
                gameOver = true;
            }

            currentPlayer = (currentPlayer == 1) ? 2 : 1;
        }

        // Determine the winner and display the result
        int player1FinalScore = player1.getScore();
        int player2FinalScore = player2.getScore();
        System.out.println("\nИгра окончена!");
        System.out.println(player1.getName() + ": " + player1FinalScore + " очков");
        System.out.println(player2.getName() + ": " + player2FinalScore + " очков");
        if (player1FinalScore > player2FinalScore) {
            System.out.println(player1.getName() + " побеждает!");
        } else if (player2FinalScore > player1FinalScore) {
            System.out.println(player2.getName() + " побеждает!");
        } else {
            System.out.println("Ничья!");
        }
    }

    // Initialize the game board with random cell values (points or actions)
    private static int[] initializeGameBoard() {
        int[] board = new int[NUM_CELLS];
        Random random = new Random();
        for (int i = 0; i < NUM_CELLS; i++) {
            int type = random.nextInt(3); // 0: points, 1: re-roll, 2: lose points
            if (type == 0) {
                board[i] = random.nextInt(15) - 5; // Points between -5 and 10
            } else if (type == 1) {
                board[i] = -999; // Re-roll
            } else {
                board[i] = -998; // Lose all points
            }
        }
        //Last cell is a win
        board[NUM_CELLS - 1] = -997; // Win
        return board;
    }


    //Move player and handle actions
    private static void movePlayer(int playerNum, int spaces) {
        Player currentPlayer = (playerNum == 1) ? player1 : player2;
        currentPlayer.move(spaces, cells);

        // Update the game board panel to reflect the player's new position.
        if (playerNum == 1) {
            gameBoardPanel.setPlayer1Pos(currentPlayer.getPosition());
        } else {
            gameBoardPanel.setPlayer2Pos(currentPlayer.getPosition());
        }
        gameBoardPanel.repaint();
    }

    static class Player {
        private String name = "Игрок";
        private int score;
        private int position;

        public Player() {
            this.score = 0;
            this.position = 0;
        }

        public String getName() {
            return name;
        }

        public int getScore() {
            return score;
        }

        public int getPosition() {
            return position;
        }

        public void move(int spaces, int[] board) {
            position += spaces;
            if (position >= board.length) {
                position = board.length - 1;
            }
            int cellValue = board[position];
            if (cellValue >= 0) {
                score += cellValue;
            } else if (cellValue == -999) {
                move(new Dice().roll(), board);
            } else if (cellValue == -998) {
                score = 0;
            } else if (cellValue == -997) {
                score += WINNING_BONUS;
            }
        }
    }

    static class Dice {
        private Random random = new Random();

        public int roll() {
            return random.nextInt(6) + 1;
        }
    }

    static class GameBoardPanel extends JPanel {
        private final int numCells;
        private final int cellSize = 50;
        private int[] cells;
        private int player1Pos;
        private int player2Pos;

        public GameBoardPanel(int numCells, int[] cells){
            this.numCells = numCells;
            this.cells = cells;
            this.player1Pos = 0;
            this.player2Pos = 0;
            setPreferredSize(new Dimension(numCells * cellSize, cellSize*2)); // Double height for two players.
            addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    //Determine which cell was clicked. Implement Game Logic here.
                }
            });
        }


        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g;
            g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            drawBoard(g2d);
        }

        private void drawBoard(Graphics2D g2d) {
            for (int i = 0; i < numCells; i++) {
                int x = i * cellSize;
                // Draw cell
                g2d.drawRect(x,0, cellSize,cellSize);
                // Draw player1 marker.
                if(i == player1Pos){
                    g2d.setColor(Color.BLUE);
                    g2d.fillOval(x + cellSize/4, cellSize/4, cellSize/2, cellSize/2);
                }
                // Draw player2 marker.
                if(i == player2Pos){
                    g2d.setColor(Color.RED);
                    g2d.fillOval(x + cellSize/4, cellSize + cellSize/4, cellSize/2, cellSize/2);
                }
            }
        }

        public void setPlayer1Pos(int pos) {
            player1Pos = pos;
        }

        public void setPlayer2Pos(int pos) {
            player2Pos = pos;
        }
    }

    static class GameFrame extends JFrame {
        private GameBoardPanel gameBoardPanel;

        public GameFrame() {
            setTitle("Игра в кости");
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            setLayout(new BorderLayout());

            gameBoardPanel = new GameBoardPanel(NUM_CELLS, cells);
            add(gameBoardPanel, BorderLayout.CENTER);

            pack();
            setVisible(true);
        }

        public GameBoardPanel getGameBoardPanel() {
            return gameBoardPanel;
        }
    }
}
