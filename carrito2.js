class vehiculo {
    #placa

    constructor(marca, placa) {
        this.marca = marca;
        this.#placa = placa;
    }
    arrancar() {
        console.log(`El vehículo ${this.marca} con placa ${this.#placa} ha arrancado.`);
    }
}

class auto extends vehiculo {
    constructor(marca,placa, modelo) {
        super(marca, placa);
        this.modelo = modelo;
    }
    TocarBocina() {
        console.log(`beep beep ${this.marca} ${this.modelo} esta saludandno.`);
    }   
}

class AutoElectrico extends auto {
    constructor(marca, placa, modelo, bateria) {
        super(marca, placa, modelo);
        this.bateria = bateria;
    }
    cargar() {
        console.log(`El auto ${this.marca} ${this.modelo} se esta cargando  ${this.bateria} %.`);
    }
    arrancar() {
        super.arrancar();
        console.log(`El auto electrico ${this.marca} ${this.modelo} esta arrancando silenciosamente.`);
    }
}   

const Milamborghini = new AutoElectrico("Lamborghini", "346MDV74 35", "elegante", 30);

Milamborghini.arrancar();
Milamborghini.TocarBocina();
Milamborghini.cargar();