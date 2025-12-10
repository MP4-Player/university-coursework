#include "LibraryRecord.h"


LibraryRecord::LibraryRecord() {
    lastName = "";
    orderDate = "";
    issueDate = "";
    isIssued = false;
}


LibraryRecord::LibraryRecord(string lastName, string orderDate,
    string issueDate, bool isIssued) {
    this->lastName = lastName;
    this->orderDate = orderDate;
    this->issueDate = issueDate;
    this->isIssued = isIssued;
}


LibraryRecord::LibraryRecord(const LibraryRecord& other) {
    this->lastName = other.lastName;
    this->orderDate = other.orderDate;
    this->issueDate = other.issueDate;
    this->isIssued = other.isIssued;
}


LibraryRecord::~LibraryRecord() {}


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
    catch (...) {
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