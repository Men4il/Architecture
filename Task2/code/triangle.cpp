//------------------------------------------------------------------------------
// triangle.cpp - содержит функции обработки треугольника
//------------------------------------------------------------------------------

#include "triangle.h"
#include "rnd.h"

//------------------------------------------------------------------------------
// Ввод параметров треугольника из потока
void triangle::In(std::ifstream &ifst) {
    ifst >> this->x1 >> this->y1 >> this->x2 >> this->y2 >> this->x3 >> this->y3;
}

// Случайный ввод параметров треугольника
shape* triangle::InRnd() {
    this->x1 = Random();
    this->y1 = Random();
    this->x2 = Random();
    this->y2 = Random();
    this->x3 = Random();
    this->y3 = Random();

    return this;
}

//------------------------------------------------------------------------------
// Вывод параметров треугольника в поток
void triangle::Out(std::ofstream &ofst) {
    ofst << "It is Triangle: first angle(x,y) = ("
         << this->x1 << this->y1 << "), second angle(x,y) = "
         << this->x2 << this->y2 << "), third angle(x,y) = "
         << this->x3 << this->y3 << "). Square = "
         << this->Square() << "\n";
}

//------------------------------------------------------------------------------
// Вычисление площади треугольника
double triangle::Square() {
    double temp = (this->x2 - this->x1) * (this->y3 - this->y1) - (this->x3 - this->x1) * (this->y2 - this->y1);
    if (temp < 0) temp *= -1;

    return temp / 2;
}
