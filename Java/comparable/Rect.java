package comparable;

public class Rect {
    public int width;
    public int height;
    public int area;

    public Rect(int width, int height){
        this.width = width;
        this.height = height;
        this.area = width * height;
    }
    
    /*public Rect(){

    }*/

    public int getArea(){
        return this.area;
    }
}
