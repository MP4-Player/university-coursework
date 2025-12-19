#include "Picture.h"
#include "ColoredPoint.h"
#include "Line.h"
#include "ColoredLine.h"
#include "PolyLine.h"
#include <iostream>

Picture::Picture() {}

Picture::~Picture() {
    clear();
}

void Picture::addShape(Point* shape) {
    if (shape != nullptr) {
        shapes.push_back(shape);
    }
}

void Picture::addPoint(double x, double y, string color) {
    shapes.push_back(new ColoredPoint(x, y, color, 50));
}

void Picture::addColoredPoint(double x, double y, string color, int brightness) {
    shapes.push_back(new ColoredPoint(x, y, color, brightness));
}

void Picture::addLine(double x1, double y1, double x2, double y2, string color) {
    shapes.push_back(new Line(x1, y1, x2, y2, color));
}

void Picture::addColoredLine(double x1, double y1, double x2, double y2,
    string color, int thickness) {
    shapes.push_back(new ColoredLine(x1, y1, x2, y2, color, thickness));
}

void Picture::addPolyLine(const vector<pair<double, double>>& vertices,
    string color, bool isClosed) {
    shapes.push_back(new PolyLine(vertices, color, isClosed));
}

void Picture::displayAll() const {
    cout << "\n=== ÂÑÅ ÔÈÃÓÐÛ Â ÊÀÐÒÈÍÅ (" << shapes.size() << " øò.) ===" << endl;
    for (size_t i = 0; i < shapes.size(); i++) {
        cout << i + 1 << ". ";
        shapes[i]->display();
        cout << endl;
    }
    cout << "============================================" << endl;
}

int Picture::getCount() const {
    return static_cast<int>(shapes.size());
}

void Picture::clear() {
    for (size_t i = 0; i < shapes.size(); i++) {
        delete shapes[i];
    }
    shapes.clear();
}

void Picture::showPolymorphism() const {
    cout << "\n=== ÄÅÌÎÍÑÒÐÀÖÈß ÏÎËÈÌÎÐÔÈÇÌÀ ===" << endl;
    cout << "Âñå ôèãóðû èìåþò ìåòîä display(), íî âûâîä ðàçíûé:" << endl;

    for (size_t i = 0; i < shapes.size(); i++) {
        cout << "Ôèãóðà " << i + 1 << " -> ";
        shapes[i]->display();
        cout << endl;
    }
}