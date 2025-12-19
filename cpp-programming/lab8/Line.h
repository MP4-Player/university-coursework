#ifndef LINE_H
#define LINE_H

#include "Point.h"

class Line : public Point {
protected:
    double x2, y2;

public:
    Line(double x1 = 0, double y1 = 0, double x2 = 1, double y2 = 1, string color = "черный");

    void setCoordinates(double x, double y) override;
    void getCoordinates(double& x, double& y) const override;
    void setEndPoint(double x2, double y2);
    void display() const override;

    double getLength() const;
};

#endif