package com.example.javafx_practice;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class AnonymousHandlerDemo extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        HBox hBox = new HBox(10);

        Button btNew = new Button("New");
        Button btOpen = new Button("Open");
        Button btSave = new Button("Save");
        Button btPrint = new Button("Print");

        btNew.setOnAction((ActionEvent e) -> {
            System.out.println("Process New");
        });
        btOpen.setOnAction((ActionEvent e) -> {
            System.out.println("Process Open");
        });
        btSave.setOnAction((ActionEvent e) -> {
            System.out.println("Process Save");
        });
        btPrint.setOnAction((ActionEvent e) -> {
            System.out.println("Process Print");
        });

        hBox.setAlignment(Pos.CENTER);
        hBox.getChildren().addAll(btNew, btOpen, btPrint, btSave);

        Scene scene = new Scene(hBox);
        stage.setScene(scene);
        stage.show();
    }
}