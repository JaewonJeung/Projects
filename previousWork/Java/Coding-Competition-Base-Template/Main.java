import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.math.*;
import java.util.Collections; 
/**
STRING TO INTEGER
Integer.parseInt(str)

INTEGER TO STRING
Integer.toString(int)

STRING INPUT
String inputStr1 = input.nextLine();
String inputStr2 = input.nextLine(); 
String inputStr3 = input.nextLine();

INT INPUT
int inputInt1 = input.nextInt();
int inputInt2 = input.nextInt();
int inputInt3 = input.nextInt();

INT INPUT ARRAY INITIALIZE
int inputInt1 = input.nextInt();
int [] firstArr = new int[inputInt1];  //array with inputInt1 length
int inputInt2 = input.nextInt();
int [] secondArr = new int [inputInt2];  //array with inputInt2 length

POPULATING ARRAYS BASED ON THE INPUTS
for (int i = 0; i < firstArr.length; i++){
  firstArr[i] = input.nextInt();
}
for (int j = 0; j < secondArr.length; j++){
  secondArr[j] = input.nextInt();
}

NESTED FOR LOOP
for (int i < 0; i < NUM; i++){
  for (int j < 0; j < NUM; j++){
    
  }
}

ARRAYLIST INITIALIZE
ArrayList<Integer> arrl1 = new ArrayList<Integer>();
ArrayList<Integer> arrl2 = new ArrayList<Integer>();

SIMPLE PRINT METHOD
print(array)
print(str)

ARRAY SORT ASCENDING
Arrays.sort(arr); 

ARRAY SORT DESCENDING
arr must be Integer type
Arrays.sort(arr, Collections.reverseOrder());

POPULATE ARRAYLIST WITH ARRAY
ArrayList arrl1 = new ArrayList<>(Arrays.asList(array))

*/
class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    

  }

  public static void print(Object o){
    if (o instanceof int[]){
      int [] other = (int [])o;
      System.out.println(Arrays.toString(other));
    }
    else if (o instanceof Integer){
      int other = (int)o;
      System.out.println(other);
    }
    else if (o instanceof String){
      String other = (String)o;
      System.out.println(other);
    }
  }
}