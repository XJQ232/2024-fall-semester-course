str = input().split(' ')
n= int(str[0]);m=int(str[1])
str2=input().split(' ')
ak=0
for i in range(n):
    if(int(str2[i]) == 0):
        print(i)
        exit()
    if i+1==m:
        ak=int(str2[i])
    if ak > int(str2[i]):
        print(i)
        exit()
print(n)
# #include <stdio.h>
# #include <stdlib.h>
# int main(){
#     int n,k;
#     scanf("%d %d", &n, &k);
#     int curr, ak=0;
#     for(int i=0;i<n;i++){
#         scanf("%d", &curr);
#         if (curr==0){
#             printf("%d", i);
#             exit(0);
#         }
#         if (k==(i+1)){
#             ak=curr;
#         }
#         if (curr<ak){
#             printf("%d", i);
#             exit(0);
#         }
#     }
#     printf("%d", n);
#     return 0;
# }