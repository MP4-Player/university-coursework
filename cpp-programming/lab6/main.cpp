#include <iostream>
#include <locale>
#include <cstdlib>
#ifdef _WIN32
#include <windows.h>
#endif
#include "Wine.h"

using namespace std;


void setRussianEncoding() {
#ifdef _WIN32
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);
#else
    setlocale(LC_ALL, "ru_RU.UTF-8");
#endif
}

int main() {
  
    setRussianEncoding();

    cout << "==================================================" << endl;
    cout << "Лабораторная работа №6, вариант 3" << endl;
    cout << "Класс: Wine (Вина)" << endl;
    cout << "==================================================" << endl << endl;

   
    cout << "=== 1. ТЕСТ ОСНОВНОГО КЛАССА WINE ===" << endl << endl;


    cout << "1.1 При входе в main создано объектов Wine: " << Wine::getCounter() << endl << endl;

    cout << "1.2 Создаём массив из 3 вин (статически):" << endl;
    Wine* wines[3];
    wines[0] = Wine::createWine("Красное сухое", 12.5, 1.05);
    wines[1] = Wine::createWine("Белое полусладкое", 10.0, 1.03);
    wines[2] = Wine::createWine("Розовое", 9.5, 1.02);
    cout << "   Всего объектов Wine после создания массива: " << Wine::getCounter() << endl << endl;

    cout << "1.3 Динамическое создание объекта:" << endl;
    Wine* dynamicWine = Wine::createWine("Игристое", 11.0, 1.04);
    cout << "   Всего объектов Wine после динамического создания: " << Wine::getCounter() << endl << endl;


    cout << "1.4 Работа с методами класса:" << endl;
    wines[0]->age();
    wines[1]->dilute(0.1);
    cout << endl;


    cout << "1.5 Использование дружественной функции:" << endl;
    printWineInfo(*wines[2]);
    cout << endl;

  
    cout << "1.6 Удаление динамического объекта:" << endl;
    Wine::destroyWine(dynamicWine);
    cout << "   Всего объектов Wine после удаления: " << Wine::getCounter() << endl << endl;


    cout << "1.7 Удаление массива объектов:" << endl;
    for (int i = 0; i < 3; i++) {
        Wine::destroyWine(wines[i]);
    }
    cout << "   Всего объектов Wine в конце: " << Wine::getCounter() << endl << endl;

  
    cout << "=== 2. ТЕСТ КЛАССА SECRETWINE (с методами внутри класса) ===" << endl << endl;

    cout << "2.1 Создание объектов через статические методы класса:" << endl;
    SecretWine* secret1 = SecretWine::createSecret("Секретное Бордо", 14.5);
    SecretWine* secret2 = SecretWine::createSecret("Секретное Шампанское", 12.0);

    cout << endl << "2.2 Использование методов объектов:" << endl;
    secret1->display();
    secret2->display();

    cout << endl << "2.3 Удаление объектов через статические методы класса:" << endl;
    SecretWine::destroySecret(secret1);
    SecretWine::destroySecret(secret2);
    cout << endl;


    cout << "=== 3. ТЕСТ КЛАССА HIDDENWINE (с внешними функциями) ===" << endl << endl;

    cout << "3.1 Создание объектов через внешние функции:" << endl;
    HiddenWine* hidden1 = createHiddenWine("Скрытое Мерло", 13.5);
    HiddenWine* hidden2 = createHiddenWine("Скрытое Совиньон", 11.5);

    cout << endl << "3.2 Использование внешних функций:" << endl;
    displayHiddenWine(hidden1);
    displayHiddenWine(hidden2);

    cout << endl << "3.3 Удаление объектов через внешние функции:" << endl;
    destroyHiddenWine(hidden1);
    destroyHiddenWine(hidden2);
    cout << endl;

    
    cout << "=== 4. ИТОГОВАЯ ПРОВЕРКА ===" << endl << endl;
    cout << "Количество объектов Wine в самом конце программы: " << Wine::getCounter() << endl;

    if (Wine::getCounter() == 0) {
        cout << "✓ Все объекты Wine корректно удалены!" << endl;
    }
    else {
        cout << "✗ Обнаружена утечка памяти!" << endl;
    }

    cout << endl << "==================================================" << endl;
    cout << "Программа успешно завершена!" << endl;
    cout << "==================================================" << endl;


#ifdef _WIN32
    system("pause");
#endif

    return 0;
}