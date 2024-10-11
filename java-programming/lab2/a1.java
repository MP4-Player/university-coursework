public class a1 {
    public static void main(String[] args) {
        System.out.println("-------------------------------------------------------------");
        System.out.println("Тип данных | min   | max");
        System.out.println("----------------------------------------------------------");
        System.out.println("byte    | " + Byte.MIN_VALUE + "         | " + Byte.MAX_VALUE);
        System.out.println("short   | " + Short.MIN_VALUE + "   | " + Short.MAX_VALUE);
        System.out.println("int     | " + Integer.MIN_VALUE + "| " + Integer.MAX_VALUE);
        System.out.println("long    | " + Long.MIN_VALUE + "   | " + Long.MAX_VALUE);
        System.out.println("float   | " + Float.MIN_VALUE + "  | " + Float.MAX_VALUE);
        System.out.println("double  | " + Double.MIN_VALUE + " | " + Double.MAX_VALUE);
        System.out.println("char    | " + (int) Character.MIN_VALUE + " | " + (int) Character.MAX_VALUE);
        System.out.println("boolean | -                | -");
        System.out.println("-----------------------------------------------------------");
    }
}