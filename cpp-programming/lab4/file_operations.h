#ifndef FILE_OPERATIONS_H
#define FILE_OPERATIONS_H

#include <string>
#include <vector>

class FileOperations {
public:
    static void removeWordsWithDigits(const std::string& filename);

    static void filterLinesBySubstring(const std::string& inputFile,
        const std::string& outputFile,
        const std::string& substring);

    static bool containsDigits(const std::string& word);
    static bool fileExists(const std::string& filename);
};

#endif#pragma once
