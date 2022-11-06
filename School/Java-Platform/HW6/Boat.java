package HW6;

abstract class Boat extends Item {
    int horsepower;
    /**
    * Construct a Boat item with specified name, cost, and horsepower.
    * @param name the name of the food.
    * @param cost the cost of the food.
    * @param horsepower the horsepower of the boat's engine.
    */
    public Boat( String name, double cost, int horsepower ) {
        super( name, cost );
        this.horsepower = horsepower;
    }
    /**
    * Get the number of horsepower for this Boat.
    * @return the horsepower of this boat's engine.
    */
    public int getHorsepower() {
        return this.horsepower;
    }
    /**
    * Set the number of horsepower for this boat.
    * @param horsepower the boat engine's horsepower.
    */
    public void setHorsepower(int horsepower) {
        this.horsepower = horsepower;
    }
    /**
    * Return a string representation of this Food.
    * @return a string in format Name -- Cost: $cost Horsepower: horsepower.
    */
    public String toString() {
        return super.toString() + " Horsepower: " + horsepower;
    }
        }