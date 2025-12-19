#ifndef POINT_H
#define POINT_H

#include <iostream>
#include <string>
using namespace std;

// Класс Point (точка)
class Point {
protected:
    double x, y;
    string color;

public:
    Point(double x = 0, double y = 0, string color = "черный");
    virtual ~Point() {}

    // Виртуальные методы
    virtual void setCoordinates(double x, double y);
    virtual void getCoordinates(double& x, double& y) const;
    virtual void setColor(string color);
    virtual string getColor() const;
    virtual void display() const;
};

#endif