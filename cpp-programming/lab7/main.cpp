#include <iostream>
#include <locale>
#ifdef _WIN32
#include <windows.h>  
#endif
#include "LibraryRecord.h"
#include "LibraryManager.h"

using namespace std;


void setRussianEncoding() {
#ifdef _WIN32
    
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);
#else
    
    setlocale(LC_ALL, "ru_RU.UTF-8");
#endif
}

// Функция для заполнения тестовыми данными
void fillTestData(LibraryManager& manager) {
    cout << "Заполняем библиотеку тестовыми данными..." << endl;

    // Создаем тестовые записи с использованием конструкторов:

    // 1. Книга выдана через 2 дня
    LibraryRecord record1("Иванов", "10.09.90", "12.09.90", true);

    // 2. Книга выдана через 5 дней
    LibraryRecord record2("Петров", "15.09.90", "20.09.90", true);

    // 3. Книга не выдана (isIssued = false)
    LibraryRecord record3("Сидоров", "25.04.90", "", false);

    // 4. Еще одна запись для Иванова (будет самым частым читателем)
    LibraryRecord record4("Иванов", "05.09.90", "15.09.90", true);

    // 5. Книга выдана через 5 дней в другую дату
    LibraryRecord record5("Кузнецов", "25.04.90", "30.04.90", true);

    // 6. Еще одна запись для Петрова
    LibraryRecord record6("Петров", "10.09.90", "15.09.90", true);

    // 7. Книга выдана в тот же день (самый маленький срок поиска)
    LibraryRecord record7("Смирнов", "15.09.90", "15.09.90", true);

    // Добавляем записи в менеджер
    manager.addRecord(record1);
    manager.addRecord(record2);
    manager.addRecord(record3);
    manager.addRecord(record4);
    manager.addRecord(record5);
    manager.addRecord(record6);
    manager.addRecord(record7);

    cout << "Добавлено " << manager.getRecordCount() << " записей." << endl;
}

