#include "ColoredPoint.h"

ColoredPoint::ColoredPoint(double x, double y, string color, int brightness)
    : Point(x, y, color), brightness(brightness) {
    if (brightness < 0) this->brightness = 0;
    if (brightness > 100) this->brightness = 100;
}

void ColoredPoint::setCoordinates(double x, double y) {
    this->x = x;
    this->y = y;
}

void ColoredPoint::getCoordinates(double& x, double& y) const {
    x = this->x;
    y = this->y;
}

void ColoredPoint::setColor(string color) {
    this->color = color;
    brightness = 50;
}

void ColoredPoint::display() const {
    cout << "÷ветна€ точка в (" << x << ", " << y << ")";
    cout << ", цвет: " << color << ", €ркость: " << brightness << "%";
}

void ColoredPoint::setBrightness(int brightness) {
    this->brightness = brightness;
    if (this->brightness < 0) this->brightness = 0;
    if (this->brightness > 100) this->brightness = 100;
}

int ColoredPoint::getBrightness() const {
    return brightness;
}