package Activida_POO_2;

/**
 *
 * @author m64wr
 */
public class Visitante extends Persona {
    public Integer carnet;

    public Visitante(String nombre, int edad, Integer carnet) {
        super(nombre, edad);        
        this.carnet = carnet;
    }
    
    @Override
    public String toString(){
        return super.toString()+" || Carnet: "+carnet;
    }
       
}
