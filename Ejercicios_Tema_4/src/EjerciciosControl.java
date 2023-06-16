public class EjerciciosControl {

    public static void main(String[] args) {

        // Ejercicio if
        int numeroIf = 5;
        if (numeroIf > 0) {
            System.out.println("El número es positivo.");
        } else if (numeroIf < 0) {
            System.out.println("El número es negativo.");
        } else {
            System.out.println("El número es cero.");
        }

        // Ejercicio While
        int numeroWhile = 0;
        while (numeroWhile < 3) {
            numeroWhile++;
            System.out.println("Valor de numeroWhile: " + numeroWhile);
        }

        // Ejercicio Do While
        int numeroDoWhile = 0;
        do {
            numeroDoWhile++;
            System.out.println("Valor de numeroDoWhile: " + numeroDoWhile);
        } while (numeroDoWhile < 3);

        // Ejercicio For
        for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println("Valor de numeroFor: " + numeroFor);
        }

        // Ejercicio Switch
        String estacion = "primavera";
        switch (estacion) {
            case "primavera":
                System.out.println("Es primavera.");
                break;
            case "verano":
                System.out.println("Es verano.");
                break;
            case "otoño":
                System.out.println("Es otoño.");
                break;
            case "invierno":
                System.out.println("Es invierno.");
                break;
            default:
                System.out.println("No es una estación válida.");
                break;
        }
    }
}
