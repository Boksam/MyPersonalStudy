module com.example.lecture_11_08_javafx {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.lecture_11_08_javafx to javafx.fxml;
    exports com.example.lecture_11_08_javafx;
}