package HW6;

import java.text.NumberFormat;
import java.util.Locale;

public class Pastry extends Food {
    String flavor;
    
    public Pastry(String name, double cost, int calories, String flavor){
        super(name, cost, calories);
        this.flavor = flavor;
    }

    public String getFlavor(){
        return this.flavor;
    }

    public void setFlavor(String flavor){
        this.flavor = flavor;
    }

    public String getDescription( )
    {
        NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);
        return flavor + " " + super.getDescription() + " " + currency.format(super.getCost());
    }
}
