#ifndef LIBRARYRECORD_H
#define LIBRARYRECORD_H

#include <iostream>
#include <string>
using namespace std;

class LibraryRecord {
private:
    string lastName;     // Фамилия читателя
    string orderDate;    // Дата заказа книги (формат "дд.мм.гг")
    string issueDate;    // Дата выдачи книги
    bool isIssued;       // Флаг: выдана ли книга (true - выдана, false - нет)

public:
    // КОНСТРУКТОРЫ:

    // 1. Конструктор по умолчанию - инициализирует объект пустыми значениями
    LibraryRecord();

    // 2. Параметризированный конструктор - создает объект с заданными значениями
    LibraryRecord(string ln, string od, string id, bool issued);

    // 3. Конструктор копирования - создает копию существующего объекта
    //    Важно: параметр передается по константной ссылке для избежания лишнего копирования
    LibraryRecord(const LibraryRecord& other);

    // ДЕСТРУКТОР:
    // Вызывается автоматически при уничтожении объекта
    ~LibraryRecord();

    // ГЕТТЕРЫ (методы доступа для чтения):
    // const в конце означает, что метод не изменяет состояние объекта
    string getLastName() const;
    string getOrderDate() const;
    string getIssueDate() const;
    bool getIsIssued() const;

    // СЕТТЕРЫ (методы для изменения полей):
    void setLastName(string ln);
    void setOrderDate(string od);
    void setIssueDate(string id);
    void setIsIssued(bool issued);

    // Вспомогательный метод для вычисления дней поиска книги
    int getSearchDays() const;

    // Старый метод для вывода информации (оставлен для обратной совместимости)
    void displayInfo() const;

    // =========== ПЕРЕГРУЖЕННЫЕ ОПЕРАТОРЫ ===========

    // 1. Оператор присваивания
    // Возвращает ссылку на текущий объект (*this) для поддержки цепочки присваиваний: a = b = c
    LibraryRecord& operator=(const LibraryRecord& other);

    // 2. Оператор сравнения на равенство
    // const в конце означает, что метод не изменяет объект
    // Возвращает true, если все поля объектов совпадают
    bool operator==(const LibraryRecord& other) const;

    // 3. Оператор сравнения "меньше"
    // Сравнивает объекты по фамилии (лексикографически)
    // Используется для сортировки объектов
    bool operator<(const LibraryRecord& other) const;

    // 4. Арифметический оператор сложения
    // Добавляет указанное количество дней к дате заказа
    // Возвращает новый объект (не изменяет текущий)
    LibraryRecord operator+(int days) const;

    // 5. Арифметический оператор вычитания
    // Здесь можно было бы реализовать разницу между датами,
    // но в данном примере это демонстрационная заглушка
    LibraryRecord operator-(const LibraryRecord& other) const;

    // 6. Дружественная функция для оператора вывода в поток
    // Дружественная функция имеет доступ к приватным полям класса
    // friend означает, что эта функция не является методом класса,
    // но имеет доступ к его приватным членам
    friend ostream& operator<<(ostream& os, const LibraryRecord& record);
};

#endif