import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    System.out.print("The radius of your circle is: ");
    Scanner S = new Scanner(System.in);
    double r = S.nextDouble();
    double p = 2*3.14*r;
    double a = 3.14*r*r;
    System.out.print("The area of your circle is: " + a + " and the circumference of your circle is: " + p);
  }
}