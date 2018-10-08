#include<stdio.h> 
#include <iostream>
using namespace std;
 
int main() {
    int caseNum;
    scanf ("%d", &caseNum);
    int i = 0;
 
    while ( i< caseNum ) {
        int n, k, p,ans;
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