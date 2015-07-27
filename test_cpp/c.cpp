#include <iostream>
#include <assert.h>
#include <map>
#include <vector>
using namespace std;

int main(){
    map<int, vector<int> > a;
    a[1].push_back(1);
    cout << a[1][0] << endl;
    
    int x = 1;
    int &y = x;
    assert(&x == &y);

    int o = 1;
    int p = o;
    assert(p == o);
    assert(&p != &o);

     
    //a[1] = 2;
    //cout << a[1] << endl;
    //if (!a[1]){
    //    a[1] = 3;
    //} else {
    //    a[1] = 4;
    //}
    //cout << a[1] << "\n";
    //for (auto& kv : a){
    //    cout << kv.first << " " << kv.second << "\n";   
    //}

    //vector<int> b;
    //b.push_back(1);
    //cout << b[0] << endl;
    //int* pvar=&nvar;
}
