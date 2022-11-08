public class Main {
    public static void main(String[] args) {
        Edible stuff = new Chicken();
        eat(stuff);
    }
    public static void eat(Edible food){
        System.out.println(food.howToEat());
    }
}

interface Edible{
    public String howToEat();
}

class Chicken implements Edible{
    @Override
    public String howToEat(){
        return "Fry it";
    }
}

class Brocolli implements Edible{
    @Override
    public String howToEat(){
        return "Stir-Fry it";
    }
}
