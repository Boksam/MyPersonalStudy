package com.example.javafx_practice;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class ControlCircle extends Application {
    private CirclePane circlePane = new CirclePane();

    @Override
    public void start(Stage stage) throws Exception {
        HBox hbox = new HBox(10);

        Button btEnlarge = new Button("Enlarge");
        Button btShrink = new Button("Shrink");

        EnlargeHandle enlargeHandle = new EnlargeHandle();
        ShrinkHandle shrinkHandle = new ShrinkHandle();

        btEnlarge.setOnAction(enlargeHandle);
        btShrink.setOnAction(shrinkHandle);

        hbox.getChildren().addAll(btEnlarge, btShrink);

        BorderPane pane = new BorderPane();
        pane.setCenter(circlePane);
        pane.setBottom(hbox);
        BorderPane.setAlignment(hbox, Pos.CENTER);
        Scene scene = new Scene(pane, 200, 150);

        stage.setScene(scene);
        stage.show();
    }
    class EnlargeHandle implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent actionEvent) {
            circlePane.enlarge();
        }
    }

    class ShrinkHandle implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent actionEvent) {
            circlePane.shrink();
        }
    }

    class CirclePane extends StackPane {
        private Circle circle = new Circle(50);

        public CirclePane() {
            getChildren().add(circle);
            circle.setRadius(10);
            circle.setStroke(Color.BLACK);
            circle.setFill(Color.WHITE);
        }

        public void enlarge() {
            circle.setRadius(circle.getRadius() + 2);
        }

        public void shrink() {
            circle.setRadius(circle.getRadius() > 2 ? circle.getRadius() - 2 : circle.getRadius());
        }
    }


}