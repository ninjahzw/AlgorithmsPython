#include "Node.h"
#include <iostream>
#include <vector>

using namespace std;

Node::Node(int value, Color color) : value(value),
  flag(color) {
}

shared_ptr<Node> Node::constructGraph(){

  auto n1 = make_shared<Node>(1);
  auto n2 = make_shared<Node>(2);
  auto n3 = make_shared<Node>(3);
  auto n4 = make_shared<Node>(4);
  auto n5 = make_shared<Node>(5);
  auto n6 = make_shared<Node>(6);

  n1->neighbors.push_back(n2);
  n1->neighbors.push_back(n3);
  
  n2->neighbors.push_back(n3);
  n2->neighbors.push_back(n4);

  n3->neighbors.push_back(n5);

  n4->neighbors.push_back(n5);
  n4->neighbors.push_back(n6);

  n5->neighbors.push_back(n6);

  return n1;
}
