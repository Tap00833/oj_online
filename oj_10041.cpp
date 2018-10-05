#include <iostream>
using namespace std;
 


void nSort(int n,int s[]){ // selection sort 
int i,k,j ;
    for(i=0;i<n-1;i++){ // 对每一个跑一圈
        for(j=i+1,k=i;j<n;j++){
            if(s[j]<s[k]){ //k is the index of min num
                j=k;
            }
        }
        int t;  // exchange the min num and the first index   
        t=s[i];
        s[i]=s[k];
        s[k]=t;       
    }
}

void disCount(int medium,int n, int s[]){
    int sumDis=0 ,i;
    for(i=0;i<n;i++){
        sumDis+=abs(s[i]-s[medium]);
        }
    cout<<sumDis<<endl; 
}

int main() {
    int caseNum;
    cin >> caseNum;
    int i = 0;
 
    while ( i< caseNum ) { // in each case 
        int r;    //親戚數量
        cin>>r;
        int s[500];    //每個親戚的門牌號碼，上限500人 
        for(int j=0;j<r;j++){
            cin>>s[j];
            }
        nSort(r,s);

    int medium;
    if(r%2==1){
        medium=(r+1)/2-1;
    }    
    if (r%2==0){
        medium=r/2;
    }
    disCount(medium,r,s);
    }
 
    return 0;
}
