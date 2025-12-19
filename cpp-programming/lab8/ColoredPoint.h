#ifndef COLOREDPOINT_H
#define COLOREDPOINT_H

#include "Point.h"

class ColoredPoint : public Point {
private:
    int brightness;

public:
    ColoredPoint(double x = 0, double y = 0, string color = "черный", int brightness = 50);

    void setCoordinates(double x, double y) override;
    void getCoordinates(double& x, double& y) const override;
    void setColor(string color) override;
    void display() const override;

    void setBrightness(int brightness);
    int getBrightness() const;
};

#endif