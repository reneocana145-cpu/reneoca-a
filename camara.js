class camara {
    tomarFoto () {
        console.log("toma una foto setsi")
    }
}
class grabadora {
    grabarAudio () {
        console.log("graba un audio sabroso")
    }
}


class smartphone extends camara {
    constructor(numero, celular) {
        super();
        this.numero = numero;
        this.celular = celular;
        this.grabadora = new grabadora();
    }
    hacerLlamada() {
        console.log(`llama a ${this.numero} esta llamando a  ${this.celular}`);
    }
    grabarAudio() {
        this.grabadora.grabarAudio();
    }
}

const miSmartphone = new smartphone("123456789", "mi amigo");
miSmartphone.hacerLlamada();
miSmartphone.tomarFoto();
miSmartphone.grabarAudio();
