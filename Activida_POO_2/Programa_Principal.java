package Activida_POO_2;

import java.util.Scanner;

/**
 * @author Roberto Fajardo
 */
public class Programa_Principal {
    
        public static boolean validarEdad(int edad){
        return edad > 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        boolean salir = false;
        int opc;

        do {
            menuPrincipal();
            try {
                opc = sc.nextInt();
                switch (opc) {
                    case 1:
                        instanciarVisitante(sc);
                        break;
                    case 2:
                        instanciarCuidador(sc);
                        break;
                    case 3:
                        instanciarLeon(sc);
                        break;
                    case 4: 
                        instanciarPinguino(sc);
                        break;
                    case 5:
                        salir = true;
                        break;
                    default:
                        System.out.println("Debe ser 1 y 4");
                        break;
                }
            } catch (Exception e) {
                System.out.println("Debe ingresar un numero");
                sc.nextLine();
                opc = 0;
            }

        } while (!salir);
        sc.close();

    }

    public static void menuPrincipal() {
        System.out.print("\t**Menu Principal**\n"
                + "1. Para instanciar visitante\n"
                + "2. Para instanciar cuidador\n"
                + "3. Para instanciar Leon\n"
                + "4. Para instanciar Pingunino\n"
                + "5. Para salir\n"
                + "Seleccione una opcion: ");
    }

    public static void instanciarVisitante(Scanner sc) {
        System.out.print("Ingrese un nombre: ");
        String nombre = sc.next();
        System.out.print("Ingrese la edad: ");
        int edad = obtenerEdad(sc);
        if (validarEdad(edad)) {
            System.out.println("Puede continuar.");
        } else {
            System.out.println("No puedes continuar.");
        }
        System.out.print("Ingrese su carnet: ");
        int carnet = sc.nextInt();
        Visitante visitante = new Visitante(nombre, edad, carnet);
        System.out.println("VISITANTE --> " +visitante.toString());
    }

    public static void instanciarCuidador(Scanner sc) {
        int edad;
        System.out.print("Ingrese un nombre: ");
        String nombre = sc.next();
        do {
            System.out.println("Ingrese su edad: ");
            edad = sc.nextInt();
        } while (edad < 18);
        System.out.print("Ingrese el numero de id: ");
        int identificacion = sc.nextInt();
        Cuidador cuidador = new Cuidador(nombre, edad, identificacion);
        System.out.println("CUIDADOR --> " +cuidador.toString());
    }

    public static void instanciarLeon(Scanner sc) {
        System.out.print("Ingrese un nombre: ");
        String nombre = sc.next();
        System.out.print("Ingrese la edad: ");
        int edad = sc.nextInt();
        Leon leon = new Leon(nombre, edad);
        System.out.println("LEON --> " + leon.toString()+ " || Nº INSTANCIA: " + Leon.getContadorLeon());
    }

    public static void instanciarPinguino(Scanner sc) {
        System.out.print("Ingrese un nombre: ");
        String nombre = sc.next();
        System.out.print("Ingrese la edad: ");
        int edad = sc.nextInt();
        Pinguino pinguino = new Pinguino(nombre, edad);
        System.out.println("PINGUINO --> " + pinguino.toString()+ " || Nº INSTANCIA: " + Pinguino.getContadorPinguino());
    }
    
        private static int obtenerEdad(Scanner sc) {
        int edad = 0;
        boolean entradaValida = false;

        do {
            try {
                edad = sc.nextInt();
                sc.nextLine();
                entradaValida = true;
            } catch (java.util.InputMismatchException e) {
                System.out.println("ERROR: Debes ingresar un número.");
                sc.nextLine();
                System.out.print("Vuelve a ingresar su edad: ");
            }
        } while (!entradaValida);

        return edad;
    }
}
