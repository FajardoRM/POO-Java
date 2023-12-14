package Actividad_Poo;

/**
 Programacion orientada a objetos || NRC: 16362
 * Actividad Nº 1
 * @author Roberto Fajardo
 */
public abstract class Vehiculos {
    public String marca, modelo;
    public Integer serie;
    private String placa;
    
    public Vehiculos(String marca, String modelo, Integer serie ){
        this.marca = marca;
        this.modelo = modelo;
        this.serie = serie;
    }
    
    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }
    
    public abstract String toString();
    
}
