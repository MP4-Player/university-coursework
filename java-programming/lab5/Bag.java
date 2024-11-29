import java.lang.Math;

public class Bag { /* Объявление класса Bag*/

    private Object[] items; /* Массив для хранения элементов мешка. Тип Object позволяет хранить элементы любых типов.*/
    private int size;       /* Текущее количество элементов в мешке*/

    /*Конструктор класса Bag, который принимает размер массива в качестве параметра*/
    public Bag(int capacity) {
        items = new Object[capacity]; /* Создание массива заданного размера*/
        size = 0;                    /* Изначально мешок пуст*/
    }

    /* Метод для добавления элемента в мешок.  Элемент добавляется в случайную позицию.*/
    public void add(Object item) {
        if (size < items.length) {  /* Проверка, есть ли место в мешке*/
            int index = (int) Math.round(Math.random() * (size)); /* Генерация случайного индекса для вставки*/
            /* Сдвигаем элементы массива вправо от случайного индекса, чтобы освободить место для нового элемента*/
            System.arraycopy(items, index, items, index + 1, size - index);
            items[index] = item;     /* Добавление элемента в случайную позицию*/
            size++;                  /* Увеличение размера мешка*/
        } else {
            System.out.println("Мешок полон!"); /* Сообщение об ошибке, если мешок полон*/
        }
    }

    /* Метод для удаления и возврата случайного элемента из мешка*/
    public Object remove() {
        if (size > 0) {           /* Проверка, есть ли элементы в мешке*/
            int index = (int) Math.round(Math.random() * (size - 1)); /* Генерация случайного индекса для удаления*/
            Object item = items[index]; /* Запоминаем удаляемый элемент*/
            /* Сдвигаем элементы массива влево от случайного индекса, чтобы удалить элемент*/
            System.arraycopy(items, index + 1, items, index, size - index - 1);
            items[--size] = null; /* Удаление элемента и уменьшение размера мешка*/
            return item;           /* Возвращение удаленного элемента*/
        } else {
            System.out.println("Мешок пуст!"); /* Сообщение об ошибке, если мешок пуст*/
            return null;
        }
    }

    /* Метод для возврата случайного элемента из мешка (без удаления)*/
    public Object get() {
        if (size > 0) {
            int index = (int) Math.round(Math.random() * (size - 1));
            return items[index];
        } else {
            System.out.println("Мешок пуст!");
            return null;
        }
    }

    /* Метод для получения текущего размера мешка*/
    public int getSize() {
        return size;
    }


    public static void main(String[] args) {
        Bag bag = new Bag(5); /* Создание мешка вместимостью 5 элементов*/

        bag.add(10);       /* Добавление целого числа*/
        bag.add("Hello");  /* Добавление строки*/
        bag.add(3.14);     /* Добавление числа с плавающей точкой*/
        bag.add(new Object()); /*Добавление объекта*/
        bag.add(true);     /* Добавление булевого значения*/


        System.out.println("Размер мешка: " + bag.getSize()); /* Вывод текущего размера мешка*/

        System.out.println("Удаленный элемент: " + bag.remove()); /* Удаление и вывод случайного элемента*/
        System.out.println("Случайный элемент: " + bag.get());   /* Вывод случайного элемента без удаления*/
        System.out.println("Размер мешка: " + bag.getSize()); /* Вывод текущего размера мешка*/
    }
}
