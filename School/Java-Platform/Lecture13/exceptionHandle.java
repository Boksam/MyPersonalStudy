package Lecture13;
import java.util.Scanner;

public class exceptionHandle {
    public static double divide(int n1, int n2){
        if (n2 == 0)
            throw new ArithmeticException("Divisor cannot be zero");
        return n1/ n2;
    }
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n1 = input.nextInt();
        int n2 = input.nextInt();

        try{
            double result = divide(n1, n2);
            System.out.println(result);
        }
        catch(ArithmeticException ex){
            System.out.println("Divisor cannot be zero");
        }

        System.out.println("Out of try-catch");
    }
}

