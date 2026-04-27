#ifndef PERSONAJE_H
#define PERSONAJE_H
#include <vector>
#include <memory>
#include "EfectoDeEstado.h"

class Personaje {
protected: // Encapsulamiento
    std::string nombre;
    int salud;
    std::vector<std::unique_ptr<EfectoDeEstado>> estados; // Gestión de ciclo de vida

public:
    Personaje(std::string n, int s) : nombre(n), salud(s) {}
    virtual ~Personaje() {}

    virtual void atacar(Personaje& objetivo) = 0; // Polimorfismo
    virtual void usarHabilidad() = 0;

    void añadirEstado(std::unique_ptr<EfectoDeEstado> nuevoEstado) {
        estados.push_back(std::move(nuevoEstado));
    }

    void procesarTurno() {
        for (auto it = estados.begin(); it != estados.end();) {
            (*it)->aplicarEfecto();
            (*it)->reducirDuracion();
            if (!(*it)->estaActivo()) it = estados.erase(it);
            else ++it;
        }
    }
    
    std::string getNombre() { return nombre; }
};
#endif