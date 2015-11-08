#include "Node.h"
#include <iostream>
#include <stack>
#include <queue>

using namespace std;

void bfs(shared_ptr<Node>& head){
  queue<shared_ptr<Node>> q;
  q.push(head);
  while (!q.empty()){
	auto node = q.front();	
	if (node->flag == Color::WHITE){
	  cout << node->value << endl;
	  node->flag = Color::BLACK;
	}
	for (auto& one : node->neighbors){
	  q.push(one);
	}
	// remove the element
	q.pop();
  }
}

void dfs(shared_ptr<Node>& head){
  stack<shared_ptr<Node>> s;
  s.push(head);
  head->flag = Color::GRAY;
  while (!s.empty()){
	auto node = s.top();	
	if (node->flag == Color::GRAY){
	  cout << node->value << endl;
	  node->flag = Color::BLACK;
	  s.pop();
	}
	for (auto& one : node->neighbors){
	  if (one->flag == Color::WHITE){
	    s.push(one);
	    one->flag = Color::GRAY;
	  }
	}
  }
}

int main(){
  auto head = Node::constructGraph();
  bfs(head);
  cout << "-------" << endl;
  auto head_dfs = Node::constructGraph();
  dfs(head_dfs);
  return 0;
}
