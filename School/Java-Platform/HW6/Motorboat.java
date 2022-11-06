package HW6;

import java.text.NumberFormat;
import java.util.Locale;

public class Motorboat extends Boat{
    int seats;

    public Motorboat(String name, double cost, int horsepower, int seats){
        super(name, cost, horsepower);
        this.seats = seats;
    }

    public int getSeats(){
        return this.seats;
    }

    public void setSeats(int seats){
        this.seats = seats;
    }

    public String getDescription() {
        NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);

        return super.getDescription() + " " + Integer.toString(seats) + "-seat Motorboat " + currency.format(super.getCost());
    }
}
