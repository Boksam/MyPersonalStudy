package com.example.lecture19;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.scene.Scene;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

import java.io.*;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

//public class Server extends Application {
//    @Override
//    public void start(Stage stage) throws Exception {
//        TextArea ta = new TextArea();
//
//        Scene scene = new Scene(new ScrollPane(ta), 450, 200);
//        stage.setTitle("server");
//        stage.setScene(scene);
//        stage.show();
//
//        new Thread(() -> {
//            try {
//                ServerSocket serverSocket = new ServerSocket(8000);
//
//                Platform.runLater(() -> {
//                    ta.appendText("Server opened at " + new Date() + '\n');
//                });
//
//                Socket socket = serverSocket.accept();
//                DataInputStream inputFromClient = new DataInputStream(socket.getInputStream());
//                DataOutputStream outputToClient = new DataOutputStream(socket.getOutputStream());
//
//                while (true) {
//                    double radius = inputFromClient.readDouble();
//                    double area = radius * radius * Math.PI;
//
//                    outputToClient.writeDouble(area);
//
//                    Platform.runLater(() -> {
//                        ta.appendText("Radius received from Client: " + radius + '\n');
//                        ta.appendText("Area is: " + area + '\n');
//                    });
//                }
//            }
//            catch (IOException ex) {
//                ex.printStackTrace();
//            }
//        }).start();
//    }
//}


public class Server extends Application{
    @Override
    public void start(Stage stage) throws Exception {
        TextArea ta = new TextArea();
        Scene scene = new Scene(new ScrollPane(ta), 450, 200);
        stage.setTitle("Server");
        stage.setScene(scene);
        stage.show();

        new Thread(() -> {
            try {
                ServerSocket serverSocket = new ServerSocket(8000);
                Socket socket = serverSocket.accept();

                DataInputStream fromClient = new DataInputStream(socket.getInputStream());
                DataOutputStream toClient = new DataOutputStream(socket.getOutputStream());

                InetAddress inetAddress = socket.getInetAddress();
                while (true) {
                    double radius = fromClient.readDouble();
                    double area = radius * radius * Math.PI;

                    toClient.writeDouble(area);

                    Platform.runLater(() -> {
                        ta.appendText("Radius received from client: " + radius + '\n');
                        ta.appendText("Area is: " + area + '\n');
                        ta.appendText(inetAddress.getHostName() + '\n');
                    });
                }
            }
            catch (IOException ex) {
                ex.printStackTrace();
            }
        }).start();
    }
}