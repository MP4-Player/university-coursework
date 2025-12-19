#ifndef POLYLINE_H
#define POLYLINE_H

#include "Line.h"
#include <vector>
#include <utility>
using namespace std;

class PolyLine : public Line {
private:
    vector<pair<double, double>> vertices;
    bool isClosed;

public:
    PolyLine(const vector<pair<double, double>>& vertices = { {0,0}, {1,0}, {0,1} },
        string color = "черный", bool isClosed = true);

    void setCoordinates(double x, double y) override;
    void getCoordinates(double& x, double& y) const override;
    void display() const override;

    double getArea() const;
    double getPerimeter() const;

    void addVertex(double x, double y);
    int getVertexCount() const;
    bool getIsClosed() const;
};

#endif