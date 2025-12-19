#include "LibraryManager.h"
#include <iostream>
#include <algorithm>
#include <limits>

using namespace std;



// Конструктор по умолчанию
LibraryManager::LibraryManager() {
    
}

// Конструктор копирования
LibraryManager::LibraryManager(const LibraryManager& other) {
    // Копируем все записи из other в текущий объект
    // vector поддерживает оператор присваивания, который выполняет глубокое копирование
    this->records = other.records;

    // cout << "Вызван конструктор копирования LibraryManager" << endl;
}


LibraryManager::~LibraryManager() {
    

    // cout << "Вызван деструктор LibraryManager" << endl;
}



void LibraryManager::addRecord(const LibraryRecord& record) {
    // push_back добавляет копию record в конец вектора
    records.push_back(record);
}


vector<LibraryRecord> LibraryManager::getAllRecords() const {
    // Возвращаем копию вектора
    return records;
}


LibraryRecord LibraryManager::getRecord(int index) const {
    // Проверка корректности индекса
    if (index >= 0 && index < (int)records.size()) {
        // Возвращаем копию записи
        return records[index];
    }

   
    return LibraryRecord();
}

int LibraryManager::getRecordCount() const {
    // size() возвращает количество элементов в векторе
    // Приведение к int для совместимости
    return (int)records.size();
}


int LibraryManager::findMinSearchTime() const {
    int minTime = -1;  // Инициализируем специальным значением

    // Проходим по всем записям
    for (const auto& record : records) {
        // Проверяем, выдана ли книга
        if (record.getIsIssued()) {
            int searchTime = record.getSearchDays();

            // Если срок поиска корректен
            if (searchTime >= 0) {
                // Если это первый найденный срок или срок меньше текущего минимума
                if (minTime == -1 || searchTime < minTime) {
                    minTime = searchTime;
                }
            }
        }
    }

    return minTime;
}

// Подсчитать количество неудовлетворенных заказов
int LibraryManager::countUnsatisfiedOrders() const {
    int count = 0;

    // Проходим по всем записям
    for (const auto& record : records) {
        // Если книга не выдана, увеличиваем счетчик
        if (!record.getIsIssued()) {
            count++;
        }
    }

    return count;
}


string LibraryManager::findMostFrequentReader() const {
    // Используем map для подсчета количества посещений каждого читателя
    // Ключ - фамилия, значение - количество посещений
    map<string, int> readerCount;

    
    for (const auto& record : records) {
        string lastName = record.getLastName();
        readerCount[lastName]++;  // Увеличиваем счетчик для этой фамилии
    }

    string mostFrequent = "";
    int maxCount = 0;

    // Находим фамилию с максимальным количеством посещений
    for (const auto& pair : readerCount) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            mostFrequent = pair.first;
        }
    }

    return mostFrequent;
}


vector<string> LibraryManager::getReadersByIssueDate(string date) const {
    vector<string> result;

    // Проходим по всем записям
    for (const auto& record : records) {
        // Если книга выдана и дата выдачи совпадает с искомой
        if (record.getIsIssued() && record.getIssueDate() == date) {
            // Добавляем фамилию в результат
            result.push_back(record.getLastName());
        }
    }

    return result;
}

int LibraryManager::countReadersByOrderDate(string date) const {
    int count = 0;

    // Проходим по всем записям
    for (const auto& record : records) {
        // Если дата заказа совпадает с искомой
        if (record.getOrderDate() == date) {
            count++;
        }
    }

    return count;
}


void LibraryManager::displayAllRecords() const {
    cout << "=== ВСЕ ЗАПИСИ БИБЛИОТЕКИ ===" << endl;

    // Используем обычный цикл for с индексом
    for (size_t i = 0; i < records.size(); i++) {
        cout << "Запись #" << (i + 1) << ":" << endl;
        records[i].displayInfo();  // Используем старый метод displayInfo
    }
}


LibraryRecord& LibraryManager::operator[](int index) {
    // Проверка корректности индекса
    if (index >= 0 && index < (int)records.size()) {
        // Возвращаем ссылку на элемент, что позволяет его изменять
        return records[index];
    }

    
    static LibraryRecord dummy;
    return dummy;
}


const LibraryRecord& LibraryManager::operator[](int index) const {
    // Проверка корректности индекса
    if (index >= 0 && index < (int)records.size()) {
        // Возвращаем константную ссылку (нельзя изменить элемент)
        return records[index];
    }

    // Если индекс некорректен
    static LibraryRecord dummy;
    return dummy;
}


// Дружественная функция operator<< для LibraryManager
ostream& operator<<(ostream& os, const LibraryManager& manager) {
    // Выводим заголовок с количеством записей
    os << "=== ВСЕ ЗАПИСИ БИБЛИОТЕКИ (" << manager.records.size() << " записей) ===" << endl;

    // Проходим по всем записям
    for (size_t i = 0; i < manager.records.size(); i++) {
        os << "\nЗапись #" << (i + 1) << ":\n";

        // Используем перегруженный operator<< для LibraryRecord
        os << manager.records[i] << endl;

        os << "-------------------------";
    }

    // Возвращаем поток для поддержки цепочек вывода
    return os;
}