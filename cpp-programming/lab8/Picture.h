#ifndef PICTURE_H
#define PICTURE_H

#include <vector>
#include <string>
#include <utility>
using namespace std;

// Только объявления, чтобы избежать циклических зависимостей
class Point;

class Picture {
private:
    vector<Point*> shapes;

public:
    Picture();
    ~Picture();

    void addShape(Point* shape);
    void addPoint(double x, double y, string color = "черный");
    void addColoredPoint(double x, double y, string color = "красный", int brightness = 50);
    void addLine(double x1, double y1, double x2, double y2, string color = "синий");
    void addColoredLine(double x1, double y1, double x2, double y2,
        string color = "зеленый", int thickness = 1);
    void addPolyLine(const vector<pair<double, double>>& vertices,
        string color = "фиолетовый", bool isClosed = true);

    void displayAll() const;
    int getCount() const;
    void clear();
    void showPolymorphism() const;
};

#endif