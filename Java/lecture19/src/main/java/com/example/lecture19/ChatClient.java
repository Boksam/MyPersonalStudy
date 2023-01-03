package com.example.lecture19;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class ChatClient {
    private Socket socket = null;
    private Scanner console = null;
    private DataOutputStream streamOut = null;

    public ChatClient(String hostIPAddress, int serverPort) {
        System.out.println("Establishing connection, Please wait ....");
        console = new Scanner(System.in);
        try {
            socket = new Socket(hostIPAddress, serverPort);
            System.out.println("Connected: " +  socket);
            start();
        } catch (UnknownHostException e) {
// TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
// TODO Auto-generated catch block
            e.printStackTrace();
        }
        String line = "";
        try {
            while (!line.equals(".bye")) {
                line = console.nextLine();
                streamOut.writeUTF(line);
                streamOut.flush();
            }
        } catch(IOException ioe) {
        }
    }

    public void start() throws IOException {
        streamOut = new DataOutputStream(socket.getOutputStream());
    }

    public void stop() {
        try {
            if (console != null) console.close();
            if (streamOut != null)streamOut.close();
            if (socket != null) socket.close();
        } catch (IOException e) {
// TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java ChatClient serverIP port");
            System.exit(-1);
        }
        ChatClient client = new ChatClient(args[0], Integer.parseInt(args[1]));
        client.stop();
    }
}

