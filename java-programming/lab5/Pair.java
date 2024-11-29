public class Pair<K, V> { /* Обобщенный класс Pair с двумя типами параметров K и V*/

    public K first; /* Первый элемент пары. Тип K - произвольный ссылочный тип.*/
    public V second; /* Второй элемент пары. Тип V - произвольный ссылочный тип.*/


    /* Конструктор для создания пары с заданными значениями*/
    public Pair(K first, V second) {
        this.first = first;
        this.second = second;
    }

    /* Статический метод make_pair для создания пары вне контекста объекта класса Pair*/
    public static <K, V> Pair<K, V> makePair(K first, V second) {
        return new Pair<>(first, second);
    }

    @Override /* Переопределяем метод toString() для вывода пар в нужном формате*/
    public String toString() {
        return "(" + first + ", " + second + ")";
    }

    public static void main(String[] args) {
        /* Примеры использования обобщенного класса Pair:*/

        /* Пара целого числа и строки*/
        Pair<Integer, String> intStringPair = new Pair<>(10, "Hello");
        System.out.println("Integer: " + intStringPair.first + ", Stringi): " + intStringPair.second);


        /* Пара строк*/
        Pair<String, String> stringStringPair = Pair.makePair("Java", "Programming"); /* Использование make_pair*/
        System.out.println("String1: " + stringStringPair.first + ", Stringi2): " + stringStringPair.second);

        /*Пара объектов пользовательского класса*/
        class Person{
            String name;
            int age;
            Person(String name, int age){
                this.name = name;
                this.age = age;
            }
            @Override
            public String toString(){
                return name + ", " + age;
            }
        }

        Pair<Person, Person> personPair = new Pair<>(new Person("Bob", 30), new Person("Alice", 25));
        System.out.println("Person1: " + personPair.first + ", Person5: " + personPair.second);

        /* Изменение значений пары*/
        intStringPair.first = 20;
        intStringPair.second = "World";
        System.out.println("Modified Integer: " + intStringPair.first + ", Modified String: " + intStringPair.second);


        System.out.println("Pair toString(): " + intStringPair); /* Тест переопределенного toString()*/

    }
}

