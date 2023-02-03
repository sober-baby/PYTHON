#include <stdio.h>
#include <math.h>

int baseConversion(int, int, int);

int main() {
  // initialize variables
  char sign = '$';
  int b1, b2, n1, n2;

  do {
    printf("Give input ($ to stop): ");
    scanf(" %c", &sign);

    if ((sign != '+') && (sign != '-') && (sign != '*') && (sign != '/') && (sign != '$'))
        printf("Invalid Input\n");

    else if (sign == '$')
        break;

    else
    {
      scanf(" %d %d %d %d", &b1, &n1, &n2, &b2);
      int calc; 

      //Converting numbers
      int num1 = baseConversion(n1, b1, 10);
      int num2 = baseConversion(n2, b1, 10);

      //Calculations
      if (sign == '+')
        calc = num1 + num2;
      else if (sign == '-')
        calc = num1 - num2;
      else if (sign == '*')
        calc = num1 * num2;
      else
        calc = num1 / num2; 

      int newNum =  baseConversion(calc, 10, b2);


      printf("%d + %d (base%d) = %d + %d = %d (base%d)\n", n1, n2, b1, num1, num2, newNum, b2);
    }

  } while (sign != '$');
}

int baseConversion(int n, int b1, int b2){
  int conversion, number;
  for (int i = 0; n > 0; i++)
  {
    conversion = n % b2;
    n /= b2;

    number = conversion * (int) pow(b1,i);
  }

  return number;

}