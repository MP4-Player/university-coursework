#ifndef LIBRARYMANAGER_H
#define LIBRARYMANAGER_H

#include "LibraryRecord.h"
#include <vector>
#include <map>

using namespace std;

class LibraryManager {
private:
    vector<LibraryRecord> records;

public:
   
    LibraryManager();
    LibraryManager(const LibraryManager& other);
    ~LibraryManager();

    
    void addRecord(const LibraryRecord& record);
    vector<LibraryRecord> getAllRecords() const;
    LibraryRecord getRecord(int index) const;
    int getRecordCount() const;

    int findMinSearchTime() const;
    int countUnsatisfiedOrders() const;
    string findMostFrequentReader() const;
    vector<string> getReadersByIssueDate(string date) const;
    int countReadersByOrderDate(string date) const;
    void displayAllRecords() const;
};

#endif