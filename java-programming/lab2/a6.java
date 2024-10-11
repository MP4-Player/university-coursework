import java.util.Scanner;//обьеденяет PrintStream и несколько других прикольных штук но рекомендовали его
public class a6 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int startCode = 16;
        int numRows = 16;
        int numColumns = 16;
        //char d= 97;
        //System.out.println(d);


        System.out.println("\nТаблица Кириллицы (стартовый код: 0x0400):");
        printUnicodeTable(0x0400, numRows, numColumns);

  
        System.out.println("\nТаблица знаков денежных единиц (стартовый код: 0x20a0):");
        printUnicodeTable(0x20a0, 2, numColumns);
    }

    public static void printUnicodeTable(int startCode, int numRows, int numColumns) {// cоздаем таблицу 
        char[][] table = new char[numRows][numColumns];//Char — это символьный тип данных. Переменная такого типа занимает 2 байта памяти, так как хранится в кодировке unicode.

    
        int currentCode = startCode;// заполняем таблицу символами Unicode
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numColumns; j++) {
                table[i][j] = (char) currentCode;
                currentCode++;
            }
        }

        //  хрень на консоль
        for (char[] row : table) {
            for (char c : row) {
                System.out.printf("%c ", c);//%c: для вывода одиночного символа
            }
            System.out.println();
            //System.out.println(currentCode);
            //System.out.println(table);
            //System.out.println(row);
        }
    }
}

