package HW6;

import java.text.NumberFormat;
/**
* A generic item sold at a store
*/
abstract class Item {
    double cost;
    String name;
    /**
    * Constructs a new item with cost of zero and null name.
    */
    public Item( )
    {
        cost = 0.0;
        name = "";
    }
    /**
    * Constructs a new Item with the given name and cost.
    * @param name the item name.
    * @param cost the item's cost.
    */
    public Item( String name, double cost )
    {
        this.name = name;
        this.cost = cost;
    }
    /**
    * Set the cost of this Item.
    * @param cost the cost of the item.
    */
    public void setCost( double cost )
    {
        this.cost = cost;
    }
    /**
    * Get the cost of this Item
    * @return the cost of the item.
    */
    public double getCost()
    {
        return this.cost;
    }
    /**
    * Set the name of this item.
    * @param name the item name.
    */
    public void setName( String name )
    {
        this.name = name;
    }
    /**
    * Get the name of this Item.
    * @return the name of the item.
    */
    public String getName( )
    {
        return this.name;
    }
    /**
    * Return a string representation of this Item.
    * @return a string in format Name -- Cost: $cost.
    */
    public String toString( )
    {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String result;
        result = name + " -- Cost: " + currency.format( cost );
        return result;
    }
    /**
    * Return a string that describes this item.
    * The default action is to return the item name
    */
    public String getDescription( )
    {
        return this.name;
    }
}