package com.example.lecture19;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class MyChatServer {
    private ServerSocket server = null;
    private Socket socket = null;
    private DataInputStream streamIn = null;

    public MyChatServer(int port) {
        try {
            server = new ServerSocket(port);
            System.out.println("Server initiated: " + server);
            socket = server.accept();
            streamIn = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
            boolean done = false;
            while (!done) {
                try {
                    String line = streamIn.readUTF();
                    System.out.println(line);
                    done = line.equals(".bye");
                }
                catch (IOException ioe) {
                    done = true;
                }
            }

            server = null;
            socket = null;
            streamIn = null;
        }
        catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("args 0: portNum");
            System.exit(-1);
        }
        MyChatServer myChatServer = new MyChatServer(Integer.parseInt(args[0]));
    }
}
