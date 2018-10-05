#include<stdio.h>

static char s[64];


int asiccT(char s[]){
    int bic=1;
    int num=0;
    for(int i=9;i>=1;i--){
        if(s[i]=='o'){
            num+=bic;
            bic*=2;
        }
        else if(s[i]==' '){
            bic*=2;
        }
    }
    return num;
}

int main(){
    
    while(gets(s)){
        if(s[0]=='-'){continue;}
        int asc_num=asiccT(s);  
        printf("%c",asc_num);    
    
    }
    
    /* code */
    return 0;
}