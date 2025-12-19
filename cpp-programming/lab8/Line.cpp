#include "Line.h"
#include <cmath>
#include <iostream>

Line::Line(double x1, double y1, double x2, double y2, string color)
    : Point(x1, y1, color), x2(x2), y2(y2) {
}

void Line::setCoordinates(double x, double y) {
    this->x = x;
    this->y = y;
}

void Line::getCoordinates(double& x, double& y) const {
    x = this->x;
    y = this->y;
}

void Line::setEndPoint(double x2, double y2) {
    this->x2 = x2;
    this->y2 = y2;
}

double Line::getLength() const {
    return sqrt((x2 - x) * (x2 - x) + (y2 - y) * (y2 - y));
}

void Line::display() const {
    cout << "Линия от (" << x << ", " << y << ") до ("
        << x2 << ", " << y2 << ")";
    cout << ", длина: " << getLength();
    cout << ", цвет: " << color;
}