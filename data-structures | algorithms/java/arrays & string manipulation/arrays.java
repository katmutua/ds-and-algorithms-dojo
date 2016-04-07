/*
Check that an array has a certain value
*/

public boolean containsValue(int [] arr, int value) {
   if(arr.length == 0 ) {
   	return false;
   } else{
   	 for(int x =0; x < arr.length; x ++) {
        if(arr[x] == value) {
        	return true;
        }
   	 }
   	 return false;
   }
}

//using an array list

public boolean containsValue(int [] arr, int value) {
   if(arr.length == 0 ) {
   	return false;
   } else{
   	   return true if(Arrays.asList(arr)).containsValue(value));
   	 }
   	 return false;
   }
}

/*
given an array of int primitives and a number, you need to find all pairs in array whose sum is equal to given number 
*/
public String sumOf(int [] arr, int sum) {
    for(int x =0; x < arr.length; x ++) {
        for(int j = 1; j<array.length; j ++) {
        	if (arr[x] + arr[j]) {
        		return arr[x].toString + arr[j].toString
        	}
        }
    }

	return items.toString();
}

/*
remove duplicates in an array
*/

/*
reverse an array 
*/


/*
highest two numbers in an array 
*/

/*
move all zeros to end of an array
*/


/*
find largest integer in an array
*/

/*There is an array with every element repeated twice except one. Find that element?
*/

/*
How to find kth smallest element in unsorted array? 
*/

/*
How to find kth largest element in unsorted array?
*/

/*How to find common elements in three sorted array?
*/

/*
How find the first repeating element in an array of integers?
*/

/*
How to find first non-repeating element in array of integers?
*/

/*
Write a program to find length of longest consecutive sequence in array of integers?
*/

