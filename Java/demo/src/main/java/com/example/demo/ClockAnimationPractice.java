package com.example.demo;


import javafx.application.Application;
import javafx.stage.Stage;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.util.Duration;

public class ClockAnimationPractice extends Application{
    @Override
    public void start(Stage stage) throws Exception {
        ClockPanePractice clock = new ClockPanePractice();

        EventHandler<ActionEvent> eventHandler = e -> {
            clock.setCurrentTime();
        };

        Timeline animation = new Timeline(new KeyFrame(Duration.millis(1000), eventHandler));
        animation.setCycleCount(Timeline.INDEFINITE);
        animation.play();

        Scene scene = new Scene(clock, 250, 50);
        stage.setScene(scene);
        stage.show();
    }
}
