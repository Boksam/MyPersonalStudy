package lecture18.lecture18;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

import java.util.Stack;


//public class FlashText extends Application {
//    private String text = "";
//    @Override
//    public void start(Stage stage) throws Exception {
//        Label lbText = new Label("Programming is Fun");
//
//        StackPane pane = new StackPane();
//        pane.getChildren().add(lbText);
//
//        Scene scene = new Scene(pane);
//
//        stage.setScene(scene);
//        stage.show();
//
//        new Thread(() -> {
//                try {
//                    while (true) {
//                        if (lbText.getText().trim().length() == 0)
//                            text = "Welcome";
//                        else
//                            text = "";
//
//                        Platform.runLater(() -> {
//                            lbText.setText(text);
//                        });
//
//                        Thread.sleep(200);
//                    }
//                }
//                catch (InterruptedException ex){
//                    ex.printStackTrace();
//                }
//        }).start();
//    }
//}
