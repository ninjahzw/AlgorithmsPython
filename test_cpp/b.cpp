#include <iostream>
#include <assert.h>
using namespace std;

int main(){
    int arr[] = {1,2,3};
    std::string s = "aaa";
    std::string nvar=s;
    
    int x = 0;
    int &r = x;
    int *p = &x;
    int *p2 = &r;
    assert(p == p2);
    //int* pvar=&nvar;
}
