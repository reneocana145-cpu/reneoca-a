

// Clase que representa un nodo de la lista
class Nodo {
    int dato;
    Nodo siguiente;
    Nodo anterior;

    public Nodo(int dato) {
        this.dato = dato;
        this.siguiente = null;
        this.anterior = null;
    }
}

// Clase que gestiona la estructura de la lista circular doblemente enlazada
class ListaCircularDoble {
    private Nodo cabeza = null;
    private Nodo cola = null;

    // Método para insertar un elemento al final de la lista
    public void insertar(int dato) {
        Nodo nuevo = new Nodo(dato);

        if (cabeza == null) {
            cabeza = nuevo;
            cola = nuevo;
            // Al ser circular, se apuntan a sí mismos
            cabeza.siguiente = cabeza;
            cabeza.anterior = cabeza;
            System.out.println("Insertado primer nodo: " + dato);
        } else {
            // El nuevo nodo se coloca después de la cola actual
            cola.siguiente = nuevo;
            nuevo.anterior = cola;
            // Se cierra el círculo con la cabeza
            nuevo.siguiente = cabeza;
            cabeza.anterior = nuevo;
            // La nueva cola es el nuevo nodo
            cola = nuevo;
            System.out.println("Insertado nodo: " + dato);
        }
    }

    // Método para recorrer la lista hacia adelante
    public void mostrarHaciaAdelante() {
        if (cabeza == null) {
            System.out.println("La lista está vacía.");
            return;
        }
        Nodo actual = cabeza;
        System.out.print("Recorrido horario: ");
        do {
            System.out.print("[" + actual.dato + "] <-> ");
            actual = actual.siguiente;
        } while (actual != cabeza);
        System.out.println("(Vuelve al inicio)");
    }

    // Método para recorrer la lista hacia atrás
    public void mostrarHaciaAtras() {
        if (cola == null) return;
        Nodo actual = cola;
        System.out.print("Recorrido anti-horario: ");
        do {
            System.out.print("[" + actual.dato + "] <-> ");
            actual = actual.anterior;
        } while (actual != cola);
        System.out.println("(Vuelve al final)");
    }

    // Método para eliminar un nodo por su valor
    public void eliminar(int valor) {
        if (cabeza == null) return;

        Nodo actual = cabeza;
        boolean encontrado = false;

        do {
            if (actual.dato == valor) {
                encontrado = true;
                if (actual == cabeza && actual == cola) {
                    // Caso: Solo hay un nodo
                    cabeza = null;
                    cola = null;
                } else {
                    // Re-enlazamos los vecinos
                    actual.anterior.siguiente = actual.siguiente;
                    actual.siguiente.anterior = actual.anterior;
                    
                    // Si eliminamos la cabeza o la cola, actualizamos las referencias
                    if (actual == cabeza) cabeza = actual.siguiente;
                    if (actual == cola) cola = actual.anterior;
                }
                System.out.println("Nodo " + valor + " eliminado.");
                break;
            }
            actual = actual.siguiente;
        } while (actual != cabeza);

        if (!encontrado) System.out.println("Valor " + valor + " no encontrado.");
    }
}

// Clase principal para ejecutar el programa
public class Main {
    public static void main(String[] args) {
        ListaCircularDoble lista = new ListaCircularDoble();

        // 1. Insertar datos
        lista.insertar(10);
        lista.insertar(20);
        lista.insertar(30);
        lista.insertar(40);

        // 2. Mostrar la lista en ambos sentidos
        System.out.println("\n--- Estado de la Lista ---");
        lista.mostrarHaciaAdelante();
        lista.mostrarHaciaAtras();

        // 3. Eliminar un nodo intermedio
        System.out.println("\n--- Eliminación ---");
        lista.eliminar(20);
        lista.mostrarHaciaAdelante();

        // 4. Eliminar la cabeza
        lista.eliminar(10);
        lista.mostrarHaciaAdelante();
        
        System.out.println("\nPrueba finalizada con éxito.");
    }
}



