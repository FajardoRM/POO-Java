package Actividad_Poo;

/**
 *Programacion orientada a objetos || NRC: 16362
 * Actividad Nº 1
 * @author Roberto Fajardo
 */
public class Clase_Principal {

    public static void main(String[] args) {
        Moto moto = new Moto("Kawasaki", "Z900 SE", 2022);
        Carro carro = new Carro("Toyota", "Corolla Axio", 2006);
        
        System.out.println("Vehiculo --> "+moto.toString());
        moto.Contramanillar();
        System.out.println("Vehiculo --> "+carro.toString());    
        carro.Dar_Marcha_Atraz();
        
        moto.setPlaca("PCZ1100");
        carro.setPlaca("JP000k");
        
        System.out.println("\t **Vehiculo con implementacion de placa**");
        System.out.println("Vehiculo --> "+moto.toString()+" || Placa: "+moto.getPlaca());
        System.out.println("Vehiculo --> "+carro.toString()+" || Placa: "+carro.getPlaca());
    }

}
