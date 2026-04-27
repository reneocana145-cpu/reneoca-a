#ifndef EFECTODESTADO_H
#define EFECTODESTADO_H
#include <string>
#include <iostream>

// Clase abstracta para estados
class EfectoDeEstado {
protected:
    std::string nombre;
    int duracion;
public:
    EfectoDeEstado(std::string n, int d) : nombre(n), duracion(d) {}
    virtual ~EfectoDeEstado() { std::cout << "Efecto " << nombre << " eliminado.\n"; }
    
    virtual void aplicarEfecto() = 0; // Abstracción
    bool estaActivo() const { return duracion > 0; }
    void reducirDuracion() { duracion--; }
    std::string getNombre() { return nombre; }
};

class Veneno : public EfectoDeEstado {
public:
    Veneno() : EfectoDeEstado("Veneno", 3) {}
    void aplicarEfecto() override { std::cout << "-> Daño por veneno aplicado.\n"; }
};
#endif