# 🌳 Binary Tree Problem-Solving Templates in C++

This repository contains a complete set of **C++ templates** and recall notes for solving common binary tree problems efficiently. Use this as a quick reference when solving problems on LeetCode, HackerRank, or during interviews.

---

## ✅ Core Tree Traversals (DFS)

### In-Order (Left → Root → Right)

```cpp
void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    // process(root->val);
    inorder(root->right);
}
```
### Pre-Order (Root → Left → Right)

```cpp

void preorder(TreeNode* root) {
    if (!root) return;
    // process(root->val);
    preorder(root->left);
    preorder(root->right);
}
```


### Post-Order (Left → Right → Root)
```cpp
void postorder(TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    // process(root->val);
}

```

### 🚀 General DFS with Return

```cpp
int dfs(TreeNode* root) {
    if (!root) return 0;
    int left = dfs(root->left);
    int right = dfs(root->right);
    return max(left, right) + 1;
}
```

### 🔁 Level Order Traversal (BFS)
```cpp
void levelOrder(TreeNode* root) {
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front(); q.pop();
            // process(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
}

🧠 Kth Smallest in BST

void inorder(TreeNode* root, int& k, int& result) {
    if (!root) return;
    inorder(root->left, k, result);
    if (--k == 0) {
        result = root->val;
        return;
    }
    inorder(root->right, k, result);
}
⚖️ Validate BST (Min/Max Range Check)

bool isValid(TreeNode* node, long minVal, long maxVal) {
    if (!node) return true;
    if (node->val <= minVal || node->val >= maxVal) return false;
    return isValid(node->left, minVal, node->val) &&
           isValid(node->right, node->val, maxVal);
}
🧭 Lowest Common Ancestor (General Tree)

TreeNode* LCA(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left = LCA(root->left, p, q);
    TreeNode* right = LCA(root->right, p, q);
    return !left ? right : !right ? left : root;
}
🛠 Construct Tree from Preorder + Inorder

TreeNode* build(vector<int>& preorder, int preStart, int preEnd,
                vector<int>& inorder, int inStart, int inEnd,
                unordered_map<int, int>& inMap) {
    if (preStart > preEnd || inStart > inEnd) return nullptr;

    int rootVal = preorder[preStart];
    TreeNode* root = new TreeNode(rootVal);
    int inRoot = inMap[rootVal];
    int numsLeft = inRoot - inStart;

    root->left = build(preorder, preStart + 1, preStart + numsLeft,
                       inorder, inStart, inRoot - 1, inMap);
    root->right = build(preorder, preStart + numsLeft + 1, preEnd,
                        inorder, inRoot + 1, inEnd, inMap);
    return root;
}
📦 Serialize / Deserialize Binary Tree (Preorder + Null Marker)

void serialize(TreeNode* root, string& data) {
    if (!root) {
        data += "#,";
        return;
    }
    data += to_string(root->val) + ",";
    serialize(root->left, data);
    serialize(root->right, data);
}

TreeNode* deserialize(queue<string>& nodes) {
    string val = nodes.front(); nodes.pop();
    if (val == "#") return nullptr;
    TreeNode* root = new TreeNode(stoi(val));
    root->left = deserialize(nodes);
    root->right = deserialize(nodes);
    return root;
}
```

## 📌 Notes

Prefer DFS (recursive) for structural problems.
Use BFS for level-wise logic or serialization.
Use inorder for anything related to sorted properties (especially in BSTs).
Use hashmap when reconstructing tree from traversal lists.

## 📚 Suggested Practice Order

Invert Binary Tree
Max Depth of Binary Tree
Same Tree / Subtree
Level Order Traversal
Validate BST
LCA
Kth Smallest in BST
Construct from Preorder + Inorder
Serialize/Deserialize
Binary Tree Max Path Sum
