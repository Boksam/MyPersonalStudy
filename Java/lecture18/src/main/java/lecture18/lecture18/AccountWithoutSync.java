package lecture18.lecture18;

import javafx.application.Platform;

import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

//public class AccountWithoutSync {
//    private static Account account = new Account();
//
//    public static void main(String[] args){
//        ExecutorService executor = Executors.newCachedThreadPool();
//
//        for (int i = 0; i < 100; i++)
//            executor.execute(new AddAPennyTask());
//
//        executor.shutdown();
//
//        while (!executor.isTerminated()){}
//
//        System.out.println(account.getBalance());
//    }
//
//    private static class AddAPennyTask implements Runnable {
//        @Override
//        public void run() {
//            account.deposit(1);
//        }
//    }
//
//    private static class Account {
//        private int balance = 0;
//        private Lock lock = new ReentrantLock();
//
//        public int getBalance() {
//            return balance;
//        }
//
//        public void deposit(int amount) {
//            lock.lock();
//            try {
//                int newBalance = balance + amount;
//                balance = newBalance;
//                Thread.sleep(5);
//            }
//            catch (InterruptedException ex){
//                ex.printStackTrace();
//            }
//            finally {
//                lock.unlock();
//            }
//        }
//    }
//}

public class AccountWithoutSync {
    private static Account account = new Account();

    private static class Account {
        private int balance = 0;
        Lock lock = new ReentrantLock();

        public void  deposit(int n) {
            lock.lock();
            balance += n;
            lock.unlock();
        }

        public int getBalance() {
            return balance;
        }
    }

    private static class AddAPenny implements Runnable {
        @Override
        public void run() {
            account.deposit(1);
        }
    }

    public static void main(String[] args) {
        ExecutorService executor = Executors.newCachedThreadPool();
        for (int i = 0; i < 100; i++) {
            executor.execute(new AddAPenny());
        }

        executor.shutdown();

        while (!executor.isTerminated()){}

        System.out.println(account.getBalance());
    }
}

