
Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)
   

#using recursion

#include<stdio.h>
int sumdiv(int num, int x);
 
int main()
{
        int num;
        printf("Enter a number :");
        scanf("%d",&num);
        if(sumdiv(num, num/2) == num)
                printf("\nPerfect Number\n");
        else
                printf("\nNot Perfect Number\n");
}
 
sumdiv(int num, int x)
{
        if(x==1)
                return 1;
        if(num%x==0)/*if x is a proper divisor*/
                return x + sumdiv(num,x-1);
        else
                return sumdiv(num,x-1);
}
## this repository contains the basics of python and which will help the users to understand data structures and algorithmms.

    
