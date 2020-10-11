
def check_palin(x):
  k= x[::-1]
  if(x==k):
      return 1
  else:
      return 0
x=input("Enter a word")
out=check_palin(x)
if(out==1):
    print(x," is a palindrome")
else:
    print(x," is not a palindrome")