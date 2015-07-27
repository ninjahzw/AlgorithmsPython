#include <iostream>
#include <assert.h>
#include <map>
#include <vector>
#include <unistd.h>
using namespace std;

int main(){
    std::string a("a");
    a << "_" << "b";
    cout << a << endl;
}
