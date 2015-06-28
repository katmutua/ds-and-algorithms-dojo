package Sorting;

class MergeSort {

    public static void mergeLists(int[] listA, int[] listB){
        int listACapacity = listA.length + listA.length;
        int listALastItemIndex = listA.length  - 1;
        int listBLastItemIndex = listB.length - 1;

        while(listALastItemIndex >=0 && listBLastItemIndex >0){
            if(listA[listBLastItemIndex] > listB[listALastItemIndex]){
               listA[listACapacity--] = listA[listBLastItemIndex];
            }else{
                listA[listACapacity--] = listB[listALastItemIndex];
            }
        }
        while (listBLastItemIndex >=0){
            listA[listACapacity--] = listB[listBLastItemIndex];
        }
        System.out.println(listA.toString());
    }

    public static void main(String [] args) {
        int [] listA = new  int[] {12,34,55,66,777};
        int [] listB = new  int[] {45,67,89,90};

        mergeLists(listA, listB);
    }
}