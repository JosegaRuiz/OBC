public class Parte1 {
    public static void main(String[] args){
        // Definicion de variables para introducir a la función
        int valor1 = 3;
        int valor2 = 5;
        int valor3 = 8;
        int resultado;

        // Llamada a la función
        resultado = suma(valor1, valor2, valor3);

        // Muestreo de resultado obtenido
        System.out.println(resultado);
    }

    // Definicion de la funcion
    public static int suma(int a, int b, int c){
        return a + b + c;
    }
}
