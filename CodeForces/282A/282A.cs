using System;
using System.Text.RegularExpressions;
 
public class Test
{
	public static void Main(string[] args)
	{
		// your code goes here
		int reps = Convert.ToInt32(Console.ReadLine());
		int x = 0;
		string s;
		for( int j = 0 ; j < reps ; j++){
		s=Console.ReadLine();    
		if (s=="++X" || s=="X++"){
		 x++;   
		    
		}
		else{
		    x--;
		    
		}
		}
		
		
		Console.WriteLine(""+x);
}
}