public class a34 {
    

    public static void main(String[] args) {
        if (args.length != 4) {
            System.err.println("Необходимо ввести два числа в качестве координат и 2 числа радиса r R ");
            return;
        } 

        try {
            int x = Integer.parseInt(args[0]);
            int y = Integer.parseInt(args[1]);
            int r = Integer.parseInt(args[2]);
            int R = Integer.parseInt(args[3]);

            int xy= x*x+y*y;
            int rr= r*r;
            int RR= R*R;

            System.out.println("Растояние до обьекта по прямой"+xy );
            System.out.println("Радиус активайии тревоги"+ rr );
            System.out.println("Радиус детекции обьекта"+RR );
            

            if (RR>rr) {
                if (xy > RR) {
                System.out.println("Обьект не обнаружен " );
            } else {
             if (xy >= rr) {
                System.out.println("Обьект обнаружен " );
            } else {
            System.out.println("ТРЕВОГА!");
            }
            }
                
                
            }else {
            System.out.println("Невозможные настроки детекции,R должен быть больше r");
            }


            
        } catch (NumberFormatException e) {
            System.err.println("Некорректный формат числа. Введите целое десятичное число.");
        
        }
    }
}