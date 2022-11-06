package HW6;

import java.text.NumberFormat;
import java.util.Locale;

public class Yacht extends Boat implements LuxuryItem{
    int cabins;

    public Yacht(String name, double cost, int horsepower, int cabins){
        super(name, cost, horsepower);
        this.cabins = cabins;
    }

    public double calculateLuxuryTax(){
        final double RATE = 0.1;
        return super.getCost() * RATE; 
    }

    public String getDescription() {
        NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);

        return super.getName() + " " + Integer.toString(cabins) + "-cabins yacht " + 
        currency.format(super.getCost() + calculateLuxuryTax()) + " ** Luxury tax added **"; 
    }

    public int getCabins() {
        return this.cabins;
    }

    public void setCabins(int cabins){
        this.cabins = cabins;
    }
}
