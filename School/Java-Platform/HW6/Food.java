package HW6;

abstract class Food extends Item {
    int calories;
    /**
    * Construct a Food item with specified name, cost, and calorie count.
    * @param name the name of the food.
    * @param cost the cost of the food.
    * @param calories the number of calories per serving.
    */
    public Food( String name, double cost, int calories ) {
        super( name, cost );
        this.calories = calories;
    }
    /**
    * Get the number of calories per serving of this Food.
    * @return the number of calories per serving.
    */
    public int getCalories() {
        return this.calories;
    }
    /**
    * Set the number of calories per serving of this Food.
    * @param calories the calories per serving.
    */
    public void setCalories(int calories) {
        this.calories = calories;
    }
    /**
    * Return a string representation of this Food.
    * @return a string in format Name -- Cost: $cost Calories: calories.
    */
    public String toString() {
        return super.toString() + " Calories: " + calories;
    }
}