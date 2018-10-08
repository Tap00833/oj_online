#include <stdio.h>


int main() {
	int caseNum;
	int l,w,h;

	scanf("%d",&caseNum);
	for(int i=1;i<=caseNum;i++){
		scanf("%d %d %d",&l,&w,&h);
		printf("Case %d: ",i);
		if(l<=20 && w<=20 && h<=20){
            printf("good\n");
        }
		else{ 
            printf("bad\n");
        }
	}

	return 0;
}