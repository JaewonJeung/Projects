import java.util.Arrays;

class Main {
  public static void main(String[] args) {
    int temp = 0;
    String tempStr = "";
    int count = 0;
    
    for(int i = 1; i < 1000; i++){
      for(int j = i; j < 1000; j++){
        temp = 0;
        temp = i * j;
        if (temp < 1000){
          tempStr = Integer.toString(temp);
          String [] arr = tempStr.split("");
          if(arr.length == 1){
            count++;
            System.out.println(Arrays.toString(arr));
            System.out.println(count);
            continue;
          }
          for(int k = 0; k < arr.length-1; k++){
            if(Integer.parseInt(arr[k]) < Integer.parseInt(arr[k+1])){
              if((k+1) == arr.length-1){
                System.out.println(Arrays.toString(arr));
                System.out.println(count);
                count++;
              }
            }
            else{
              break;
            }
          }
        }
      }
    }
    System.out.println(count);
  }
}
//Integer.toString