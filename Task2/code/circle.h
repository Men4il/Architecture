#ifndef __circle__
#define __circle__

//------------------------------------------------------------------------------
// circle.h - содержит описание круга
//------------------------------------------------------------------------------

#include <fstream>
# include "rnd.h"
#include "shape.h"

//------------------------------------------------------------------------------
// круг
class circle : public shape {
public:
    int x, y, r; // Координаты центра и радиус

// Ввод параметров круга из файла
    virtual void In(std::ifstream &ifst);

// Случайный ввод параметров круга
    virtual shape* InRnd();

// Вывод параметров круга в форматируемый поток
    virtual void Out(std::ofstream &ofst);

// Вычисление площади круга
    virtual double Square();
};

#endif //__circle__
