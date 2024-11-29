
public class GPairBag<T1, T2> { // Обобщенный класс GPairBag с двумя параметрами типов T1 и T2

    private PairBag bag; //ne pizdim композицию с PairBag

    public GPairBag(int capacity) {
        bag = new PairBag(capacity); // Создаем необобщенный мешок для хранения пар
    }

    public void add(Pair<T1, T2> pair) { // Добавляем пары с конкретными типами T1 и T2
        bag.add(pair);
    }

    @SuppressWarnings("unchecked")
    public Pair<T1, T2> remove() {
        return (Pair<T1, T2>) bag.remove(); // Возвращаем пару, с типом T1, T2 

    }

    @SuppressWarnings("unchecked")
    public Pair<T1, T2> get() {
        return (Pair<T1, T2>) bag.get(); // Возвращаем пару, с типом T1, T2 
    }

    public int getSize() {
        return bag.getSize();
    }

    public void printBagContents() {
    System.out.println("Содержимое мешка:");
    for (int i = 0; i < bag.getSize(); i++) {
        Pair<T1, T2> pair = this.get(); //Используем метод get для получения элементов
        if(pair != null){
            System.out.println("Пара " + (i + 1) + ": (" + pair.first + ", " + pair.second + ")");
        }
    }
    System.out.println("--------------------");
}




    public static void main(String[] args) {
        //Пример использования GPairBag для пар Integer, String
        GPairBag<Integer, String> intStringBag = new GPairBag<>(5);
        intStringBag.add(Pair.makePair(1, "one"));
        intStringBag.add(Pair.makePair(2, "two"));

        System.out.println("Размер мешка: " + intStringBag.getSize());
        System.out.println("Удаленная пара: " + intStringBag.remove());


        //String, Double
        GPairBag<String, Double> stringDoubleBag = new GPairBag<>(3);
        stringDoubleBag.add(Pair.makePair("pi", 3.14159));
        stringDoubleBag.add(Pair.makePair("e", 2.71828));

        System.out.println("\nРазмер мешка: " + stringDoubleBag.getSize());
        System.out.println("Полученная пара: " + stringDoubleBag.get());

        intStringBag.printBagContents(); // Вывод intStringBag

        stringDoubleBag.printBagContents(); // Вывод  stringDoubleBag

    }
    
}



