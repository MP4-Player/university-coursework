#pragma once
#ifndef PATIENT_H
#define PATIENT_H

#include <string>
#include <vector>
#include <fstream>

struct Patient {
    std::string date;
    std::string fullName;
    std::string department;
    std::string reason;
    bool referred;
    std::string notes;

    // Конструктор по умолчанию
    Patient() : referred(false) {}

    // Параметризованный конструктор
    Patient(const std::string& d, const std::string& name,
        const std::string& dept, const std::string& r,
        bool ref, const std::string& n);

    void display() const;
    void writeToFile(std::ofstream& file) const;
    static Patient readFromFile(std::ifstream& file);
};

class PatientDatabase {
private:
    std::vector<Patient> patients;

public:
    void addPatient(const Patient& patient);
    void removePatient(int index);
    void displayAll() const;

    void displayByDate(const std::string& date) const;
    void displayReferredPatients() const;

    void saveToBinaryFile(const std::string& filename) const;
    void loadFromBinaryFile(const std::string& filename);
    Patient readPatientByIndex(const std::string& filename, int index) const;

    int getPatientCount() const;
    void clear();
};

#endif