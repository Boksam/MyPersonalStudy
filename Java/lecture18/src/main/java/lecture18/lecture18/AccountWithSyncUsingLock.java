package lecture18.lecture18;

import java.util.concurrent.*;
import java.util.concurrent.locks.*;

//public class AccountWithSyncUsingLock {
//    private static Account account = new Account();
//
//    public static void main(String[] args) {
//        ExecutorService executor = Executors.newFixedThreadPool(100);
//
//        for (int i = 0; i < 100; i++){
//            executor.execute(new AddAPennyTask());
//        }
//
//        executor.shutdown();
//
//        while (!executor.isTerminated()) {}
//
//        System.out.println("What is balance? " + account.getBalance());
//    }
//
//    public static class AddAPennyTask implements Runnable {
//        @Override
//        public void run() {
//            account.deposit(1);
//        }
//    }
//
//    public static class Account {
//        private static Lock lock = new ReentrantLock();
//        private int balance = 0;
//
//        public int getBalance() {
//            return balance;
//        }
//
//        public void deposit(int amount) {
//            lock.lock();
//
//            try {
//                int newBalance = balance + amount;
//                Thread.sleep(5);
//                balance = newBalance;
//            }
//            catch (InterruptedException ex) {}
//            finally {
//                lock.unlock();
//            }
//        }
//    }
//}

public class AccountWithSyncUsingLock {
    private static Account account = new Account();

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        executor.execute(new DepositTask());
        executor.execute(new WithdrawTask());
    }

    private static class DepositTask implements Runnable {
        @Override
        public void run() {
            while (true) {
                account.deposit((int)(Math.random() * 10 + 1));
            }
        }
    }

    private static class WithdrawTask implements Runnable {
        @Override
        public void run() {
            while (true) {
                account.withdraw((int)(Math.random() * 10 + 1));
            }
        }
    }
    private static class Account {
        private int balance = 0;
        private Lock lock = new ReentrantLock();
        private Condition newDeposit = lock.newCondition();
        private Semaphore semaphore = new Semaphore(1);

        public void deposit(int n) {
            semaphore.acquire();
            try {
                Thread.sleep(1000);
                balance += n;
                newDeposit.signalAll();
            }
            catch (InterruptedException ex) {
                ex.printStackTrace();
            }
            finally {
                semaphore.release();
            }
        }

        public void withdraw(int n) {
            semaphore.acquire();
            try {
                while (balance < n) {
                    newDeposit.await();
                }
                balance -= n;
            }
            catch (InterruptedException ex) {
                ex.printStackTrace();
            }
            finally {
                semaphore.release();
            }
        }
    }
}