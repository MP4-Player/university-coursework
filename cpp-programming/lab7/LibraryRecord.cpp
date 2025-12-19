#include "LibraryRecord.h"
#include <sstream>
#include <iostream>
#include <stdexcept>




LibraryRecord::LibraryRecord() {
    lastName = "";
    orderDate = "";
    issueDate = "";
    isIssued = false;

    
}


LibraryRecord::LibraryRecord(string ln, string od, string id, bool issued)
    : lastName(ln), orderDate(od), issueDate(id), isIssued(issued) {
    
}



LibraryRecord::LibraryRecord(const LibraryRecord& other) {
    this->lastName = other.lastName;
    this->orderDate = other.orderDate;
    this->issueDate = other.issueDate;
    this->isIssued = other.isIssued;

    // cout << "Вызван конструктор копирования LibraryRecord" << endl;
}


LibraryRecord::~LibraryRecord() {
    
}


string LibraryRecord::getLastName() const {
    return lastName;
}

string LibraryRecord::getOrderDate() const {
    return orderDate;
}

string LibraryRecord::getIssueDate() const {
    return issueDate;
}

bool LibraryRecord::getIsIssued() const {
    return isIssued;
}

void LibraryRecord::setLastName(string lastName) {
    // this-> указатель используется для разрешения конфликта имен(на лекции небыло !)
    this->lastName = lastName;
}

void LibraryRecord::setOrderDate(string orderDate) {
    this->orderDate = orderDate;
}

void LibraryRecord::setIssueDate(string issueDate) {
    this->issueDate = issueDate;
}

void LibraryRecord::setIsIssued(bool isIssued) {
    this->isIssued = isIssued;
}

int LibraryRecord::getSearchDays() const {
    if (!isIssued || orderDate.empty() || issueDate.empty()) {
        return -1;
    }

    try {
        
        int orderDay = stoi(orderDate.substr(0, 2));
        int issueDay = stoi(issueDate.substr(0, 2));

        
        return issueDay - orderDay;
    }
    catch (const exception& e) {
       
        return -1;
    }
}


void LibraryRecord::displayInfo() const {
    cout << "Фамилия: " << lastName << endl;
    cout << "Дата заказа: " << orderDate << endl;
    cout << "Дата выдачи: " << (isIssued ? issueDate : "не выдана") << endl;
    cout << "Статус: " << (isIssued ? "выдана" : "не выдана") << endl;
    if (isIssued) {
        int days = getSearchDays();
        if (days >= 0) {
            cout << "Срок поиска: " << days << " дней" << endl;
        }
    }
    cout << "-------------------------" << endl;
}

LibraryRecord& LibraryRecord::operator=(const LibraryRecord& other) {
   
    if (this != &other) {
        // Копируем все поля из other в текущий объект
        lastName = other.lastName;
        orderDate = other.orderDate;
        issueDate = other.issueDate;
        isIssued = other.isIssued;
    }

    
    return *this;
}


bool LibraryRecord::operator==(const LibraryRecord& other) const {
    
    return (lastName == other.lastName &&
        orderDate == other.orderDate &&
        issueDate == other.issueDate &&
        isIssued == other.isIssued);
}


bool LibraryRecord::operator<(const LibraryRecord& other) const {
    
    return lastName < other.lastName;

   
}


LibraryRecord LibraryRecord::operator+(int days) const {
    
    LibraryRecord result = *this;

    try {
       
        int day = stoi(orderDate.substr(0, 2));

        
        day += days;

        
        string newDay = (day < 10 ? "0" : "") + to_string(day);

        // Сохраняем новую дату (оставляем месяц и год без изменений)
        result.orderDate = newDay + orderDate.substr(2);
    }
    catch (const exception& e) {
        
    }

    // Возвращаем новый объект (не изменяем текущий!)
    return result;
}


    LibraryRecord result = *this;
    return result;
}


// Дружественная функция operator<<
// Не является методом класса, но имеет доступ к его приватным полям
ostream& operator<<(ostream& os, const LibraryRecord& record) {
    // Выводим информацию в поток os (может быть cout, файл и т.д.)
    os << "Фамилия: " << record.lastName << "\n"
        << "Дата заказа: " << record.orderDate << "\n"
        << "Дата выдачи: " << (record.isIssued ? record.issueDate : "не выдана") << "\n"
        << "Статус: " << (record.isIssued ? "выдана" : "не выдана");

    // Если книга выдана, добавляем информацию о сроке поиска
    if (record.isIssued) {
        int days = record.getSearchDays();
        if (days >= 0) {
            os << "\nСрок поиска: " << days << " дней";
        }
    }

    // Возвращаем поток для поддержки цепочек вывода: cout << a << b << c;
    return os;
}