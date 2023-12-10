
package Ejercicio_POO;

/**
 *
 * @author m64wr
 */
public class Persona {
    public String nombre, apellido;
    public Integer edad;
    private String id;

    public Persona(String nombre,String apellido ,Integer edad){
        this.nombre = nombre;
        this.apellido = apellido; 
        this.edad = edad;
    }
    
    public String getId() {
        return id;
    }

    public void setCedula(String id) {
        this.id = id;
    }
    
    @Override
    public String toString(){
        return "Nombre: "+nombre+" Apellido: "+apellido+" Edad: "+edad;
    }
}
