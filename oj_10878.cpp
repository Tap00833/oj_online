#include<stdio.h>
 
static char s[64];
 
int main(){
    unsigned int i;
    unsigned sum, found;
 
    while(gets(s)){
        unsigned int bit = 128;     /* Since the binary form is 8 characters long ( not including . or | ) 2^7 = 128 ( 7 but not 8 starts from 0. 2^0....2^7 total 8 digits ) we keep left shifting and adding only if we find a hole */
 
        i = sum = found = 0;
        if(s[i] != '|') continue;   /* We don't want to print anything for lines not starting with | */
 
        for(; s[i]; ++i){
            if(s[i] == ' ')
                bit >>= 1;          /* keep shifting bits right ( makes them smaller. Ex, 128 = 2^7. So, 128 >> 1 = 64, 2^7 >> 1 = 2^6 = 64 ) OR, you can shift bits to left make them bigger but then you have search the string in reverse order */
            else if(s[i] == 'o'){
                sum += bit;         /* Add the bits where we find a hole */
                bit >>= 1;
            }
        }
 
        printf("%c", sum);          /* Print the sum. No need to print newline. The last line of tape represents a newline character |    o. o | */
    }
    return 0;
}