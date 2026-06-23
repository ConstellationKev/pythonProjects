import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int dec_num;
    int bin_place = 0;
    boolean is_zero = false;
    System.out.println("Enter a decimal number: ");
    dec_num = scanner.nextInt();
    scanner.nextLine();
    
    if (dec_num == 0) {
      System.out.println("Binary: 0");
      is_zero = true;
    }
    
    while (dec_num >= Math.pow(2, bin_place)) {
      if (dec_num < Math.pow(2, bin_place+1)) {
        break;
      }
      else {
        bin_place++;
      }
    }

    double ex_num;
    double bin_num = Math.pow(10, bin_place);
    ex_num = bin_num;
    
    dec_num -= Math.pow(2, bin_place);
    
    // System.out.println(bin_place);
    // System.out.println(Math.pow(2, bin_place));
    bin_place = 0;
    // System.out.println(bin_num);
    // System.out.println(dec_num);
    // System.out.println("------");
    
    while (dec_num > 0) {
      while (dec_num >= Math.pow(2, bin_place)) {
        if (dec_num < Math.pow(2, bin_place+1)) {
          break;
        }
        else {
          bin_place++;
        }
      }
      
      bin_num = Math.pow(10, bin_place);
      // System.out.println(bin_num);
      ex_num += bin_num;
      dec_num -= Math.pow(2, bin_place);
      // System.out.println(dec_num);
      bin_place = 0;
      
    }
    if (is_zero) {
      ;
    }
    else {
    int fin_num = (int)ex_num;
    System.out.println("Binary: " + fin_num);
    }
  }
}