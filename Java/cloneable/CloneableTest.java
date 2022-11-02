package cloneable;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class CloneableTest {
    public static void main(String[] args){
        Calendar calendar = new GregorianCalendar(2022, 11, 1);
        Calendar calendar1 = calendar;
        Calendar calendar2 = (Calendar)calendar.clone();
        System.out.println(calendar == calendar1);
        System.out.println(calendar == calendar2);
        System.out.println(calendar.equals(calendar2));

        ArrayList<Double> list1 = new ArrayList<>();
        list1.add(1.5);
        
    }
}
