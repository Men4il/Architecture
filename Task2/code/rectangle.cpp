//------------------------------------------------------------------------------
// rectangle_In.cpp - содержит процедуру ввода параметров 
// для уже созданного прямоугольника
//------------------------------------------------------------------------------

#include "rectangle.h"
#include "rnd.h"

//------------------------------------------------------------------------------
// Ввод параметров прямоугольника из файла
void rectangle::In(std::ifstream &ifst) {
    ifst >> this->x1 >> this->y1 >> this->x2 >> this->y2;
}

// Случайный ввод параметров прямоугольника
shape* rectangle::InRnd() {
    this->x1 = Random();
    this->y1 = Random();
    this->x2 = Random();
    this->y2 = Random();

    return this;
}

//------------------------------------------------------------------------------
// Вывод параметров прямоугольника в форматируемый поток
void rectangle::Out(std::ofstream &ofst) {
    ofst << "It is Rectangle: left top angle(x,y) = ("
    << this->x1 << ", " << this->y1 << "), right bot angle(x,y) = ("
    << this->x2 << ", " << this->y2 << "). Square = "
    << this->Square() << "\n";
}

//------------------------------------------------------------------------------
// Вычисление площади прямоугольника
double rectangle::Square() {
    double temp_a, temp_b;

    temp_a = this->x1 > this->x2 ? this->x1 - this->x2 : this->x2 - this->x1;
    temp_b = this->y1 > this->y2 ? this->y1 - this->y2 : this->y2 - this->y1;

    return temp_a * temp_b;
}
