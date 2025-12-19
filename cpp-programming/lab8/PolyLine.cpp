#include "PolyLine.h"
#include <cmath>
#include <iostream>

PolyLine::PolyLine(const vector<pair<double, double>>& vertices,
    string color, bool isClosed)
    : Line(vertices.empty() ? 0 : vertices[0].first,
        vertices.empty() ? 0 : vertices[0].second,
        0, 0, color),
    vertices(vertices), isClosed(isClosed) {
}

void PolyLine::setCoordinates(double x, double y) {
    if (!vertices.empty()) {
        vertices[0] = make_pair(x, y);
        this->x = x;
        this->y = y;
    }
}

void PolyLine::getCoordinates(double& x, double& y) const {
    if (!vertices.empty()) {
        x = vertices[0].first;
        y = vertices[0].second;
    }
    else {
        x = this->x;
        y = this->y;
    }
}

double PolyLine::getArea() const {
    if (!isClosed || vertices.size() < 3) return 0;

    double area = 0;
    int n = vertices.size();

    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        area += vertices[i].first * vertices[j].second;
        area -= vertices[j].first * vertices[i].second;
    }

    return fabs(area) / 2.0;
}

double PolyLine::getPerimeter() const {
    if (vertices.size() < 2) return 0;

    double perimeter = 0;
    int n = vertices.size();

    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        if (!isClosed && i == n - 1) break;

        double dx = vertices[j].first - vertices[i].first;
        double dy = vertices[j].second - vertices[i].second;
        perimeter += sqrt(dx * dx + dy * dy);
    }

    return perimeter;
}

void PolyLine::display() const {
    cout << "Многоугольник с " << vertices.size() << " вершинами";
    cout << ", цвет: " << color;
    cout << ", " << (isClosed ? "замкнутый" : "незамкнутый");
    cout << ", площадь: " << getArea();
    cout << ", периметр: " << getPerimeter();
}

void PolyLine::addVertex(double x, double y) {
    vertices.push_back(make_pair(x, y));
}

int PolyLine::getVertexCount() const {
    return vertices.size();
}

bool PolyLine::getIsClosed() const {
    return isClosed;
}