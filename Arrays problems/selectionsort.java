// selection sort in java

public class selectionsort
{
    void sort(int arr[])
    {
        int n=arr.length;
        for(int i=0;i<n;i++)
        {
            int min_idx=i;
            for(int j=i+1;j<n;j++)
            {
                if(arr[min_idx]>arr[j])
                {
                    min_idx=j;
                }
            }
            //swapping
            int temp=arr[min_idx];
            arr[min_idx]=arr[i];
            arr[i]=temp;
        }
    }
    void print_arr(int arr[]){
        int n=arr.length;
        for(int i=0;i<n;i++)
        {
            System.out.print(arr[i]+ ",");
        }     
           
    }
public static void main (String args[])
{
    int arr[]={4,8,6,9,5,2,1};
    selectionsort so=new selectionsort();
    so.sort(arr);
    so.print_arr(arr);

}
}
