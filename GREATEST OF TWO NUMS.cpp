#include<stdio.h>
#include<conio.h>
void great (int a,int b)
{
	if(a>b)
printf("\n A is greater Number.");
else
printf("\n B is greater Number.");
        }
          int main ()
        {
	int a,b;
	printf("Enter two numbers:");
	scanf(" %d %d", &a,&b);
	great(a,b);
	getch();
	return 0;	
        }
