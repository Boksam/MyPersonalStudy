package HW6;

public class ParkJunwooInvoice {
    public static void main(String[] args){
        Pastry croissant = new Pastry("Croissant", 1.99, 200, "Chocolate");

        Motorboat Evinrude = new Motorboat("Evinrude", 3475.00, 400, 5);

        Yacht oceano = new Yacht("oceano", 950000, 1500, 12);

        Caviar Beluga = new Caviar("Beluga", 570.00, 800, "Caspian Sea");
        
        System.out.println(croissant.getDescription());
        System.out.println(Evinrude.getDescription());
        System.out.println(oceano.getDescription());
        System.out.println(Beluga.getDescription());
    }
}
