package lecture13;

import java.util.Date;


class House {
    public static void main(String[] args) {
        MyHouse house1 = new MyHouse(1, 50.2);
        MyHouse house2 = new MyHouse(2, 25.9);
        MyHouse house3 = house1;
        try {
            Thread.sleep(5000);
        }
        catch (InterruptedException ex) {
        }
        MyHouse house4 = house1.clone();

        System.out.println(house3);
        System.out.println(house4);
    }
}

class MyHouse implements Cloneable, Comparable<MyHouse> {
    private int id;
    private double area;
    private Date whenBuilt;

    public MyHouse(int id, double area) {
        this.id = id;
        this.area = area;
        whenBuilt = new Date();
    }

    public int getId() {
        return id;
    }

    public double getArea() {
        return area;
    }

    public Date getWhenBuilt() {
        return whenBuilt;
    }

    @Override
    public int compareTo(MyHouse o) {
        if (area > o.getArea())
            return 1;
        else if (area == o.getArea())
            return 0;
        else
            return -1;
    }

    @Override
    protected MyHouse clone() {
        MyHouse tmp = new MyHouse(this.id, this.area);
        tmp.whenBuilt = (Date)(whenBuilt.clone());
        return tmp;
    }

    @Override
    public String toString() {
        String message = "";
        message += "Id : " + this.id + '\n';
        message += "Area : " + this.area + '\n';
        message += "WhenBuilt : " + this.whenBuilt.toString() + '\n';
        return message;
    }
}
