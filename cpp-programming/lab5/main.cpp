#include <iostream>
#include <locale>
#include <cstdlib>
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


void fillTestData(LibraryManager& manager) {
    cout << "Заполняем библиотеку тестовыми данными..." << endl;

    // Создаем тестовые записи о читателях
    LibraryRecord record1("Иванов", "10.09.90", "12.09.90", true);   // Выдана через 2 дня
    LibraryRecord record2("Петров", "15.09.90", "20.09.90", true);   // Выдана через 5 дней
    LibraryRecord record3("Сидоров", "25.04.90", "", false);         // Не выдана
    LibraryRecord record4("Иванов", "05.09.90", "15.09.90", true);   // Выдана через 10 дней
    LibraryRecord record5("Кузнецов", "25.04.90", "30.04.90", true); // Выдана через 5 дней
    LibraryRecord record6("Петров", "10.09.90", "15.09.90", true);   // Выдана через 5 дней
    LibraryRecord record7("Смирнов", "15.09.90", "15.09.90", true);  // Выдана в тот же день

    
    manager.addRecord(record1);
    manager.addRecord(record2);
    manager.addRecord(record3);
    manager.addRecord(record4);
    manager.addRecord(record5);
    manager.addRecord(record6);
    manager.addRecord(record7);

    cout << "Добавлено " << manager.getRecordCount() << " записей." << endl;
}


int main() {
    
    setRussianEncoding();

    
    cout << "==========================================" << endl;
    cout << "Лабораторная работа №3 (Вариант 3)" << endl;
    cout << "Библиотечная система: учет заказов книг" << endl;
    cout << "==========================================" << endl << endl;

    LibraryManager manager;

    
    fillTestData(manager);
    cout << endl;



    cout << "1. ВЫВОД ВСЕХ ЗАПИСЕЙ:" << endl;
    manager.displayAllRecords();


    cout << "\n2. РЕЗУЛЬТАТЫ АНАЛИЗА:" << endl;

 
    int minTime = manager.findMinSearchTime();
    if (minTime != -1) {
        cout << "   а) Самый маленький срок поиска книги: " << minTime << " дней" << endl;
    }
    else {
        cout << "   а) Нет данных о выданных книгах" << endl;
    }

 
    int unsatisfied = manager.countUnsatisfiedOrders();
    cout << "   б) Количество неудовлетворенных заказов: " << unsatisfied << endl;


    string frequentReader = manager.findMostFrequentReader();
    if (!frequentReader.empty()) {
        cout << "   в) Самый частый читатель: " << frequentReader << endl;
    }
    else {
        cout << "   в) Нет данных о читателях" << endl;
    }


    cout << "   г) Читатели, получившие книги 15.09.90:" << endl;
    vector<string> readers15_09_90 = manager.getReadersByIssueDate("15.09.90");
    if (readers15_09_90.empty()) {
        cout << "      Никто" << endl;
    }
    else {
        for (const auto& reader : readers15_09_90) {
            cout << "      - " << reader << endl;
        }
    }


    int count25_04_90 = manager.countReadersByOrderDate("25.04.90");
    cout << "   д) Количество читателей, заказавших книги 25.04.90: "
        << count25_04_90 << endl;

  
    cout << "\n3. ДЕМОНСТРАЦИЯ МЕТОДОВ GET И SET:" << endl;
    if (manager.getRecordCount() > 0) {
        // Получаем первую запись
        LibraryRecord sample = manager.getRecord(0);
        cout << "   Первая запись в коллекции:" << endl;
        cout << "   - Фамилия (метод get): " << sample.getLastName() << endl;


        sample.setLastName("Новиков");
        cout << "   - Фамилия после set: " << sample.getLastName() << endl;

  
        cout << "   - Оригинал в коллекции: "
            << manager.getRecord(0).getLastName() << endl;
    }

 
    cout << "\n4. ДЕМОНСТРАЦИЯ КОНСТРУКТОРА КОПИРОВАНИЯ:" << endl;

  
    LibraryRecord original("Тестов", "01.01.90", "10.01.90", true);
    cout << "   Создаем оригинальную запись: " << original.getLastName() << endl;


    LibraryRecord copy(original);
    cout << "   Создаем копию: " << copy.getLastName() << endl;


    copy.setLastName("ИзмененнаяКопия");
    cout << "\n   После изменения копии:" << endl;
    cout << "   - Оригинал: " << original.getLastName() << endl;
    cout << "   - Копия: " << copy.getLastName() << endl;
    cout << "   (Оригинал не изменился - это разные объекты)" << endl;

 
    cout << "\n5. ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ:" << endl;

  
    cout << "   а) Книги, выданные 20.09.90:" << endl;
    vector<string> readers20_09_90 = manager.getReadersByIssueDate("20.09.90");
    if (readers20_09_90.empty()) {
        cout << "      Никто" << endl;
    }
    else {
        for (const auto& reader : readers20_09_90) {
            cout << "      - " << reader << endl;
        }
    }

    // Статистика
    cout << "   б) Статистика:" << endl;
    cout << "      - Всего записей: " << manager.getRecordCount() << endl;
    cout << "      - Выданных книг: " << (manager.getRecordCount() - unsatisfied) << endl;
    cout << "      - Не выданных книг: " << unsatisfied << endl;


    cout << "\n==========================================" << endl;
    cout << "Программа завершена успешно!" << endl;
    cout << "==========================================" << endl;


#ifdef _WIN32
    system("pause");
#endif

    return 0;
}