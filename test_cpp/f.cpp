#include <iostream>
#include <assert.h>
#include <map>
#include <vector>
#include <unistd.h>
using namespace std;

void change (int& a){
    a = 3;    
}

int main(){
    int a = 1;
    map<string, int> m;
    m["a"] = 1;
    const int int_ = 3;
    m["b"] = int_;
    change(m["a"]);
    cout << m["a"] << endl;


    const string s = "";
    s = " 1234 ";
    cout << s << endl;
}
