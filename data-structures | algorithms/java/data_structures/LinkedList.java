//sum everything keep track of missing indices and return difference
public static int findMissingNumber(int[]arr){
        int sum=0;

        if(arr.length==0){
        return 0;
        }else{
        int index=0;
        for(int x=0;x<arr.length;x++){
        if(arr[x]!=0){
        sum+=arr[x];
        }else{
        index=x;
        }
        }
        System.out.println("Missing number is  on index "+index+" and the values should be:"+(100-sum));
        return sum;
        }
        }

//


public boolean isBalanced(String word){
//assumption: only comprises brackets not any other characters

        if(word==null||word.length()==1){
        return false;
        }

        Stack<Character>stack=new Stack<>();
        char current=' ',previous=' ';

        for(int i=0;i<word.length();i++){
        current=word.charAt(i);
        if(current=='{'||current=='['||current=='('){
        stack.push(current);
        }
        else if(current=='}'||current==']'||current==')'){
        if(stack.isEmpty){
        return false;
        }else{
        previous=stack.peek();
        if(current=='{'&&previous=='}'||current==']'&&previous=='['||current==')'&&previous=='('){
        stack.pop();
        }else{
        return false;
        }
        }
        }
        }
        }

//to improve consider using an arraylist with possible brackets and check for contains
//put matches in stack is in the above algorithmn
//check if stack is still empty


//create a function that finds allthe power sets of a set









