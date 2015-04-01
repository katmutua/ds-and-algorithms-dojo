package arrays;

public class ReverseString {

    public static boolean uniqueValues(String str) {
        boolean[] charset = new boolean[256];

        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (charset[val]) return false;
            charset[val] = true;
        }
        return true;
    }

    public static void test() {
        String lol = "aol";
        int str = 1 << lol.charAt(0);
        System.out.println(str);
    }

    public static void main(String[] args) {
        System.out.println(uniqueValues("haha"));
        test();
    };
};

