#include "ColoredLine.h"
#include <iostream>

ColoredLine::ColoredLine(double x1, double y1, double x2, double y2,
    string color, int thickness)
    : Line(x1, y1, x2, y2, color), thickness(thickness) {
    if (thickness < 1) this->thickness = 1;
}

void ColoredLine::display() const {
    cout << "Цветная линия от (" << x << ", " << y << ") до ("
        << x2 << ", " << y2 << ")";
    cout << ", длина: " << getLength();
    cout << ", цвет: " << color;
    cout << ", толщина: " << thickness;
}

void ColoredLine::setThickness(int thickness) {
    this->thickness = thickness;
    if (this->thickness < 1) this->thickness = 1;
}

int ColoredLine::getThickness() const {
    return thickness;
}