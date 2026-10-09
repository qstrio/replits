import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    System.out.println("Enter your first number:");
    Scanner S = new Scanner(System.in);
    Double numOne = S.nextDouble();
    System.out.println("Enter your second number: ");
    Double numTwo = S.nextDouble();
    System.out.println("Enter your operator +-*/: ");
    char operator = S.next().charAt(0);
    Double sum = numOne+numTwo;
    Double difference = numOne-numTwo;
    Double product = numOne*numTwo;
    Double quotient = numOne/numTwo;
    if (operator == "+") {
      result = numOne+numTwo
    }
    else if (operator == "-") {
      System.out.println(numOne + operator + numTwo + "=" + difference);
    }
    else if (avg >= 70 && avg <= 79) {
      System.out.println("Your letter grade is: C");
    }   
    else if (avg >= 60 && avg <= 69) {
      System.out.println("Your letter grade is: D");
    }   
    else {
      System.out.println("Your letter grade is: F");
    }   
    }
    
  }


