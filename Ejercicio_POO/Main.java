package Ejercicio_POO;

/**
 *
 * @author m64wr
 */
public class Main {

    public static void main(String[] args) {
        Persona p1 = new Persona("Jose", "Gonzales", 20);
        p1.setCedula("12849478");
        System.out.println(p1);
        System.out.println("Numero cedula: " + p1.getId());
    }
}
