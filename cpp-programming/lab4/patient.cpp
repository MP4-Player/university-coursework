#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>
#include <locale>
#include "patient.h"

using namespace std;

Patient::Patient(const string& d, const string& name,
    const string& dept, const string& r,
    bool ref, const string& n)
    : date(d), fullName(name), department(dept),
    reason(r), referred(ref), notes(n) {
}

void Patient::display() const {
    cout << "Дата: " << date << endl;
    cout << "Ф.И.О.: " << fullName << endl;
    cout << "Отдел: " << department << endl;
    cout << "Причина: " << reason << endl;
    cout << "Направлен: " << (referred ? "Да" : "Нет") << endl;
    cout << "Примечание: " << notes << endl;
    cout << "------------------------" << endl;
}

void Patient::writeToFile(ofstream& file) const {
    size_t len = date.size();
    file.write(reinterpret_cast<const char*>(&len), sizeof(len));
    file.write(date.c_str(), len);

    len = fullName.size();
    file.write(reinterpret_cast<const char*>(&len), sizeof(len));
    file.write(fullName.c_str(), len);

    len = department.size();
    file.write(reinterpret_cast<const char*>(&len), sizeof(len));
    file.write(department.c_str(), len);

    len = reason.size();
    file.write(reinterpret_cast<const char*>(&len), sizeof(len));
    file.write(reason.c_str(), len);

    file.write(reinterpret_cast<const char*>(&referred), sizeof(referred));

    len = notes.size();
    file.write(reinterpret_cast<const char*>(&len), sizeof(len));
    file.write(notes.c_str(), len);
}

Patient Patient::readFromFile(ifstream& file) {
    Patient patient;
    size_t len;

    file.read(reinterpret_cast<char*>(&len), sizeof(len));
    patient.date.resize(len);
    file.read(&patient.date[0], len);

    file.read(reinterpret_cast<char*>(&len), sizeof(len));
    patient.fullName.resize(len);
    file.read(&patient.fullName[0], len);

    file.read(reinterpret_cast<char*>(&len), sizeof(len));
    patient.department.resize(len);
    file.read(&patient.department[0], len);

    file.read(reinterpret_cast<char*>(&len), sizeof(len));
    patient.reason.resize(len);
    file.read(&patient.reason[0], len);

    file.read(reinterpret_cast<char*>(&patient.referred), sizeof(patient.referred));

    file.read(reinterpret_cast<char*>(&len), sizeof(len));
    patient.notes.resize(len);
    file.read(&patient.notes[0], len);

    return patient;
}

void PatientDatabase::addPatient(const Patient& patient) {
    patients.push_back(patient);
    cout << "✓ Пациент добавлен!" << endl;
}

void PatientDatabase::removePatient(int index) {
    if (index < 0 || index >= (int)patients.size()) {
        throw out_of_range("Неверный индекс пациента!");
    }
    patients.erase(patients.begin() + index);
    cout << "✓ Пациент удален!" << endl;
}

void PatientDatabase::displayAll() const {
    if (patients.empty()) {
        cout << "База пациентов пуста!" << endl;
        return;
    }

    cout << "\n=== ВСЕ ПАЦИЕНТЫ (" << patients.size() << ") ===" << endl;
    for (size_t i = 0; i < patients.size(); i++) {
        cout << "Пациент #" << i + 1 << ":" << endl;
        patients[i].display();
    }
}

void PatientDatabase::displayByDate(const string& date) const {
    cout << "\n=== ПАЦИЕНТЫ ЗА " << date << " ===" << endl;
    bool found = false;

    for (size_t i = 0; i < patients.size(); i++) {
        if (patients[i].date == date) {
            cout << "Пациент #" << i + 1 << ":" << endl;
            patients[i].display();
            found = true;
        }
    }

    if (!found) {
        cout << "Пациентов за указанную дату не найдено." << endl;
    }
}

void PatientDatabase::displayReferredPatients() const {
    cout << "\n=== НАПРАВЛЕННЫЕ ПАЦИЕНТЫ ===" << endl;
    bool found = false;

    for (size_t i = 0; i < patients.size(); i++) {
        if (patients[i].referred) {
            cout << "Пациент #" << i + 1 << ":" << endl;
            patients[i].display();
            found = true;
        }
    }

    if (!found) {
        cout << "Направленных пациентов не найдено." << endl;
    }
}

void PatientDatabase::saveToBinaryFile(const string& filename) const {
    ofstream file(filename, ios::binary);
    if (!file.is_open()) {
        throw runtime_error("Ошибка создания файла: " + filename);
    }

    size_t count = patients.size();
    file.write(reinterpret_cast<const char*>(&count), sizeof(count));

    for (const auto& patient : patients) {
        patient.writeToFile(file);
    }

    file.close();
    cout << "✓ Данные сохранены в файл: " << filename << " (" << count << " записей)" << endl;
}

void PatientDatabase::loadFromBinaryFile(const string& filename) {
    ifstream file(filename, ios::binary);
    if (!file.is_open()) {
        throw runtime_error("Ошибка открытия файла: " + filename);
    }

    size_t count;
    file.read(reinterpret_cast<char*>(&count), sizeof(count));

    patients.clear();
    patients.reserve(count);

    for (size_t i = 0; i < count; i++) {
        patients.push_back(Patient::readFromFile(file));
    }

    file.close();
    cout << "✓ Данные загружены из файла: " << filename << " (" << count << " записей)" << endl;
}

Patient PatientDatabase::readPatientByIndex(const string& filename, int index) const {
    ifstream file(filename, ios::binary);
    if (!file.is_open()) {
        throw runtime_error("Ошибка открытия файла: " + filename);
    }

    size_t count;
    file.read(reinterpret_cast<char*>(&count), sizeof(count));

    if (index < 0 || index >= (int)count) {
        file.close();
        throw out_of_range("Неверный индекс пациента! Доступно: 1-" + to_string(count));
    }

    for (int i = 0; i < index; i++) {
        Patient::readFromFile(file);
    }

    Patient patient = Patient::readFromFile(file);
    file.close();

    return patient;
}

int PatientDatabase::getPatientCount() const {
    return (int)patients.size();
}

void PatientDatabase::clear() {
    patients.clear();
    cout << "✓ База данных очищена!" << endl;
}