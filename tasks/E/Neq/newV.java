public class newV{
    public static double snippet(double a, double b) {
        if (b >= 0){
            a = -a;//change
            if (a >= 0)
                return a;
            else
                return 0;//change
        }
        else {
            if (a >= 0 && b>=0) //change
                return -a;
            else
                return a;
        }
    }
}
