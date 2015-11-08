/**
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Solution:
hashtable. also can use sort.
*/

#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
 public:
  bool isAnagram(string s, string t) {
    std::unordered_map<char, int32_t> ana;
    for (auto& one : s){
      auto iter = ana.find(one);
      // not found
      if (iter == ana.end()){
        ana[one] = 1;
      } else {
        ana[one] += 1;
      }
    }
    for (auto& one : t){
      auto iter = ana.find(one);
      if (iter == ana.end()){
        return false;
      }
      if (iter->second == 0){
        return false;
      }
      ana[one] -= 1;
    }
    // check remaining
    for (auto& kv : ana){
      if (kv.second > 0){
        return false;
      }
    }
    return true;
  }
};

int main(){
  Solution s;
  auto&& res = s.isAnagram("ab", "a");
  cout << res << endl;
}
