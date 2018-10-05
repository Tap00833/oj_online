#include <iostream>
using namespace std;

 
int main() {
    int caseNum;
    cin >> caseNum:
    int i = 0;
    while ( i< caseNum ) {
        cin >> n;
        int l[501]
        for(int x=0;x<n;x++)){
            cin >> l[x];
            

        }


        int n, k, p, ans;
        scanf ("%d %d %d", &n, &k, &p);
        ans=(k+p)%n;
        if(ans==0){
            ans=n;
        }
        i+=1;
        printf ("Case %d: %d\n", i, ans);
    }
 
    return 0;
}


main() {
    int kase, i, j, n, a[505], sum, ans;
    cin >> kase;
    while (kase--) {
        cin >> n;
        for (i=0; i<n; i++)
            cin >> a[i];
        sort(a, a+n); ans = INF;
        for (i=0; i<n; i++) {
            sum = 0;
            for (j=i+1; j<n; j++)
                sum += a[j]-a[i];
            for (j=0; j<i; j++)
                sum += a[i]-a[j];
            if (sum<ans) ans = sum;
        }
        cout << ans << endl;
    }
}