import java.io.*;

public class Solution {
    public static void main (String [] args){
        int lines;
        try {
            BufferedReader is = new BufferedReader(new InputStreamReader(System.in));
            int inputLine;
            for (lines=3;lines>0;lines--){
                inputLine = Integer.parseInt(is.readLine());
                System.out.println(inputLine);
            }
        } catch (IOException exception){
            System.out.print(exception);
        }
        }
    }
