//Check is a string has unique characters is extra buffer 

public boolean isUnique(String word){
        int asciiCharSet[]=new boolean[256];
        for(int x=0;x<word.length;x++){
        int val=word.charAt(x);
        if(asciiCharSet[x])return false;

        asciiCharSet[val]=true;
        }
        return true;
        }

//Check that a string is unique with no extra buffers

public static boolean isUniqueChars(String str){
        int checker=0;
        for(int i=0;i<str.length();++i){
        int val=str.charAt(i)- ‘a’;
        if((checker&(1<<val))>0)return false;
        checker|=(1<<val);
        }
        return true;
        }


//reverse a string

public String reverse(String word){
        StringBuffer buffer=new StringBuffer();
        for(int x=0;x<word.length()-1;x++){
        buffer.append(word.charAt(x));
        }
        return buffer.toString();
        }

//remove duplicates

public String removeDups(String word){
        StringBuffer buffer=new StringBuffer();
        ArrayList<Character>arrList=new ArrayList<>();
        if(word==null||word.length()==1)return word;

        for(int x=0;x<x.length();x++){
        if(!arrList.contains(word.charAt(x))){
        arrList.put(word.charAt(x));
        }
        }

        for(char c:arrList)buffer.append(c);
        return buffer.toString();
        return;
        }

//Parser of a string that checks if opened brackets were correctly closed


