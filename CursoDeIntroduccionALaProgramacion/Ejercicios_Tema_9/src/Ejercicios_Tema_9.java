public class Ejercicios_Tema_9 {
    public static class Persona {
        private int edad;
        private String nombre;
        private String telefono;

        public int getEdad() {
            return edad;
        }

        public void setEdad(int edad) {
            this.edad = edad;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getTelefono() {
            return telefono;
        }

        public void setTelefono(String telefono) {
            this.telefono = telefono;
        }
    }

    public static class Cliente extends Persona {
        private double credito;

        public double getCredito() {
            return credito;
        }

        public void setCredito(double credito) {
            this.credito = credito;
        }
    }

    public static class Trabajador extends Persona {
        private double salario;

        public double getSalario() {
            return salario;
        }

        public void setSalario(double salario) {
            this.salario = salario;
        }
    }

    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setEdad(30);
        cliente.setNombre("Juan");
        cliente.setTelefono("123456789");
        cliente.setCredito(5000.0);
        System.out.println("Cliente:");
        System.out.println("Edad: " + cliente.getEdad());
        System.out.println("Nombre: " + cliente.getNombre());
        System.out.println("Teléfono: " + cliente.getTelefono());
        System.out.println("Crédito: " + cliente.getCredito());

        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(25);
        trabajador.setNombre("María");
        trabajador.setTelefono("987654321");
        trabajador.setSalario(2500.0);
        System.out.println("\nTrabajador:");
        System.out.println("Edad: " + trabajador.getEdad());
        System.out.println("Nombre: " + trabajador.getNombre());
        System.out.println("Teléfono: " + trabajador.getTelefono());
        System.out.println("Salario: " + trabajador.getSalario());
    }

}
