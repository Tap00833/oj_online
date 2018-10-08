#include <iostream>
using namespace std;


int main() {
    int caseNum;
    cin >> caseNum;
    cout<<"case number :"<<caseNum<<endl;

    int d[501];
    for(int i=0;i<caseNum;i++){
        int r;    //親戚數量
        cin>>r;
        cout<<"number of rel: " <<r<<endl;
        int s[30001]; 
        for(int j=0;j<r;j++){
            cin>>s[j];
            cout<<s[j];
        }
        cout<<endl;
    }

    //cout<<"i am a pig"<<endl;
    return 0;

}
