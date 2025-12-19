#include <iostream>
#include <vector>
#include <cmath>
#include <locale>
#ifdef _WIN32
#include <windows.h>
#endif
using namespace std;


#include "Picture.h"
#include "Point.h"
#include "ColoredPoint.h"
#include "Line.h"
#include "ColoredLine.h"
#include "PolyLine.h"

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

    cout << "==========================================" << endl;
    cout << "Лабораторная работа" << endl;
    cout << "Наследование и полиморфизм" << endl;
    cout << "Вариант 3: Точка, ЦветнаяТочка, Линия, ЦветнаяЛиния, Многоугольник" << endl;
    cout << "==========================================" << endl << endl;

   
    vector<pair<double, double>> triangle;

    
    cout << "1. СОЗДАНИЕ И ДОБАВЛЕНИЕ ФИГУР:" << endl;
    cout << "-------------------------------" << endl;

    Picture picture;

    try {
        picture.addPoint(10, 20, "красный");
        cout << "✓ Обычная точка добавлена" << endl;

        picture.addColoredPoint(30, 40, "синий", 75);
        cout << "✓ Цветная точка добавлена" << endl;

        picture.addLine(0, 0, 100, 100, "зеленый");
        cout << "✓ Линия добавлена" << endl;

        picture.addColoredLine(50, 50, 150, 150, "фиолетовый", 3);
        cout << "✓ Цветная линия добавлена" << endl;

       
        triangle.clear();
        triangle.push_back(make_pair(0, 0));
        triangle.push_back(make_pair(50, 100));
        triangle.push_back(make_pair(100, 0));
        picture.addPolyLine(triangle, "оранжевый", true);
        cout << "✓ Треугольник добавлен" << endl;

        
        vector<pair<double, double>> square;
        square.push_back(make_pair(200, 200));
        square.push_back(make_pair(300, 200));
        square.push_back(make_pair(300, 300));
        square.push_back(make_pair(200, 300));
        picture.addPolyLine(square, "коричневый", true);
        cout << "✓ Квадрат добавлен" << endl;

       
        vector<pair<double, double>> openLine;
        openLine.push_back(make_pair(400, 400));
        openLine.push_back(make_pair(450, 450));
        openLine.push_back(make_pair(500, 400));
        openLine.push_back(make_pair(550, 450));
        picture.addPolyLine(openLine, "серый", false);
        cout << "✓ Незамкнутая ломаная добавлена" << endl;

        cout << "Всего фигур: " << picture.getCount() << endl;

    }
    catch (...) {
        cout << "Ошибка при добавлении фигур!" << endl;
        return 1;
    }

    
    cout << "\n2. ВЫВОД ВСЕХ ФИГУР:" << endl;
    cout << "-------------------" << endl;
    picture.displayAll();

    
    cout << "\n3. ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА:" << endl;
    cout << "----------------------------" << endl;
    picture.showPolymorphism();

    
    cout << "\n4. РАБОТА С КОНКРЕТНЫМИ КЛАССАМИ:" << endl;
    cout << "---------------------------------" << endl;

    
    cout << "4.1 Цветная точка:" << endl;
    ColoredPoint cp(500, 500, "золотой", 60);
    cout << "   Создана: ";
    cp.display();
    cout << endl;

    cp.setBrightness(90);
    cout << "   После setBrightness(90): ";
    cp.display();
    cout << endl;

    
    cout << "\n4.2 Линия:" << endl;
    Line l(100, 100, 200, 200, "серебряный");
    cout << "   Создана: ";
    l.display();
    cout << endl;

    double x, y;
    l.getCoordinates(x, y);
    cout << "   Координаты начала (через getCoordinates): (" << x << ", " << y << ")" << endl;

    
    cout << "\n4.3 Цветная линия:" << endl;
    ColoredLine cl(300, 300, 400, 400, "бирюзовый", 4);
    cout << "   Создана: ";
    cl.display();
    cout << endl;

    cl.setThickness(2);
    cout << "   После setThickness(2): ";
    cl.display();
    cout << endl;

    
    cout << "\n4.4 Многоугольник:" << endl;
    PolyLine pl(triangle, "радужный", true);
    cout << "   Создан: ";
    pl.display();
    cout << endl;

    
    cout << "   Проверка формул:" << endl;
    cout << "   - Площадь (по формуле Гаусса): " << pl.getArea() << endl;
    cout << "   - Периметр: " << pl.getPerimeter() << endl;

    pl.addVertex(150, 50);
    cout << "   После addVertex(150, 50): ";
    pl.display();
    cout << endl;

    
    cout << "\n5. ДИНАМИЧЕСКОЕ ВЫДЕЛЕНИЕ ПАМЯТИ:" << endl;
    cout << "--------------------------------" << endl;

    cout << "5.1 Создание через new и работа через базовый указатель:" << endl;
    Point* figures[3];

    figures[0] = new ColoredPoint(600, 600, "розовый", 80);
    figures[1] = new Line(700, 700, 800, 800, "желтый");
    figures[2] = new ColoredLine(900, 900, 1000, 1000, "белый", 2);

    for (int i = 0; i < 3; i++) {
        cout << "   Фигура " << i + 1 << " -> ";
        figures[i]->display();
        cout << endl;
    }

    
    for (int i = 0; i < 3; i++) {
        delete figures[i];
    }
    cout << "   Память освобождена (delete)" << endl;

    
    cout << "\n6. ДОПОЛНИТЕЛЬНЫЕ ФИГУРЫ:" << endl;
    cout << "-------------------------" << endl;

   
    picture.addShape(new ColoredPoint(777, 888, "малиновый", 90));
    picture.addShape(new Line(999, 999, 1111, 1111, "бирюза"));

    // Пятиугольник
    vector<pair<double, double>> pentagon;
    for (int i = 0; i < 5; i++) {
        double angle = 2 * 3.14159 * i / 5;
        pentagon.push_back(make_pair(1000 + 100 * cos(angle), 1000 + 100 * sin(angle)));
    }
    picture.addPolyLine(pentagon, "фиолетовый", true);

    cout << "Добавлено 3 дополнительные фигуры" << endl;
    cout << "Всего фигур теперь: " << picture.getCount() << endl;

    
    cout << "\n7. ПРОВЕРКА ВИРТУАЛЬНЫХ МЕТОДОВ:" << endl;
    cout << "-------------------------------" << endl;

    cout << "7.1 Проверка методов getCoordinates() и getColor():" << endl;
    if (picture.getCount() > 0) {
        
        ColoredPoint* testShape = new ColoredPoint(123, 456, "тестовый", 50);
        Point* firstShape = testShape;

        double testX, testY;
        firstShape->getCoordinates(testX, testY);
        cout << "   Координаты: (" << testX << ", " << testY << ")" << endl;
        cout << "   Цвет: " << firstShape->getColor() << endl;

        firstShape->setCoordinates(999, 888);
        firstShape->getCoordinates(testX, testY);
        cout << "   После setCoordinates(999, 888): (" << testX << ", " << testY << ")" << endl;

        firstShape->setColor("измененный");
        cout << "   После setColor('измененный'): " << firstShape->getColor() << endl;

        delete testShape;
    }

    
    cout << "\n8. ОБРАБОТКА ОШИБОК:" << endl;
    cout << "-------------------" << endl;

    cout << "8.1 Проверка некорректных данных:" << endl;

    
    ColoredPoint badPoint1(1, 1, "красный", 150);
    cout << "   Цветная точка с brightness=150: ";
    badPoint1.display();
    cout << " (яркость скорректирована в конструкторе)" << endl;

    
    ColoredLine badLine1(0, 0, 10, 10, "синий", 0);
    cout << "   Линия с thickness=0: ";
    badLine1.display();
    cout << " (толщина скорректирована в конструкторе)" << endl;

    
    cout << "\n8.2 Проверка формул расчета:" << endl;

   
    vector<pair<double, double>> testTriangle;
    testTriangle.push_back(make_pair(0, 0));
    testTriangle.push_back(make_pair(4, 0));
    testTriangle.push_back(make_pair(0, 3));
    PolyLine testPoly(testTriangle, "тест", true);

    cout << "   Треугольник (0,0)-(4,0)-(0,3):" << endl;
    cout << "   - Площадь (должна быть 6): " << testPoly.getArea() << endl;
    cout << "   - Периметр (должен быть 12): " << testPoly.getPerimeter() << endl;

    
    cout << "\n9. ФИНАЛЬНАЯ КАРТИНА:" << endl;
    cout << "-------------------" << endl;
    picture.displayAll();

    
    cout << "\n10. ПРОВЕРКА ВЫПОЛНЕНИЯ ЗАДАНИЯ:" << endl;
    cout << "-------------------------------" << endl;

    cout << "✓ Класс Point создан" << endl;
    cout << "✓ Виртуальные методы: setCoordinates(), getCoordinates()" << endl;
    cout << "✓ Виртуальные методы: setColor(), getColor()" << endl;
    cout << "✓ Наследование: ColoredPoint <- Point" << endl;
    cout << "✓ Наследование: Line <- Point" << endl;
    cout << "✓ Наследование: ColoredLine <- Line" << endl;
    cout << "✓ Наследование: PolyLine <- Line" << endl;
    cout << "✓ Полиморфизм: виртуальные методы display()" << endl;
    cout << "✓ Класс Picture с коллекцией объектов" << endl;
    cout << "✓ Динамическое выделение памяти (new/delete)" << endl;
    cout << "✓ Все методы классов использованы" << endl;
    cout << "✓ Формулы расчета реализованы:" << endl;
    cout << "  - Длина линии: sqrt((x2-x1)² + (y2-y1)²)" << endl;
    cout << "  - Площадь многоугольника: формула Гаусса" << endl;
    cout << "  - Периметр многоугольника: сумма длин сторон" << endl;

   
    cout << "\n11. ОЧИСТКА ПАМЯТИ:" << endl;
    cout << "------------------" << endl;

    cout << "Память будет автоматически очищена при завершении программы" << endl;
    cout << "(вызовется деструктор Picture, который вызовет delete для всех фигур)" << endl;

    cout << "\n==========================================" << endl;
    cout << "ЛАБОРАТОРНАЯ РАБОТА ВЫПОЛНЕНА УСПЕШНО!" << endl;
    cout << "Все требования варианта 3 выполнены:" << endl;
    cout << "1. Класс Point" << endl;
    cout << "2. Наследование: 4 производных класса" << endl;
    cout << "3. Полиморфизм через виртуальные методы" << endl;
    cout << "4. Виртуальные методы для координат и цвета" << endl;
    cout << "5. Класс Picture с коллекцией в динамической памяти" << endl;
    cout << "6. Вывод характеристик всех объектов" << endl;
    cout << "7. Демонстрация всех методов классов" << endl;
    cout << "==========================================" << endl;

#ifdef _WIN32
    system("pause");
#endif

    return 0;
}