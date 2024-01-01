package Activida_POO_2;

/**
 *
 * @author Roberto Fajardo
 */

public class Pinguino extends Zoo {
    private static int contadorPinguino = 0;

    public Pinguino(String nombre, int edad) {
        super(nombre, edad);
        contadorPinguino++;
    }
    
    public static int getContadorPinguino(){
        return contadorPinguino;
    }
    
    @Override
    public String toString(){
        return super.toString();
    }

}
