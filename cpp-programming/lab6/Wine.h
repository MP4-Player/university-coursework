#ifndef WINE_H
#define WINE_H

#include <string>
#include <iostream>


class Wine {
private:
    static int counter; 

    double alcContent;  
    double density;     
    std::string name;   

    
    Wine();
    Wine(std::string wineName, double alc, double dens);
    ~Wine();

public:
    
    static Wine* createWine(std::string name, double alc, double dens);
    static void destroyWine(Wine* wine);

    
    void age();                 
    void dilute(double ratio);  

    
    double getAlcContent() const;
    double getDensity() const;
    std::string getName() const;

    
    static int getCounter();

    
    friend void printWineInfo(const Wine& w);
};


// Класс с закрытыми конструкторами и методами внутри класса
class SecretWine {
private:
    double secretAlc;
    std::string secretName;

    // Закрытые конструкторы и деструктор
    SecretWine();
    SecretWine(std::string name, double alc);
    ~SecretWine();

public:
    // Методы для создания и уничтожения ВНУТРИ класса
    static SecretWine* createSecret(std::string name, double alc);
    static void destroySecret(SecretWine* wine);

    void display() const;
};


// Класс с закрытыми конструкторами и внешними функциями
class HiddenWine {
private:
    double hiddenAlc;
    std::string hiddenName;

    
    HiddenWine();
    HiddenWine(std::string name, double alc);
    ~HiddenWine();

    friend HiddenWine* createHiddenWine(std::string name, double alc);
    friend void destroyHiddenWine(HiddenWine* wine);
    friend void displayHiddenWine(const HiddenWine* wine);
};


HiddenWine* createHiddenWine(std::string name, double alc);
void destroyHiddenWine(HiddenWine* wine);
void displayHiddenWine(const HiddenWine* wine);

#endif 