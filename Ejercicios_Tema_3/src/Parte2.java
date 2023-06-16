public class Parte2 {

    public static void main(String[] args){
        // Creacion de objeto
        Coche miCoche = new Coche();
        // Se añade una puerta
        miCoche.AnadirPuertas(1);
        // Se muestra el numero actual de puertas del objeto
        System.out.println("El coche tiene: " + miCoche.puertas + " puerta/s");
    }
}


// Definicion de la clase Coche
class Coche {
    // Definicion del numero de puertas inicial con el que se creara el objeto por defecto
    public int puertas = 0;

    // Metodo para añadir un numero de puertas determinado al objeto coche
    public void AnadirPuertas(int numPuertas) {
        this.puertas += numPuertas;
    }
}