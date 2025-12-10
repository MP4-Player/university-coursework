#include "LibraryManager.h"


LibraryManager::LibraryManager() {}


LibraryManager::LibraryManager(const LibraryManager& other) {
    this->records = other.records;
}


LibraryManager::~LibraryManager() {}


void LibraryManager::addRecord(const LibraryRecord& record) {
    records.push_back(record);
}


vector<LibraryRecord> LibraryManager::getAllRecords() const {
    return records;
}


LibraryRecord LibraryManager::getRecord(int index) const {
    if (index >= 0 && index < records.size()) {
        return records[index];
    }
    return LibraryRecord();
}


int LibraryManager::getRecordCount() const {
    return records.size();
}


int LibraryManager::findMinSearchTime() const {
    int minTime = -1;

    for (const auto& record : records) {
        if (record.getIsIssued()) {
            int searchTime = record.getSearchDays();
            if (searchTime >= 0) {
                if (minTime == -1 || searchTime < minTime) {
                    minTime = searchTime;
                }
            }
        }
    }

    return minTime;
}


int LibraryManager::countUnsatisfiedOrders() const {
    int count = 0;

    for (const auto& record : records) {
        if (!record.getIsIssued()) {
            count++;
        }
    }

    return count;
}


string LibraryManager::findMostFrequentReader() const {
    map<string, int> readerCount;

    for (const auto& record : records) {
        string lastName = record.getLastName();
        readerCount[lastName]++;
    }

    string mostFrequent = "";
    int maxCount = 0;

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

    for (const auto& record : records) {
        if (record.getIsIssued() && record.getIssueDate() == date) {
            result.push_back(record.getLastName());
        }
    }

    return result;
}


int LibraryManager::countReadersByOrderDate(string date) const {
    int count = 0;

    for (const auto& record : records) {
        if (record.getOrderDate() == date) {
            count++;
        }
    }

    return count;
}


void LibraryManager::displayAllRecords() const {
    cout << "=== ÂÑÅ ÇÀÏÈÑÈ ÁÈÁËÈÎÒÅÊÈ ===" << endl;

    for (size_t i = 0; i < records.size(); i++) {
        cout << "Çàïèñü #" << (i + 1) << ":" << endl;
        records[i].displayInfo();
    }
}