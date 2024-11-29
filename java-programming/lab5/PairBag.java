import java.util.Scanner;

public class PairBag { // Объявление класса PairBag

    private Bag bag; //Использование Bag для хранения пар.  Тип Object подойдет так как в нём можно хранить Pair разных типов.

    //Конструктор PairBag, который принимает размер массива в качестве параметра
    public PairBag(int capacity) {
        bag = new Bag(capacity); // Создание объекта класса Bag для хранения пар
    }

    // Метод для добавления пары в мешок
    public void add(Pair<?, ?> pair) { //Параметры типов <?> - дженерики для любого типа
        bag.add(pair);
    }


    // Метод для удаления и возврата случайной пары из мешка
    public Pair<?, ?> remove() {
        return (Pair<?, ?>) bag.remove(); // Приведение типа к Pair (возможно ClassCastException, если Bag пустой или содержит не Pair)
    }

    // Метод для получения случайной пары из мешка (без удаления)
    public Pair<?, ?> get() {
        return (Pair<?, ?>) bag.get(); //Приведение типа к Pair (возможно ClassCastException, если Bag пустой или содержит не Pair)
    }

    // Метод для получения текущего размера мешка
    public int getSize() {
        return bag.getSize();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите размер мешка:");
        int capacity = scanner.nextInt();
        scanner.nextLine(); // очищаем буфер

        PairBag pairBag = new PairBag(capacity); // Создаем PairBag

        while (true){
            System.out.println("\nВыберите действие:");
            System.out.println("1. Добавить пару");
            System.out.println("2. Удалить пару");
            System.out.println("3. Получить пару");
            System.out.println("4. Размер мешка");
            System.out.println("5. Выйти");

            int choice = scanner.nextInt();
            scanner.nextLine(); // очищаем буфер

            switch (choice) {
                case 1:
                    System.out.println("Введите первый элемент пары:");
                    String first = scanner.nextLine();
                    System.out.println("Введите второй элемент пары:");
                    String second = scanner.nextLine();
                    pairBag.add(Pair.makePair(first, second));
                    break;
                case 2:
                    Pair<?, ?> removedPair = pairBag.remove();
                    if(removedPair != null){
                        System.out.println("Удаленная пара: " + removedPair.first + ", " + removedPair.second);
                    }
                    break;
                case 3:
                    Pair<?, ?> gotPair = pairBag.get();
                    if(gotPair != null){
                        System.out.println("Полученная пара: " + gotPair.first + ", " + gotPair.second);
                    }
                    break;
                case 4:
                    System.out.println("Размер мешка: " + pairBag.getSize());
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Неверный выбор.");
            }
        }
    }
}
