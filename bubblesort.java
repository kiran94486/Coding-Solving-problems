
public class bubblesort {

    void sort(int arr[])
    {
        int n=arr.length;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n-i-1;j++){
                if(arr[j]>arr[j+1]){

                    int temp=arr[j+1];
                    arr[j+1]=arr[j];
                    arr[j]=temp;

                }
            }
        }

    }
    void print_arr(int arr[])
    {
        int n=arr.length;
        for(int i=0;i<n;i++)
        {
            System.out.print(arr[i]+ ",");
        }

    }

    public static void main(String[] args) {
        int arr[]={64, 34, 25, 12, 22, 11, 90};
        bubblesort bsort=new bubblesort();
        bsort.sort(arr);
        bsort.print_arr(arr);
    }
    
}
