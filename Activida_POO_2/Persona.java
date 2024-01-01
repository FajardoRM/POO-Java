package Activida_POO_2;

/**
 *
 * @author Roberto Fajardo
 */

public abstract class Persona {
    public String nombre;
    public int edad;
    private Integer cedula;
    
    public Persona(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;    
    }
    
    public Integer getCedula(){
        return cedula;
    }
    
    public void SetNombre(Integer cedula){
        this.cedula = cedula;
    }
     
    public String toString(){
        return "Nombre: "+ nombre+" || Edad: "+edad;
    }
    
}
