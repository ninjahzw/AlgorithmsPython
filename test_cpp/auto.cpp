#include <iostream>
#include <assert.h>
#include <map>
#include <vector>
#include <unistd.h>
#include <algorithm>

using namespace std;

/**
 * Function of return type as auto
 * similar to templates
 */
auto func(){
  return 1;
}

int main() {
  auto func_ptr = [](const auto& arg1, const auto& arg2){
	cout << arg1 + arg2 << endl;
  };
  func_ptr(1, 2);

  // NOTE, below yields compile error. (at compile time of course)
  // func_ptr("a", "b");

  cout << func() << endl;
}
