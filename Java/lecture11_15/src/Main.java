import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        executor.execute(new PrintChar('a'));
        executor.execute(new PrintChar('b'));
        executor.execute(new PrintChar('c'));

        executor.shutdown();
    }

    public static class PrintChar implements Runnable {
        char c;
        public PrintChar(char c){
            this.c = c;
        }

        @Override
        public void run() {
            for (int i = 0; i < 100; i++)
                System.out.print(c + " ");
        }
    }
}

