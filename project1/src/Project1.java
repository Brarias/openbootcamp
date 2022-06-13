public class Project1 {
    public static void main(String[] args) {
        int resultado = suma(10,20,30);
        System.out.println(resultado);

        Coche miCoche = new Coche();
        miCoche.numeroPuertas = 4;
        miCoche.incrementarPuerta();
        System.out.println(miCoche.numeroPuertas);
    }

    public static int suma(int a, int b, int c){
        return a+b+c;
    }
}
