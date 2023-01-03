module lecture18.lecture18 {
    requires javafx.controls;
    requires javafx.fxml;


    opens lecture18.lecture18 to javafx.fxml;
    exports lecture18.lecture18;
}