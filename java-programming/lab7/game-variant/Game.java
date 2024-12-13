import java.awt.*;
import java.util.Random;

public class Game {

    private static final int NUM_CELLS = 20;
    private static final int WINNING_BONUS = 50;

    private static int[] cells;
    private static Player player1;
    private static Player player2;
    private static Dice dice;

    public static void main(String[] args) {
        // Initialize game components
        cells = initializeGameBoard();
        player1 = new Player("Игрок 1");
        player2 = new Player("Игрок 2");
        dice = new Dice();

        // Game loop
        boolean gameOver = false;
        int currentPlayer = 1; // 1 or 2

        while (!gameOver) {
            int roll = dice.roll();
            System.out.println("n" + (currentPlayer == 1 ? player1.getName() : player2.getName()) + " бросает кость: " + roll);
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
        System.out.println("nИгра окончена!");
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

    }

    static class Player {
        private String name;
        private int score;
        private int position;

        public Player(String name) {
            this.name = name;
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
}
