class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ConstructBinaryTree:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node

    def buildTree(self,preorder, inorder):
        return self.buildTreeRec(preorder,0,len(preorder) - 1, inorder,0,len(inorder) - 1)

    def buildTreeRec(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        pivot = -1
        for i in range(inStart, inEnd + 1):
            if inorder[i] == root.val:
                pivot = i

        if pivot == -1:
            return None

        root.left = self.buildTreeRec(preorder,
                                      preStart + 1,
                                      preStart + (pivot - inStart)
                                      , inorder, inStart ,pivot -1)

        root.right = self.buildTreeRec(preorder,
                                       preStart + (pivot - inStart) + 1,
                                       preEnd,inorder, pivot + 1, inEnd)

        return root

if __name__ == '__main__':
    node = ConstructBinaryTree().buildTree([1,2,5,4,3],[1,2,3,4,5])
    print node