// Основная функция
int main() {
    // Устанавливаем русскую кодировку
    setRussianEncoding();

    // Выводим заголовок программы
    cout << "==========================================" << endl;
    cout << "Лабораторная работа №7 (Вариант 3)" << endl;
    cout << "Перегрузка операций в библиотечной системе" << endl;
    cout << "==========================================" << endl << endl;

    // Создаем менеджер библиотеки
    LibraryManager manager;

    // Заполняем тестовыми данными
    fillTestData(manager);
    cout << endl;

    

    cout << "=== ДЕМОНСТРАЦИЯ ПЕРЕГРУЖЕННЫХ ОПЕРАТОРОВ ===" << endl;

    // 1. Демонстрация оператора вывода для одной записи (operator<<)
    cout << "\n1. ВЫВОД ОДНОЙ ЗАПИСИ С ПОМОЩЬЮ operator<<:" << endl;
    cout << "Первая запись в коллекции:" << endl;
    cout << manager[0] << endl;  // Используем перегруженный operator<<

    // 2. Демонстрация оператора вывода для всей коллекции
    cout << "\n2. ВЫВОД ВСЕЙ КОЛЛЕКЦИИ С ПОМОЩЬЮ operator<<:" << endl;
    cout << manager << endl;  // Используем перегруженный operator<< для LibraryManager

    // 3. Демонстрация оператора индексации (operator[])
    cout << "\n3. ИСПОЛЬЗОВАНИЕ ОПЕРАТОРА ИНДЕКСАЦИИ (operator[]):" << endl;
    cout << "Доступ к записям по индексу:" << endl;
    cout << "Запись [0]: " << manager[0].getLastName() << endl;
    cout << "Запись [1]: " << manager[1].getLastName() << endl;

    // Изменение записи через оператор индексации
    cout << "\nИзменение записи через operator[]:" << endl;
    manager[0].setLastName("Новиков");
    cout << "После изменения: Запись [0]: " << manager[0].getLastName() << endl;

    // 4. Демонстрация оператора присваивания (operator=)
    cout << "\n4. ДЕМОНСТРАЦИЯ ОПЕРАТОРА ПРИСВАИВАНИЯ (operator=):" << endl;
    LibraryRecord original("Оригинал", "01.01.90", "10.01.90", true);
    LibraryRecord copy;

    cout << "До присваивания:" << endl;
    cout << "original: " << original.getLastName() << endl;
    cout << "copy: " << copy.getLastName() << endl;

    // Используем перегруженный operator=
    copy = original;

    cout << "\nПосле copy = original:" << endl;
    cout << "original: " << original.getLastName() << endl;
    cout << "copy: " << copy.getLastName() << endl;

    // Изменяем копию (оригинал не должен измениться)
    copy.setLastName("Копия");
    cout << "\nПосле изменения копии:" << endl;
    cout << "original: " << original.getLastName() << " (не изменился!)" << endl;
    cout << "copy: " << copy.getLastName() << endl;

    // 5. Демонстрация оператора сравнения (operator==)
    cout << "\n5. ДЕМОНСТРАЦИЯ ОПЕРАТОРА СРАВНЕНИЯ (operator==):" << endl;
    LibraryRecord rec1("Иванов", "10.09.90", "12.09.90", true);
    LibraryRecord rec2("Иванов", "10.09.90", "12.09.90", true);
    LibraryRecord rec3("Петров", "10.09.90", "12.09.90", true);

    cout << "rec1 и rec2 одинаковы: " << (rec1 == rec2 ? "ДА" : "НЕТ") << endl;
    cout << "rec1 и rec3 одинаковы: " << (rec1 == rec3 ? "ДА" : "НЕТ") << endl;

    // 6. Демонстрация оператора сравнения (operator<)
    cout << "\n6. ДЕМОНСТРАЦИЯ ОПЕРАТОРА СРАВНЕНИЯ (operator<):" << endl;
    cout << "rec1 < rec3: " << (rec1 < rec3 ? "ДА (Иванов < Петров)" : "НЕТ") << endl;
    cout << "rec3 < rec1: " << (rec3 < rec1 ? "ДА" : "НЕТ") << endl;

    // 7. Демонстрация арифметического оператора (operator+)
    cout << "\n7. ДЕМОНСТРАЦИЯ АРИФМЕТИЧЕСКОГО ОПЕРАТОРА (operator+):" << endl;
    LibraryRecord rec4("Тестов", "05.09.90", "10.09.90", true);
    cout << "Исходная дата заказа: " << rec4.getOrderDate() << endl;

    // Добавляем 3 дня к дате заказа
    LibraryRecord rec5 = rec4 + 3;
    cout << "После rec4 + 3: " << rec5.getOrderDate() << " (05 + 3 = 08)" << endl;

    // Добавляем 10 дней (переход через десятки)
    LibraryRecord rec6 = rec4 + 10;
    cout << "После rec4 + 10: " << rec6.getOrderDate() << " (05 + 10 = 15)" << endl;

   

    cout << "\n\n=== ВЫПОЛНЕНИЕ ЗАДАНИЯ ВАРИАНТА 3 ===" << endl;

    // 1. Самый маленький срок поиска книги
    int minTime = manager.findMinSearchTime();
    cout << "\n1. Самый маленький срок поиска книги: ";
    if (minTime != -1) {
        cout << minTime << " дней" << endl;
    }
    else {
        cout << "нет данных" << endl;
    }

    // 2. Количество неудовлетворенных заказов
    int unsatisfied = manager.countUnsatisfiedOrders();
    cout << "2. Количество неудовлетворенных заказов: " << unsatisfied << endl;

    // 3. Самый частый читатель
    string frequentReader = manager.findMostFrequentReader();
    cout << "3. Самый частый читатель: " << frequentReader << endl;

    // 4. Читатели, получившие книги 15.09.90
    cout << "4. Читатели, получившие книги 15.09.90:" << endl;
    vector<string> readers = manager.getReadersByIssueDate("15.09.90");
    if (readers.empty()) {
        cout << "   Никто" << endl;
    }
    else {
        for (const auto& reader : readers) {
            cout << "   - " << reader << endl;
        }
    }

    // 5. Количество читателей, заказавших книги 25.04.90
    int count = manager.countReadersByOrderDate("25.04.90");
    cout << "5. Количество читателей, заказавших книги 25.04.90: " << count << endl;

    

    cout << "\n\n=== ДОПОЛНИТЕЛЬНАЯ ДЕМОНСТРАЦИЯ ===" << endl;

    // Демонстрация цепочек операций
    cout << "\nДемонстрация цепочек операций:" << endl;

    // Цепочка присваивания (благодаря возврату ссылки из operator=)
    LibraryRecord a, b, c;
    a = b = c = LibraryRecord("Цепочка", "01.01.90", "10.01.90", true);
    cout << "Цепочка присваивания: a = b = c = LibraryRecord(...)" << endl;
    cout << "a: " << a.getLastName() << endl;

    // Цепочка вывода (благодаря возврату ссылки на поток из operator<<)
    cout << "\nЦепочка вывода: cout << a << b << c" << endl;
    cout << a << "\n---\n" << b << "\n---\n" << c << endl;

    // Работа с константным объектом
    cout << "\nРабота с константным объектом:" << endl;
    const LibraryManager& constManager = manager;
    cout << "Доступ к записи через константную ссылку: " << constManager[0].getLastName() << endl;
    // constManager[0].setLastName("Новое"); // ОШИБКА: нельзя изменить через константную ссылку

    // =========== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===========

    cout << "\n==========================================" << endl;
    cout << "Программа завершена успешно!" << endl;
    cout << "==========================================" << endl;

    // Пауза для Windows (чтобы консоль не закрывалась сразу)
#ifdef _WIN32
    system("pause");
#endif

    return 0;
}