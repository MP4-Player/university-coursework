#include "Wine.h"
#include <iostream>

using namespace std;



// Инициализация статического поля
int Wine::counter = 0;

Wine::Wine() : name("Неизвестно"), alcContent(0.0), density(0.0) {
    counter++;
    cout << "Создано вино: " << name << ". Всего объектов Wine: " << counter << endl;
}

Wine::Wine(std::string wineName, double alc, double dens)
    : name(wineName), alcContent(alc), density(dens) {
    counter++;
    cout << "Создано вино: " << name << ". Всего объектов Wine: " << counter << endl;
}

Wine::~Wine() {
    counter--;
    cout << "Уничтожено вино: " << name << ". Осталось объектов Wine: " << counter << endl;
}


Wine* Wine::createWine(std::string name, double alc, double dens) {
    return new Wine(name, alc, dens);
}

void Wine::destroyWine(Wine* wine) {
    delete wine;
}


void Wine::age() {
    alcContent += 0.5;
    cout << name << " выдержано. Новое содержание алкоголя: " << alcContent << "%" << endl;
}


void Wine::dilute(double ratio) {
    alcContent *= (1.0 - ratio);
    density *= (1.0 - ratio);
    cout << name << " разбавлено. Алкоголь: " << alcContent << "%, Плотность: " << density << endl;
}

double Wine::getAlcContent() const { return alcContent; }
double Wine::getDensity() const { return density; }
std::string Wine::getName() const { return name; }


int Wine::getCounter() { return counter; }


void printWineInfo(const Wine& w) {
    cout << "[Дружественная функция] Вино: " << w.name
        << ", Алкоголь: " << w.alcContent
        << "%, Плотность: " << w.density << endl;
}

// SECRETWINE 


SecretWine::SecretWine() : secretName("Секретное"), secretAlc(0.0) {
    cout << "Создан SecretWine: " << secretName << endl;
}


SecretWine::SecretWine(std::string name, double alc)
    : secretName(name), secretAlc(alc) {
    cout << "Создан SecretWine: " << secretName << endl;
}


SecretWine::~SecretWine() {
    cout << "Уничтожен SecretWine: " << secretName << endl;
}


SecretWine* SecretWine::createSecret(std::string name, double alc) {
    return new SecretWine(name, alc);
}


void SecretWine::destroySecret(SecretWine* wine) {
    delete wine;
}

void SecretWine::display() const {
    cout << "SecretWine: " << secretName << ", Алкоголь: " << secretAlc << "%" << endl;
}

// HIDDENWIN


HiddenWine::HiddenWine() : hiddenName("Скрытое"), hiddenAlc(0.0) {
    cout << "Создан HiddenWine: " << hiddenName << endl;
}

HiddenWine::HiddenWine(std::string name, double alc)
    : hiddenName(name), hiddenAlc(alc) {
    cout << "Создан HiddenWine: " << hiddenName << endl;
}


HiddenWine::~HiddenWine() {
    cout << "Уничтожен HiddenWine: " << hiddenName << endl;
}


HiddenWine* createHiddenWine(std::string name, double alc) {
    return new HiddenWine(name, alc);
}


void destroyHiddenWine(HiddenWine* wine) {
    delete wine;
}


void displayHiddenWine(const HiddenWine* wine) {
    cout << "HiddenWine: " << wine->hiddenName << ", Алкоголь: " << wine->hiddenAlc << "%" << endl;
}