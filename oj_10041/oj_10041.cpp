//
//  main.cpp
//  ojol
//
//  Created by kkwang on 2018/10/4.
//  Copyright © 2018年 kkwang. All rights reserved.
//

#include <iostream>
using namespace std;



void nSort(int n,int s[]){ // selection sort
    int i,k,j ;
    for(i=0;i<n-1;i++){ // 对每一个跑一圈
        for(j=i+1,k=i;j<n;j++){
            if(s[j]<s[k]){ //k is the index of min num
                k=j;
            }
        }
        int t;  // exchange the min num and the first index
        t=s[i];
        s[i]=s[k];
        s[k]=t;
    }
}



int main() {
    int caseNum;
    cin >> caseNum;
    //cout<<"case number :"<<caseNum<<endl;

    int d[501];
    for(int i=0;i<caseNum;i++){
        int r;    //親戚數量
        cin>>r;
        //cout<<"number of rel: " <<r<<endl;
        int s[30001]; 
        for(int j=0;j<r;j++){
            cin>>s[j];
            //cout<<s[j];
        }
        nSort(r,s); // just sort the array from small to large 


        int medium=0;
        if(r%2==1){
            medium=(r+1)/2-1;
        }
        if (r%2==0){
            medium=r/2;
        }

        int sumDis=0 ;
    
        for(int j=0;j<r;j++){
            sumDis+=abs(s[j]-s[medium]);
        }
        
        d[i]=sumDis;
    }

    for (int i=0;i<caseNum;i++)
    {    cout<<d[i]<<endl;    }
    //cout<<"i am a pig"<<endl;
    return 0;

}

