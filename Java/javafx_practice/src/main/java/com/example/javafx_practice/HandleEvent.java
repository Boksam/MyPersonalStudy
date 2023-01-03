package com.example.javafx_practice;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class HandleEvent extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        Button btOK = new Button("OK");
        Button btNO = new Button("NO");

        OkHandler okHandler = new OkHandler();
        NoHandler noHandler = new NoHandler();

        btOK.setOnAction(okHandler);
        btNO.setOnAction(noHandler);

        HBox pane = new HBox(10);
        pane.getChildren().addAll(btOK, btNO);

        Scene scene = new Scene(pane);

        stage.setScene(scene);
        stage.show();
    }

    class OkHandler implements EventHandler<ActionEvent>{
        @Override
        public void handle(ActionEvent actionEvent) {
            System.out.println("OK clicked");
        }
    }
    class NoHandler implements EventHandler<ActionEvent>{
        @Override
        public void handle(ActionEvent actionEvent) {
            System.out.println("NO clicked");
        }
    }
}