//multiple inheritance acheived throuh interface

interface Printable
{
void print();
}

interface Drawable
{
void draw();
}

class Circle implements Printable,Drawable

{
public void print()
{
System.out.println("Print Circle");
}
public void draw()
{
System.out.println("draw Circle");
}
}

class Demo
{
public static void main(String...a)
{
Circle c=new Circle();
c.print();
c.draw();

}
}