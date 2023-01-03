module com.example.lecture19 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.lecture19 to javafx.fxml;
    exports com.example.lecture19;
}