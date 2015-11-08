#include <memory>
#include <vector>

enum Color { WHITE=1, GRAY=2, BLACK=3 };

class Node {
 public:
  Node(int value, Color color = Color::WHITE);
  int value;
  Color flag;
  int weight;
  // Node next;
  std::vector<std::shared_ptr<Node>> neighbors;
  static std::shared_ptr<Node> constructGraph();
};
