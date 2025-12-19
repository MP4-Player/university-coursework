#ifndef LIBRARYMANAGER_H
#define LIBRARYMANAGER_H

#include "LibraryRecord.h"
#include <vector>
#include <map>

using namespace std;

class LibraryManager {
private:
    // Коллекция записей о книгах
    // Используем vector для хранения объектов LibraryRecord
    vector<LibraryRecord> records;

public:
    // КОНСТРУКТОРЫ И ДЕСТРУКТОР:

    // Конструктор по умолчанию
    LibraryManager();

    // Конструктор копирования
    LibraryManager(const LibraryManager& other);

    // Деструктор
    ~LibraryManager();

    // БАЗОВЫЕ МЕТОДЫ ДЛЯ РАБОТЫ С КОЛЛЕКЦИЕЙ:

    // Добавление новой записи в коллекцию
    void addRecord(const LibraryRecord& record);

    // Получение всех записей (возвращает копию вектора)
    vector<LibraryRecord> getAllRecords() const;

    // Получение записи по индексу (старый метод)
    LibraryRecord getRecord(int index) const;

    // Получение количества записей
    int getRecordCount() const;

    // МЕТОДЫ ДЛЯ АНАЛИЗА ДАННЫХ (по заданию варианта 3):

    // 1. Найти самый маленький срок поиска книги
    int findMinSearchTime() const;

    // 2. Подсчитать количество неудовлетворенных заказов
    int countUnsatisfiedOrders() const;

    // 3. Найти самого частого читателя
    string findMostFrequentReader() const;

    // 4. Получить список читателей, получивших книги в указанную дату
    vector<string> getReadersByIssueDate(string date) const;

    // 5. Подсчитать количество читателей, заказавших книги в указанную дату
    int countReadersByOrderDate(string date) const;

    // Старый метод для вывода всех записей
    void displayAllRecords() const;

    // =========== ПЕРЕГРУЖЕННЫЕ ОПЕРАТОРЫ ===========

    // 1. Оператор индексации (неконстантная версия)
    // Возвращает ссылку на элемент, что позволяет изменять его: manager[0] = record;
    LibraryRecord& operator[](int index);

    // 2. Оператор индексации (константная версия)
    // Используется, когда объект LibraryManager объявлен как const
    // Не позволяет изменять элементы: const LibraryManager& m = manager; m[0];
    const LibraryRecord& operator[](int index) const;

    // 3. Дружественная функция для вывода всей коллекции
    // Выводит информацию обо всех записях в удобном формате
    friend ostream& operator<<(ostream& os, const LibraryManager& manager);
};

#endif