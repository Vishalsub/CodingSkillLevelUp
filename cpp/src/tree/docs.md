# 🌳 Binary Tree Problem-Solving Templates in C++

---

## ✅ Core Tree Traversals (DFS)

### Pre-Order (Root → Left → Right)

---

```cpp
void preOrder(TreeNode* Node){
    if(!Node) return nullptr;
    process(Node->value); 
    preOrder(Node->left);
    preOrder(Node->right);
}

```

Do before children
Visit node before going down

### Use Cases:
Clone/copy trees
Serialize trees (DFS-based)
Tree building where root must be processed first
Prefix expression parsing

---

### In-Order (Left → Root → Right)

```cpp

void inOrder(TreeNode* Node){
    if(!Node) return nullptr;
    inOrder(Node->left);
    process(Node->val); // visit between children
    inOrder(Node->left);

}
```
Do between children : Visit node after left, but before right

### Use Cases:
In a Binary Search Tree (BST), it gives sorted order
Kth smallest element in BST
BST validation
Recursive conversion to sorted array

---




### Post-Order (Left → Right → Root)
```cpp
void preOrder(TreeNode* Node){
    if(!Node) return nullptr;
    preOrder(Node->left);
    preOrder(Node->right);
    process(Node->value);

    
}

```

Do after children
Visit node only after both children

### Use Cases:

Delete tree / free memory
Subtree evaluation (e.g., max depth, max path sum)
Problems that rely on bottom-up computation

---

# 🧠 DFS Traversal Summary for Binary Trees

## 📚 DFS Orders Explained

| Order      | Process Root       | Use Case Examples                                             |
|------------|--------------------|----------------------------------------------------------------|
| Pre-order  | Before children     | Serialization, Cloning, Tree building from traversal          |
| In-order   | Between children    | BST operations, Sorted output                                 |
| Post-order | After children      | Tree deletion, Bottom-up DP, Max path sum                     |

---

## 🤔 When to Use What?

| Scenario                                      | DFS Order             |
|-----------------------------------------------|------------------------|
| Want to process parent before children         | Pre-order              |
| Want sorted order from a BST                  | In-order               |
| Want to process children before parent         | Post-order             |
| Computing max depth, height, etc.              | Post-order             |
| Building tree from preorder + inorder          | Preorder + Inorder     |
| Finding max path sum or leaf path totals       | Post-order             |

---

## 🧠 Notes

- **Pre-order** is great when you need to record or serialize structure before traversing children.
- **In-order** is the go-to for **BST-based problems** — it guarantees sorted values.
- **Post-order** shines in bottom-up problems like calculating **height**, **max gain**, or **subtree-based computations**.



---

### 🚀 General DFS with Return

```cpp

void dfs(TreeNode* node){
    if(!node) return nullptr;
    int left = dfs(node->left);
    int right = dfs(node->right);
    return max(left, right) + 1;
}

```
---

### 🔁 Level Order Traversal (BFS)
```cpp
void levelOrder(TreeNode* root) {
    queue<TreeNode*> q;
    q.push(root);
    while(!q.empty()){
        int s = q.size()
        for(int i = 0; i < s; i++){
            TreeNode* node = q.front(); q.pop();
            // process(root->val);
            if(node->left) q.push(node->left);
            if(node->right) q.push(node->right);
        }
    }
} 

```

### 🧠 Kth Smallest in BST
```cpp

```

---


### ⚖️ Validate BST (Min/Max Range Check)

```cpp

bool isValid(TreeNode* node, long minVal, long maxVal) {
    if (!node) return true;
    if (node->val <= minVal || node->val >= maxVal) return false;
    return isValid(node->left, minVal, node->val) &&
           isValid(node->right, node->val, maxVal);
}

```

### 🧭 Lowest Common Ancestor (General Tree)

```cpp

TreeNode* LCA(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left = LCA(root->left, p, q);
    TreeNode* right = LCA(root->right, p, q);
    return !left ? right : !right ? left : root;
}
```

### 🛠 Construct Tree from Preorder + Inorder

```cpp
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
```

### 📦 Serialize / Deserialize Binary Tree (Preorder + Null Marker)

```cpp
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

---

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
