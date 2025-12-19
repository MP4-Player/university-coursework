#include "Point.h"

Point::Point(double x, double y, string color)
    : x(x), y(y), color(color) {
}

void Point::setCoordinates(double x, double y) {
    this->x = x;
    this->y = y;
}

void Point::getCoordinates(double& x, double& y) const {
    x = this->x;
    y = this->y;
}

void Point::setColor(string color) {
    this->color = color;
}

string Point::getColor() const {
    return color;
}

void Point::display() const {
    cout << "Точка в (" << x << ", " << y << "), цвет: " << color;
}