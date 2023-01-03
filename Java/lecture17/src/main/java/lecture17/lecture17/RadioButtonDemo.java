package lecture17.lecture17;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;

public class RadioButtonDemo extends CheckBoxDemo{
    @Override
    protected BorderPane getPane() {
        BorderPane pane = super.getPane();

        VBox paneForRadioButtons = new VBox(20);
        paneForRadioButtons.setPadding(new Insets(5, 5, 5, 5));
        paneForRadioButtons.setStyle("-fx-border-color : green");
        paneForRadioButtons.setStyle("-fx-border-width : 2px; -fx-border-color : green");
        RadioButton rbRed = new RadioButton("Red");
        RadioButton rbGreen = new RadioButton("Green");
        RadioButton rbBlue = new RadioButton("Blue");
        paneForRadioButtons.getChildren().addAll(rbRed, rbGreen, rbBlue);
        pane.setLeft(paneForRadioButtons);

        EventHandler<ActionEvent> rbHandler = e -> {
            if (rbRed.isSelected())
                text.setFill(Color.RED);
            if (rbGreen.isSelected())
                text.setFill(Color.GREEN);
            if (rbBlue.isSelected())
                text.setFill(Color.BLUE);
        };

        rbRed.setOnAction(rbHandler);
        rbGreen.setOnAction(rbHandler);
        rbBlue.setOnAction(rbHandler);

        ToggleGroup group = new ToggleGroup();
        rbRed.setToggleGroup(group);
        rbBlue.setToggleGroup(group);
        rbGreen.setToggleGroup(group);

        return pane;
    }
}
