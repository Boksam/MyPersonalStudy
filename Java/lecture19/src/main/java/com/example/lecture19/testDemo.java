package com.example.lecture19;

public class testDemo {
    abstract static class Parent {
        private int x = 10;

        public Parent() {
            System.out.println("Super constructor called");
            x = 20;
        }
        public int getX() {
            return x;
        }
    }

    static class Child extends Parent {
        private int x = 100;

    }

    public static void main(String[] args) {
        Parent c = new Child();

        System.out.println(c.getX());
    }
}
