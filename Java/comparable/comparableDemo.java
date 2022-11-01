package comparable;

public class comparableDemo {
    public static void main(String[] args){
        comparableRect[] rectangles = {
            new comparableRect(3, 5),
            new comparableRect(13, 55),
            new comparableRect(7, 35),
            new comparableRect(1, 25)
        };

        java.util.Arrays.sort(rectangles);

        for (comparableRect o : rectangles){
            System.out.println(o);
        }
    }
}

class myInteger extends Number implements Comparable<myInteger>{

    public int compareTo(myInteger o){

        return 0;
    }

    @Override
    public int intValue() {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public long longValue() {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public float floatValue() {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public double doubleValue() {
        // TODO Auto-generated method stub
        return 0;
    }
    
}