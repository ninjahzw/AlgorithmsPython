#include <iostream>
//global variable
int g_One=1;
//function prototype

void func(int* pInt);

void add_one_1(int n){n += 1;}
void add_one(int& n) { n += 1; }
void add_one(int* const n) { *n += 1; }
int main() {
  int a = 0;
  add_one(a); // not clear that a may be modified
  std::cout << a;
  add_one(&a); // a is clearly being passed destructively
  std::cout << a;
  add_one_1(a);
  std::cout << a;
}


void func(int* pInt)
{
  pInt=&g_One;
}

