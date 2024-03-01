#include <stdio.h>

void main() {
  FILE *fptr;
  
  fptr = fopen("input.txt", "r");
  
  char myString[100];
  long ans = 0;
  
  while(fgets(myString, 100, fptr)) {
    int i;
    char s = -1;
    char e;
    char *ptr;
    for (i=0; i<strlen(myString); i++) {
      if (isdigit(myString[i])) {
        if (s == -1) {
          s = myString[i];
        }
        e = myString[i];
      }
    }
    char out[] = "12";
    out[0] = s;
    out[1] = e;
    long ret = strtol(out,&ptr,10);
    ans += ret;
  }
  printf("%ld", ans);
  fclose(fptr);
}