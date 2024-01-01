package Activida_POO_2;

/**
 *
 * @author Roberto Fajardo
 */

public class Leon extends Zoo {
    private static int contadorLeon = 0;
    public Leon(String nombre, int edad) {
        super(nombre, edad);
        contadorLeon++;
    }
    
    public static int getContadorLeon(){
        return contadorLeon;
    }
    
    @Override
    public String toString(){
        return super.toString();
    }

        
}
