//implementation of get() in hashmap
import java.util.*;
class MapGet2
{
public static void main(String...a)
{
Map<Integer,String>m=new HashMap<Integer,String>();
m.put(10,"Lovely");
m.put(20,"Professional");
m.put(30,"Universitry");
m.put(40,"Welcomes");
m.put(45,"YOU");
//m.clear();
m.remove(45);
System.out.println(m);

System.out.println("Value of 20 is"+m.get(20));
}
}