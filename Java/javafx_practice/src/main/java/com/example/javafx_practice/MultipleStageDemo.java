package com.example.javafx_practice;

import javafx.application.Application;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;

import java.util.Stack;

public class MultipleStageDemo{
    public static void main(String[] args){
        DoubleProperty d1 = new SimpleDoubleProperty(1);
        DoubleProperty d2 = new SimpleDoubleProperty(2);
        d1.bind(d2);
        System.out.println(d1.getValue() + " " + d2.getValue());
        d2.setValue(70.2);
        System.out.println(d1.getValue() + " " + d2.getValue());
    }
}
