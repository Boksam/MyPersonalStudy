package HW6;

import java.text.NumberFormat;
import java.util.Locale;

public class Caviar extends Food implements LuxuryItem {
    String origin;

    public Caviar(String name, double cost, int calories, String origin){
        super(name, cost, calories);
        this.origin = origin;
    }

    public double calculateLuxuryTax(){
        final double RATE = 0.15;
        return super.getCost() * RATE;
    }

    public String getOrigin(){
        return origin;
    }

    public void setOrigin(String origin){
        this.origin = origin;
    }

    public String getDescription(){
        NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);

        return super.getName() + " caviar from " + getOrigin() + " " + 
        currency.format(super.getCost() + calculateLuxuryTax()) + " ** Luxury tax added **";
    }
}
