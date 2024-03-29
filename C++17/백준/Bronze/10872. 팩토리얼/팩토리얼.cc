#include <iostream>
using namespace std;
int fac(int a)
{
   if(a==1 || a==0)
   {
      return 1;
   }
   return fac(a-1)*a;
}

int main()
{
   int a;
   cin>>a;
   cout<<fac(a)<<endl;
   return 0;
}