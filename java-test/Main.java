import java.io.*;
import java.net.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ServerSocket server = new ServerSocket(8080);

        System.out.println("Java test server running on port 8080");

        while (true) {
            Socket socket = server.accept();

            BufferedReader in = new BufferedReader(
                new InputStreamReader(socket.getInputStream())
            );

            String line = in.readLine();

            PrintWriter out = new PrintWriter(socket.getOutputStream());

            if (line != null && line.contains("GET / ")) {
                String body = "CS321 Java CI test is working";

                out.print(
                    "HTTP/1.1 200 OK\r\n" +
                    "Content-Type: text/plain\r\n" +
                    "Content-Length: " + body.length() + "\r\n" +
                    "\r\n" +
                    body
                );
            } else {
                out.print(
                    "HTTP/1.1 404 Not Found\r\n" +
                    "Content-Length: 0\r\n" +
                    "\r\n"
                );
            }

            out.flush();
            socket.close();
        }
    }
}
