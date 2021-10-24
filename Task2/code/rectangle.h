#ifndef __rectangle__
#define __rectangle__

//------------------------------------------------------------------------------
// rectangle.h - содержит описание прямоугольника  и его интерфейса
//------------------------------------------------------------------------------

#include <fstream>
# include "rnd.h"
#include "shape.h"

// прямоугольник
class rectangle : public shape {
public:
    int x1, y1, x2, y2; //Координаты противоположных углов
// Ввод параметров прямоугольника из файла
    virtual void In(std::ifstream &ifst);

// Случайный ввод параметров прямоугольника
    virtual shape* InRnd();

// Вывод параметров прямоугольника в форматируемый поток
    virtual void Out(std::ofstream &ofst);

// Вычисление площади прямоугольника
    virtual double Square();
};

#endif //__rectangle__
