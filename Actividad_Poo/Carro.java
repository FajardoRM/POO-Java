package Actividad_Poo;

/**
 *Programacion orientada a objetos || NRC: 16362
 * Actividad Nº 1
 * @author Roberto Fajardo
 */
public class Carro extends Vehiculos{
    public Carro(String marca, String modelo, int serie){
        super(marca, modelo, serie);
    }
    
    public void Dar_Marcha_Atraz(){
        System.out.println("El carro ha dado marcha hacia atraz");
    }

    @Override
    public String toString(){
        return "Carro: "+" Marca: "+marca+" || Modelo: "+modelo+" || Serie: "+serie;
    }
    
}
