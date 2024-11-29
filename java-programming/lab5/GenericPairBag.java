import java.util.ArrayList;
import java.util.List;

public class GenericPairBag<T1, T2> {

    private List<Pair<T1, T2>> bag; //ArrayList для хранения пар

    public GenericPairBag() {
        bag = new ArrayList<>(); // Создаем ArrayList
    }

    public void add(Pair<T1, T2> pair) {
        bag.add(pair);
    }

    public Pair<T1, T2> remove() {
        if (bag.isEmpty()) {
            return null; // случий пустого мешка
        }
        int index = (int) Math.round(Math.random() * (bag.size() - 1)); //Гделаем случайный индекс
        return bag.remove(index); // Удаляем элемент по случайному индексу
    }

    public Pair<T1, T2> get() {
        if (bag.isEmpty()) {
            return null;
        }
        int index = (int) Math.round(Math.random() * (bag.size() - 1));
        return bag.get(index); // Возвращаем элемент по случайному индексу
    }

    public int getSize() {
        return bag.size();
    }

    public void printBagContents() {
        System.out.println("Содержимое мешка:");
        for (Pair<T1, T2> pair : bag) { // Простой итератор для вывода
            System.out.println(pair);
        }
        System.out.println("--------------------");
    }

    public static void main(String[] args) {
        GenericPairBag<Integer, String> intStringBag = new GenericPairBag<>();
        intStringBag.add(Pair.makePair(1, "one"));
        intStringBag.add(Pair.makePair(2, "two"));
        intStringBag.add(Pair.makePair(3, "three"));

        System.out.println("Размер мешка: " + intStringBag.getSize());
        System.out.println("Удаленная пара: " + intStringBag.remove());
        intStringBag.printBagContents();


        GenericPairBag<String, Double> stringDoubleBag = new GenericPairBag<>();
        stringDoubleBag.add(Pair.makePair("pi", 3.14159));
        stringDoubleBag.add(Pair.makePair("e", 2.71828));

        System.out.println("\nРазмер мешка: " + stringDoubleBag.getSize());
        System.out.println("Полученная пара: " + stringDoubleBag.get());
        stringDoubleBag.printBagContents();
    }
}

