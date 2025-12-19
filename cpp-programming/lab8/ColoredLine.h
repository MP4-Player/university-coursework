#ifndef COLOREDLINE_H
#define COLOREDLINE_H

#include "Line.h"

class ColoredLine : public Line {
private:
    int thickness;

public:
    ColoredLine(double x1 = 0, double y1 = 0, double x2 = 1, double y2 = 1,
        string color = "черный", int thickness = 1);

    void display() const override;
    void setThickness(int thickness);
    int getThickness() const;
};

#endif