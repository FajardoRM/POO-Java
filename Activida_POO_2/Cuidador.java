package Activida_POO_2;

/**
 *
 * @author Roberto Fajardo
 */
public class Cuidador extends Persona {

    public Integer id;

    public Cuidador(String nombre, int edad, Integer id) {
        super(nombre, edad);
        this.id = id;
    }
    
    @Override
    public String toString(){
        return super.toString()+" || Id: "+id;
    }

}
