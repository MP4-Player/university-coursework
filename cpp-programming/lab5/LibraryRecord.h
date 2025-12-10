#ifndef LIBRARYRECORD_H  
#define LIBRARYRECORD_H  

#include <iostream>      
#include <string>        
using namespace std;     


class LibraryRecord {
private:  
    string lastName;     
    string orderDate;    
    string issueDate;    
    bool isIssued;       

public:  
    
    LibraryRecord();

    
    
    LibraryRecord(string ln, string od, string id, bool issued);

    
    LibraryRecord(const LibraryRecord& other);

    
    ~LibraryRecord();

    
    string getLastName() const;

    
    string getOrderDate() const;

    
    string getIssueDate() const;

    
    bool getIsIssued() const;

    
    void setLastName(string ln);

   
    void setOrderDate(string od);

   
    void setIssueDate(string id);

    
    void setIsIssued(bool issued);

    
    int getSearchDays() const;

    
    void displayInfo() const;
};

#endif