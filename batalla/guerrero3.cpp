#ifndef GUERRERO_H
#define GUERRERO_H
#include "Personaje.h"

class Guerrero : public Personaje {
public:
    Guerrero(std::string n) : Personaje(n, 150) {}
    
    void atacar(Personaje& objetivo) override {
        std::cout << nombre << " lanza un tajo de espada a " << objetivo.getNombre() << "!\n";
    }
    
    void usarHabilidad() override {
        std::cout << nombre << " usa 'Grito de Guerra' (Aumenta defensa).\n";
    }
};
#endif