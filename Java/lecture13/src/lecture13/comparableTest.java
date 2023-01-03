package lecture13;

import java.util.Arrays;

public class comparableTest {
    public static void main(String[] args) {
        myRectangle[] myRecList = {new myRectangle(11.4),
        new myRectangle(5.4), new myRectangle(8.0)};

        Arrays.sort(myRecList);

        for (myRectangle rect : myRecList) {
            System.out.println(rect);
        }
    }
}

class myRectangle implements Comparable<myRectangle> {
    private double area;

    public myRectangle(double area) {
        this.area = area;
    }

    public double getArea() {
        return area;
    }

    @Override
    public int compareTo(myRectangle o) {
        if (this.area > o.getArea())
            return 1;
        else if (this.area == o.getArea())
            return 0;
        else
            return -1;
    }

    @Override
    public String toString() {
        return Double.toString(area);
    }
}
