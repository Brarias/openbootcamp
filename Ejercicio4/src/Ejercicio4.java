public class Ejercicio4 {
    public static void main(String[] args) {

        // primer punto
        int numeroIf = 0;
        if(numeroIf > 0){
            System.out.println("El número es positivo");
        } else if (numeroIf < 0) {
            System.out.println("El número es negativo");
        }else {
            System.out.println("El número es 0");
        }

        // segundo punto
        int numeroWhile = 0;

        while(numeroWhile < 3){
            System.out.println("numeroWhile es: "+numeroWhile);
            numeroWhile++;
        }

        // punto 3
        int numeroDoWhile = 4;

        do {
            System.out.println("numeroDoWhile es: "+numeroDoWhile);
            numeroDoWhile++;
        }while (numeroDoWhile < 3);

        // punto 4
        for(int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println("numeroFor es: "+numeroFor);
        }

        // punto 5

        String estacion = "invierno";
        switch (estacion){
            case "verano" :
                System.out.println("la estación es: VERANO");
                break;
            case "invierno" :
                System.out.println("la estación es: INVIERNO");
                break;
            case "primavera" :
                System.out.println("la estación es: PRIMAVERA");
                break;
            case "otoño" :
                System.out.println("la estación es: OTOÑO");
                break;
        }

    }

}
