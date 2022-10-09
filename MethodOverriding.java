class Vehicle
{
void run()
{
System.out.println("Vehicle is running");
}
void run(int x)//method overloading
{
System.out.println("Vehicle is running at speed of "+x);
}
}
class Bike extends Vehicle
{
void run()//method overrriding
{
System.out.println("Bike is running safely");
}
}

class MethodOverriding6
{
public static void main(String...args)
{
Bike b=new Bike();
b.run();
b.run(75);

}
}

