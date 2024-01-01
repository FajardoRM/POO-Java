package Activida_POO_2;

/**
 *
 * @author Robeto Fajardo
 */

public abstract class Zoo {
    public String nombre;
    public int edad;
    private Integer nRegistro;

    public Zoo(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public Integer getNRegistro() {
        return nRegistro;
    }

    public void SetNRegistro(Integer nRegistro) {
        this.nRegistro = nRegistro;
    }
    
    public String toString(){
        return "Nombre: "+nombre+" || Edad: "+edad;
    }

}
