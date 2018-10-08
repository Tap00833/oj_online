#include <iostream>
#include <string>
using namespace std;

bool adjMat[26][26]; 

void findNei(){
    for (int k = 0; k < 26; k++)
         for (int i = 0; i < 26; i++)
             for (int j = 0; j < 26; j++)
                 adjMat[i][j] |= adjMat[i][k] && adjMat[k][j];
}
int main(){
    int m,n;
    while (cin>>m>>n){
        for(int i=0;i<26;i++){  // begin of each case just set up a new adjMat with diagonal ==1 
            for(int j=0;j<26;j++){
                adjMat[i][j]=i==j;
            }
        }
        

        while(m--){
            //set up of the node relationship 
            char x,y;
            cin>>x>>y;
            adjMat[x-'a'][y-'a']=true;
        }
        
        findNei();
        //？？find the relationship who is the neithbor of who 

        while(n--){
            string wr1,wr2;
            cin>>wr1>>wr2;
            //cout<<wr1<<wr2;
            bool ok=wr1.length()==wr2.length();
            if(!ok){
                cout<<"no"<<endl;
            } // if they are same length and all char should be same             
            if(ok){
                for(int x=0;x< wr1.length();x++){
                    ok &= adjMat[wr1[x]-'a'][wr2[x]-'a'];
                }
            cout << (ok ? "yes" : "no") << endl;

            }
        }

    }




    return 0;
}