#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cctype>
#include <stdexcept>
#include <locale>
#include <codecvt>
#include "file_operations.h"

using namespace std;


string toUTF8(const string& str) {
#ifdef _WIN32
    static bool localeSet = false;
    if (!localeSet) {
        locale::global(locale(""));
        localeSet = true;
    }
#endif
    return str;
}

bool FileOperations::fileExists(const string& filename) {
    ifstream file(filename);
    return file.good();
}

bool FileOperations::containsDigits(const string& word) {
    for (char c : word) {
        if (isdigit(static_cast<unsigned char>(c))) {
            return true;
        }
    }
    return false;
}

void FileOperations::removeWordsWithDigits(const string& filename) {
    if (!fileExists(filename)) {
        throw runtime_error("Ошибка: файл " + filename + " не существует!");
    }

    ifstream inputFile(filename, ios::binary);  
    if (!inputFile.is_open()) {
        throw runtime_error("Ошибка: не удалось открыть файл " + filename + " для чтения!");
    }

    string line;
    vector<string> processedLines;

    while (getline(inputFile, line)) {
        stringstream ss(line);
        string word;
        string newLine;

        while (ss >> word) {
            if (!containsDigits(word)) {
                if (!newLine.empty()) {
                    newLine += " ";
                }
                newLine += word;
            }
        }

        processedLines.push_back(newLine);
    }
    inputFile.close();

    ofstream outputFile(filename, ios::binary);  
    if (!outputFile.is_open()) {
        throw runtime_error("Ошибка: не удалось открыть файл " + filename + " для записи!");
    }

    for (const auto& processedLine : processedLines) {
        outputFile << processedLine << endl;
    }
    outputFile.close();

    cout << "Файл успешно обработан! Слова с цифрами удалены." << endl;
}

void FileOperations::filterLinesBySubstring(const string& inputFile,
    const string& outputFile,
    const string& substring) {
    if (!fileExists(inputFile)) {
        throw runtime_error("Ошибка: файл " + inputFile + " не существует!");
    }

    if (substring.empty()) {
        throw invalid_argument("Ошибка: подстрока не может быть пустой!");
    }

    string searchStr = toUTF8(substring);

    ifstream inFile(inputFile, ios::binary);  
    if (!inFile.is_open()) {
        throw runtime_error("Ошибка: не удалось открыть файл " + inputFile + " для чтения!");
    }

    vector<string> matchingLines;
    string line;
    bool found = false;

    while (getline(inFile, line)) {
        // Ищем подстроку в строке
        if (line.find(searchStr) != string::npos) {
            matchingLines.push_back(line);
            found = true;
        }
    }
    inFile.close();

    if (!found) {
        throw runtime_error("Подстрока '" + substring + "' не найдена в файле!");
    }

    ofstream outFile(outputFile, ios::binary);  // Бинарный режим
    if (!outFile.is_open()) {
        throw runtime_error("Ошибка: не удалось создать файл " + outputFile + "!");
    }

    for (const auto& matchingLine : matchingLines) {
        outFile << matchingLine << endl;
    }
    outFile.close();

    cout << "Файл " << outputFile << " успешно создан!" << endl;
    cout << "Найдено строк: " << matchingLines.size() << endl;
}