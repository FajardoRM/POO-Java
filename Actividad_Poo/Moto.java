package Actividad_Poo;

/**
 *Programacion orientada a objetos || NRC: 16362
 * Actividad Nº 1
 * @author Roberto Fajardo
 */
public class Moto extends Vehiculos{

    public Moto(String marca, String modelo, int serie) {
        super(marca, modelo, serie);
    }
    
    public void Contramanillar(){
        System.out.println("Ha efectuado el contramanillar para un giro mas eficiente");
    }    
    
    @Override  
    public String toString(){
        return "Moto: "+" Marca: "+marca+" || Modelo: "+modelo+" || Serie: "+serie;
    }
      
}
