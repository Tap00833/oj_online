#include<stdio.h>

void dicco(char xxx[],int xd){
    int coNum;
    coNum=(xxx[0]-'A')*26*26+(xxx[1]-'A')*26+(xxx[2]-'A')-xd;
    if(coNum<100 and coNum>(-100)){
        printf("nice\n");
    }
    else{
        printf("not nice\n");
    }
}

int main(){
    char xxx[4];
    int caseNum,xd;
    scanf("%d",&caseNum);
    while(caseNum--){
        scanf("%3s-%d",xxx,&xd);
        dicco(xxx,xd);
        
    }
    return 0;   
}