//------------------------------------------------------------------------------
// shape.cpp - содержит процедуры связанные с обработкой обобщенной фигуры
// и создания произвольной фигуры
//------------------------------------------------------------------------------

#include "shape.h"
#include "circle.h"
#include "triangle.h"
#include "rectangle.h"
#include "rnd.h"

//------------------------------------------------------------------------------
// Ввод параметров обобщенной фигуры из файла
shape* shape::In(std::ifstream &ifst) {
    int k;
    ifst >> k;
    shape* sp;
    switch(k) {
        case 1:
            dynamic_cast<circle*>(sp)->In(ifst);
            return sp;
        case 2:
            dynamic_cast<rectangle*>(sp)->In(ifst);
            return sp;
        case 3:
            dynamic_cast<triangle*>(sp)->In(ifst);
            return sp;

        default:
            return 0;
    }
}

// Случайный ввод обобщенной фигуры
shape* shape::InRnd() {
    shape *sp;
    auto k = rand() % 3 + 1;
    switch(k) {
        case 1:
            dynamic_cast<circle*>(sp)->InRnd();
            return sp;
        case 2:
            dynamic_cast<rectangle*>(sp)->InRnd();
            return sp;
        case 3:
            dynamic_cast<triangle*>(sp)->InRnd();
            return sp;

        default:
            return 0;
    }
}

//------------------------------------------------------------------------------
// Вывод параметров текущей фигуры в поток
void shape::Out(std::ofstream &ofst) {
    if(dynamic_cast<rectangle*>(this) != nullptr) {
        dynamic_cast<rectangle*>(this)->Out(ofst);
    } else if (dynamic_cast<triangle*>(this) != nullptr) {
        dynamic_cast<triangle*>(this)->Out(ofst);
    } else if (dynamic_cast<circle*>(this) != nullptr) {
        dynamic_cast<circle*>(this)->Out(ofst);
    } else {
        ofst << "Incorrect figure!\n";
    }
}

//------------------------------------------------------------------------------
// Вычисление площади фигуры
double shape::Square() {
    if (dynamic_cast<rectangle*>(this) != nullptr) {
        return dynamic_cast<rectangle*>(this)->Square();
    } else if (dynamic_cast<triangle*>(this) != nullptr) {
        return dynamic_cast<triangle*>(this)->Square();
    } else if (dynamic_cast<circle*>(this) != nullptr) {
        return dynamic_cast<circle*>(this)->Square();
    } else {
        return 0.0;
    }
}
