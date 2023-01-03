package lecture18.lecture18;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

//public class TaskThreadDemo {
//    public static void main(String[] args){
//        ExecutorService executor = Executors.newFixedThreadPool(1);
//        executor.execute(new PrintChar('a', 100));
//        executor.execute(new PrintChar('b', 100));
//        executor.execute(new PrintNum(100));
//
//        executor.shutdown();
//    }
//}
//
//class PrintChar implements Runnable {
//    private char charToPoint;
//    private int times;
//
//    public PrintChar(char c, int t){
//        this.charToPoint = c;
//        this.times = t;
//    }
//
//    @Override
//    public void run() {
//        for (int i = 0; i < times; i++) {
//            System.out.print(charToPoint);
//        }
//    }
//}
//
//class PrintNum implements Runnable {
//    private int maxNum;
//
//    public PrintNum(int n){
//        this.maxNum = n;
//    }
//
//    @Override
//    public void run() {
//        Thread thread4 = new Thread(new PrintChar('c', 40));
//        thread4.start();
//        try {
//            thread4.join();
//            for (int i = 0; i <= this.maxNum; i++) {
//                System.out.print(i);
//            }
//        } catch (InterruptedException ex) {
//            ex.printStackTrace();
//        }
//    }
//}

public class TaskThreadDemo {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        executor.execute(new PrintChar('A'));
        executor.execute(new PrintChar('B'));
        executor.execute(new PrintNum(100));

        executor.shutdown();
    }
}

class PrintChar implements Runnable {
    private char c;

    public PrintChar(char c) {
        this.c = c;
    }

    @Override
    public void run() {
        for (int i = 0; i < 100; i++)
            System.out.print(c);
    }
}

class PrintNum implements Runnable {
    private int n;

    public PrintNum(int n) {
        this.n = n;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < n; i++) {
                System.out.print(i);
                Thread.sleep(10);
            }
        }
        catch (InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}