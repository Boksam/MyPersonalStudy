package comparable;

public class comparableRect extends Rect implements Comparable<comparableRect>{
    
    public comparableRect(int width, int height){
        super(width, height);
    }

    @Override
    public int compareTo(comparableRect o){
        if (this.getArea() > o.getArea())
            return 1;
        if (this.getArea() == o.getArea())
            return 0;
        return -1;
    }

    public String toString(){
        return super.toString() + "Area: " + getArea();
    }
}
