
public class c2 {

    private double real; /* Действительная часть комплексного числа*/
    private double imag; /* Мнимая часть комплексного числа*/

    /* Конструктор для создания числа*/
    public c2(double real, double imag) {
        this.real = real;
        this.imag = imag;
    }

    /* Конструктор для создания комплексного числа из действительного числа*/
    public c2(double real) {
        this(real, 0); /* Вызов основного конструктора с нулевой мнимой частью*/
    }

    /* Метод для получения действительной части комплексного числа*/
    public double getReal() {
        return real;
    }

    /* Метод для получения мнимой части комплексного числа*/
    public double getImag() {
        return imag;
    }

    /* Метод для сложения двух комплексных чисел*/
    public c2 add(c2 other) {
        return new c2(this.real + other.real, this.imag + other.imag);
    }

    /* Метод для сложения комплексного и действительного чисел*/
    public c2 add(double other) {
        return new c2(this.real + other, this.imag);
    }

    /* Метод для вычитания двух комплексных чисел*/
    public c2 subtract(c2 other) {
        return new c2(this.real - other.real, this.imag - other.imag);
    }

    /* Метод для вычитания действительного числа из комплексного*/
    public c2 subtract(double other) {
        return new c2(this.real - other, this.imag);
    }

    /* Метод для умножения двух комплексных чисел*/
    public c2 multiply(c2 other) {
        return new c2(this.real * other.real - this.imag * other.imag,
                this.real * other.imag + other.real * this.imag);
    }

    /* Метод для умножения комплексного числа на действительное*/
    public c2 multiply(double other) {
        return new c2(this.real * other, this.imag * other);
    }

    /* Метод для деления двух комплексных чисел*/
    public c2 divide(c2 other) {
        double denominator = other.real * other.real + other.imag * other.imag;
        return new c2((this.real * other.real + this.imag * other.imag) / denominator,
                (other.real * this.imag - this.real * other.imag) / denominator);
    }

    /* Метод для деления комплексного числа на действительное*/
    public c2 divide(double other) {
        return new c2(this.real / other, this.imag / other);
    }
    /* Метод для получения комплексно сопряженного числа*/
    public c2 conjugate() {
        return new c2(this.real, -this.imag);
    }

    /* Метод для проверки равенства двух комплексных чисел*/
    public boolean equals(c2 other) {
        return this.real == other.real && this.imag == other.imag;
    }

    /* Метод для вывода комплексного числа в алгебраической форме*/
    public String toStringAlgebraic() {
        return String.format("(%.2f + %.2fi)", real, imag); /*Форматирование для вывода*/
    }

    /* Метод для вывода комплексного числа в тригонометрической форме*/
    public String toStringTrigonometric() {
        double module = Math.sqrt(real * real + imag * imag);
        double argument = Math.atan2(imag, real); /* atan2 учитывает квадранты*/
        return String.format("(%.2f * (cos(%.2f) + i*sin(%.2f)))", module, argument, argument);
    }

    public static void main(String[] args) {
        c2 z1 = new c2(3, 4);
        c2 z2 = new c2(1, -2);
        c2 z3 = new c2(5);

        System.out.println("z1 (алгебраическая): " + z1.toStringAlgebraic());
        System.out.println("z1 (тригонометрическая): " + z1.toStringTrigonometric());
        System.out.println("z2 (алгебраическая): " + z2.toStringAlgebraic());
        System.out.println("z3 (алгебраическая): " + z3.toStringAlgebraic());


        System.out.println("z1 + z2 = " + z1.add(z2).toStringAlgebraic());
        System.out.println("z1 - z2 = " + z1.subtract(z2).toStringAlgebraic());
        System.out.println("z1 * z2 = " + z1.multiply(z2).toStringAlgebraic());
        System.out.println("z1 / z2 = " + z1.divide(z2).toStringAlgebraic());
        System.out.println("z1 + z3 = " + z1.add(z3).toStringAlgebraic());
        System.out.println("z1 * 2 = " + z1.multiply(2).toStringAlgebraic());
        System.out.println("Сопряженное z1 = " + z1.conjugate().toStringAlgebraic());
        System.out.println("z1 == z2: " + z1.equals(z2));

    }
}
