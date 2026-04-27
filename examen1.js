class CuentaBancaria {
  // Atributos privados
  #numeroCuenta;
  #saldo;

  constructor(numeroCuenta, saldoInicial) {
    this.#numeroCuenta = numeroCuenta;
    
    this.#saldo = saldoInicial >= 0 ? saldoInicial : 0;
  }

  
  depositar(monto) {
    if (monto > 0) {
      this.#saldo += monto;
      console.log(`Depósito exitoso de $${monto}. Nuevo saldo: $${this.#saldo}`);
    } else {
      console.log("El monto a depositar debe ser mayor a cero.");
    }
  }

  
  retirar(monto) {
    if (monto <= 0) {
      console.log("El monto a retirar debe ser mayor a cero.");
    } else if (monto > this.#saldo) {
      console.log(`Fondos insuficientes. Intento de retiro: $${monto} | Saldo disponible: $${this.#saldo}`);
    } else {
      this.#saldo -= monto;
      console.log(`Retiro exitoso de $${monto}. Saldo restante: $${this.#saldo}`);
    }
  }

  
  mostrarSaldo() {
    console.log(`Cuenta: ${this.#numeroCuenta} | Saldo actual: $${this.#saldo}`);
    return this.#saldo;
  }
}

// --- Ejemplo de uso ---

const miCuenta = new CuentaBancaria("BCP-0634", 2000);

miCuenta.mostrarSaldo();     
miCuenta.depositar(200);     
miCuenta.retirar(1000);      
miCuenta.retirar(300);        
miCuenta.mostrarSaldo();      

