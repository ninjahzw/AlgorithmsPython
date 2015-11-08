#include <iostream>
#include <assert.h>
#include <map>
#include <vector>
#include <unistd.h>
using namespace std;

class Test{
 public:
  Test(int32_t&& a){
  }
};

int main(){
  Test t(1); 
  Test t1 = t;
  std::string a("a");
  int x(10);
  cout << x << endl;
}
