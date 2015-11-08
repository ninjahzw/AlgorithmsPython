#include <iostream>
#include <assert.h>
#include <map>
#include <vector>
#include <unistd.h>
#include <algorithm>

using namespace std;

int main(){
  int SIZE = 10;
  // the two array creations are equivalent
  int a[SIZE];
  int *s = new int[SIZE];
  a[0] = 10;
  int *p = a;
  *p ++;
  *p = 20;
  *p ++;
  *p = 30;
  *p ++;
  *p = 40;
  std::sort(s, s+10);
  std::sort(a, a+10);
  vector<int> v = {3, 2, 1, 4};
  std::sort(v.begin(), v.end(), [&](const int i, const int j){ cout << v[0] << endl; return i > j;});
  for (auto one : v){
	cout << one << endl;
  }

  for (int i = 0; i < SIZE; i++){
	cout << *(s+i) << endl;
	cout << s[i] << endl;
  }

  for (int i = 0; i < SIZE; i++){
	cout << a[i] << endl;
  }
}
