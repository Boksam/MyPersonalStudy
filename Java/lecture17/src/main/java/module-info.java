module lecture17.lecture17 {
    requires javafx.controls;
    requires javafx.fxml;


    opens lecture17.lecture17 to javafx.fxml;
    exports lecture17.lecture17;
}