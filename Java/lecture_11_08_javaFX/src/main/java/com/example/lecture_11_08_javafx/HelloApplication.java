package com.example.lecture_11_08_javafx;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

import java.io.IOException;


public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        //Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        /*stage.setTitle("Hello!");
        Button btOK = new Button("ok");
        Scene scene = new Scene(btOK, 200, 250);
        stage.setScene(scene);
        stage.show();

        Stage stage2 = new Stage();
        stage2.show();*/
        HBox pane = new HBox(10);
        pane.setAlignment(Pos.CENTER);

        Button btOK = new Button("OK");
        btOK.setOnAction(e -> {
            System.out.println("OK button clicked");
        });
//        btOK.setOnAction(new OKHandlerClass());
        pane.getChildren().addAll(btOK);
//
//        Button btCancel = new Button("Cancel");
//        btCancel.setOnAction(new CancelHandlerClass());
//        pane.getChildren().addAll(btCancel);

        Scene scene = new Scene(pane);
        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();

    }

    public static void main(String[] args) {
        launch();
    }
}

/*class OKHandlerClass implements EventHandler<ActionEvent>{
    @Override
    public void handle(ActionEvent actionEvent) {
        System.out.println("OK button clicked");

    }
}

class CancelHandlerClass implements EventHandler<ActionEvent>{
    @Override
    public void handle(ActionEvent actionEvent) {
        System.out.println("Cancel button clicked");
    }
}*/