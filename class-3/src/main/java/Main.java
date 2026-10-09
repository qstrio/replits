import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    System.out.print("Enter a character:");
    Scanner S = new Scanner(System.in);
    String c = S.next();
    char ch = c.charAt(0);
    if (Character.isDigit(ch)) {
      System.out.print("Your character is a digit!");
    }
    if (Character.isUpperCase(ch)) {
      System.out.print("Your character is an uppercase letter!");
    }
    if (Character.isLowerCase(ch)) {
      System.out.print("Your character is a lowercase letter!");
    }
}
}