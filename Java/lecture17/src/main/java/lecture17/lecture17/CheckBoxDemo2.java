package lecture17.lecture17;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.scene.text.FontWeight;

public class CheckBoxDemo2 extends ButtonDemo2 {
    @Override
    protected BorderPane getPane() {
        BorderPane pane = super.getPane();

        Font fontBoldItalic = Font.font("Times New Roman",
                FontWeight.BOLD, FontPosture.ITALIC, 20);
        Font fontBold = Font.font("Times New Roman",
                FontWeight.BOLD, FontPosture.REGULAR, 20);
        Font fontItalic = Font.font("Times New Roman",
                FontWeight.NORMAL, FontPosture.ITALIC, 20);
        Font fontNormal = Font.font("Times New Roman",
                FontWeight.NORMAL, FontPosture.REGULAR, 20);

        VBox paneForCheckBoxes = new VBox(20);
        paneForCheckBoxes.setPadding(new Insets(5, 5, 5, 5));
        paneForCheckBoxes.setStyle("-fx-border-color: green");

        CheckBox btBold = new CheckBox("Bold");
        CheckBox btItalic = new CheckBox("Italic");
        paneForCheckBoxes.getChildren().addAll(btBold, btItalic);
        pane.setRight(paneForCheckBoxes);

        EventHandler<ActionEvent> handler = e -> {
            if (btBold.isSelected() && btItalic.isSelected())
                text.setFont(fontBoldItalic);
            else if (btBold.isSelected() && !btItalic.isSelected())
                text.setFont(fontBold);
            else if (!btBold.isSelected() && btItalic.isSelected())
                text.setFont(fontItalic);
            else
                text.setFont(fontNormal);
        };

        btBold.setOnAction(handler);
        btItalic.setOnAction(handler);

        return pane;
    }
}
