package com.example.lecture19;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class MyChatClient {
    private Socket socket = null;
    private DataOutputStream streamOut = null;
    private Scanner console = null;

    public MyChatClient(String hostName, int port) {
        console = new Scanner(System.in);
        try {
            socket = new Socket(hostName, port);
            streamOut = new DataOutputStream(socket.getOutputStream());

            String line = "";
            while (!line.equals(".bye")) {
                line = console.nextLine();
                streamOut.writeUTF(line);
                streamOut.flush();
            }
        }
        catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Wrong args");
            System.exit(-1);
        }
        MyChatClient myChatClient = new MyChatClient(args[0], Integer.parseInt(args[1]));
    }
}