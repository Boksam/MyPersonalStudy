package lecture17.lecture17;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;

public class RadioButtonDemo2 extends CheckBoxDemo2{
    @Override
    protected BorderPane getPane() {
        BorderPane pane = super.getPane();

        VBox paneForRadioButtons = new VBox(20);
        paneForRadioButtons.setPadding(new Insets(5, 5, 5, 5));
        paneForRadioButtons.setStyle("-fx-border-color: green");

        RadioButton rbRed = new RadioButton("Red");
        RadioButton rbGreen = new RadioButton("Green");
        RadioButton rbBlue = new RadioButton("Blue");
        paneForRadioButtons.getChildren().addAll(rbRed, rbGreen, rbBlue);

        ToggleGroup group = new ToggleGroup();
        rbRed.setToggleGroup(group);
        rbGreen.setToggleGroup(group);
        rbBlue.setToggleGroup(group);

        EventHandler<ActionEvent> handler = e -> {
            if (rbRed.isSelected())
                text.setFill(Color.RED);
            if (rbGreen.isSelected())
                text.setFill(Color.GREEN);
            if (rbBlue.isSelected())
                text.setFill(Color.BLUE);
        };

        rbRed.setOnAction(handler);
        rbBlue.setOnAction(handler);
        rbGreen.setOnAction(handler);

        pane.setLeft(paneForRadioButtons);

        return pane;
    }
}
