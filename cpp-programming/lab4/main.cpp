#include <iostream>
#include <string>
#include <stdexcept>
#include <locale>
#include <windows.h>  
#include "file_operations.h"
#include "patient.h"

using namespace std;


void setupRussianConsole() {
#ifdef _WIN32
    
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
#endif

    setlocale(LC_ALL, "Russian");

}

string inputString(const string& prompt) {
    cout << prompt;
    string result;


    cin.clear();
    cin.ignore(cin.rdbuf()->in_avail());
    getline(cin, result);

    return result;
}

void demoTask1() {
    cout << "\n=== ЗАДАНИЕ 1: УДАЛЕНИЕ СЛОВ С ЦИФРАМИ ===" << endl;

    string filename = inputString("Введите имя файла (например: test.txt): ");

    try {
        FileOperations::removeWordsWithDigits(filename);
        cout << "✓ Файл успешно обработан!" << endl;
    }
    catch (const exception& e) {
        cout << "✗ Ошибка: " << e.what() << endl;
    }
}

void demoTask2() {
    cout << "\n=== ЗАДАНИЕ 2: ФИЛЬТРАЦИЯ СТРОК ПО ПОДСТРОКЕ ===" << endl;

    string inputFile = inputString("Введите имя входного файла: ");
    string outputFile = inputString("Введите имя выходного файла: ");

    bool success = false;
    int attempts = 0;

    while (!success && attempts < 3) {
        string substring = inputString("Введите подстроку для поиска: ");

        try {
            FileOperations::filterLinesBySubstring(inputFile, outputFile, substring);
            success = true;
        }
        catch (const exception& e) {
            cout << "✗ Ошибка: " << e.what() << endl;
            attempts++;

            if (attempts < 3) {
                char choice;
                cout << "Повторить ввод подстроки? (y/n): ";
                cin >> choice;
                cin.ignore();  // Очищаем буфер

                if (choice != 'y' && choice != 'Y') {
                    break;
                }
            }
            else {
                cout << "Достигнуто максимальное количество попыток." << endl;
            }
        }
    }
}

void demoTask3() {
    cout << "\n=== ЗАДАНИЕ 3: БАЗА ПАЦИЕНТОВ ===" << endl;

    PatientDatabase database;
    string binaryFile = "patients.dat";

    cout << "Добавление тестовых пациентов..." << endl;

    database.addPatient(Patient("2024-01-15", "Иванов Иван Иванович",
        "Кафедра информатики", "Головная боль",
        false, "Принял анальгин"));

    database.addPatient(Patient("2024-01-15", "Петрова Анна Сергеевна",
        "Отдел кадров", "Высокая температура",
        true, "Направлен в больницу"));

    database.addPatient(Patient("2024-01-16", "Сидоров Алексей Петрович",
        "Бухгалтерия", "Травма руки",
        false, "Наложен гипс"));

    database.addPatient(Patient("2024-01-16", "Козлова Мария Владимировна",
        "Кафедра математики", "Аллергия",
        true, "Направлен к аллергологу"));

    try {
        database.saveToBinaryFile(binaryFile);
    }
    catch (const exception& e) {
        cout << "✗ Ошибка сохранения: " << e.what() << endl;
    }

    int choice;
    do {
        cout << "\n=== МЕНЮ БАЗЫ ПАЦИЕНТОВ ===" << endl;
        cout << "1. Показать всех пациентов" << endl;
        cout << "2. Найти пациентов по дате" << endl;
        cout << "3. Показать направленных пациентов" << endl;
        cout << "4. Загрузить из файла в новую базу" << endl;
        cout << "5. Прочитать пациента по номеру из файла" << endl;
        cout << "6. Добавить нового пациента" << endl;
        cout << "0. Выход в главное меню" << endl;
        cout << "Выберите действие: ";

        cin >> choice;
        cin.ignore();  

        try {
            switch (choice) {
            case 1:
                database.displayAll();
                break;

            case 2: {
                string date = inputString("Введите дату (гггг-мм-дд): ");
                database.displayByDate(date);
                break;
            }

            case 3:
                database.displayReferredPatients();
                break;

            case 4: {
                PatientDatabase newDb;
                newDb.loadFromBinaryFile(binaryFile);
                cout << "\n=== ЗАГРУЖЕННЫЕ ДАННЫЕ ===" << endl;
                newDb.displayAll();
                break;
            }

            case 5: {
                int index;
                cout << "Введите номер пациента (1-" << database.getPatientCount() << "): ";
                cin >> index;
                cin.ignore();

                if (index < 1 || index > database.getPatientCount()) {
                    cout << "✗ Неверный номер!" << endl;
                }
                else {
                    cout << "\n=== ПАЦИЕНТ #" << index << " ===" << endl;
                    Patient p = database.readPatientByIndex(binaryFile, index - 1);
                    p.display();
                }
                break;
            }

            case 6: {
                cout << "\n--- ДОБАВЛЕНИЕ НОВОГО ПАЦИЕНТА ---" << endl;
                string date = inputString("Дата (гггг-мм-дд): ");
                string name = inputString("Ф.И.О.: ");
                string dept = inputString("Отдел: ");
                string reason = inputString("Причина обращения: ");

                cout << "Направлен в другое учреждение? (y/n): ";
                char refChoice;
                cin >> refChoice;
                cin.ignore();
                bool referred = (refChoice == 'y' || refChoice == 'Y');

                string notes = inputString("Примечание: ");

                database.addPatient(Patient(date, name, dept, reason, referred, notes));
                database.saveToBinaryFile(binaryFile);
                break;
            }

            case 0:
                cout << "Выход в главное меню..." << endl;
                break;

            default:
                cout << "✗ Неверный выбор!" << endl;
            }
        }
        catch (const exception& e) {
            cout << "✗ Ошибка: " << e.what() << endl;
        }

    } while (choice != 0);
}

int main() {
   
    setupRussianConsole();

    cout << "==========================================" << endl;
    cout << "  ЛАБОРАТОРНАЯ РАБОТА №4" << endl;
    cout << "  Работа с файлами, классами и исключениями" << endl;
    cout << "  Вариант 3" << endl;
    cout << "==========================================" << endl;

    int choice;
    do {
        cout << "\n=== ГЛАВНОЕ МЕНЮ ===" << endl;
        cout << "1. Задание 1 - Удаление слов с цифрами" << endl;
        cout << "2. Задание 2 - Фильтрация строк по подстроке" << endl;
        cout << "3. Задание 3 - База пациентов" << endl;
        cout << "0. Выход из программы" << endl;
        cout << "Выберите задание: ";

        cin >> choice;
        cin.ignore();  

        switch (choice) {
        case 1:
            demoTask1();
            break;
        case 2:
            demoTask2();
            break;
        case 3:
            demoTask3();
            break;
        case 0:
            cout << "\nПрограмма завершена. До свидания!" << endl;
            break;
        default:
            cout << "✗ Неверный выбор!" << endl;
        }

        
        if (choice != 0) {
            cout << "\nНажмите Enter для продолжения...";
            cin.get();
        }

    } while (choice != 0);

    return 0;
}