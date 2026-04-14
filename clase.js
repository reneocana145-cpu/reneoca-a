class Usuario {
    #name;
    #age;
    constructor(nombre, edad) {
        this.#name = nombre;
        this.#age = edad;
    }
     saludar (){
        console.log(`HOLA , MI NOMBRE ES ${this.#name} y tengo ${this.#age} años.`);
     }
     despedir () {
        console.log (`adios, ${this.#name}. ¡hasta luego!`);
     }
   }
const favio = new Usuario( "andre arnez", 20 );
favio.saludar();
favio.despedir();
