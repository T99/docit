#### `DoublyLinkedListNode`

A doubly-linked node within a {@link DoublyLinkedList}. 

```typescript
class DoublyLinkedListNode<E> implements IDoublyLinkedListNode<E> { ... }
```

---

#### `previous`

A reference to the node preceding this node, or undefined if this node has no preceding sibling.

```typescript
private previous: DoublyLinkedListNode<E> | undefined;
```

---

#### `next`

A reference to the node succeeding this node, or undefined if this node has no successive sibling.

```typescript
private next: DoublyLinkedListNode<E> | undefined;
```

---

#### `parentList`

A reference to the {@link DoublyLinkedList} to which this node belongs.

```typescript
private parentList: DoublyLinkedList<E>;
```

---

#### `content`

The content that this node contains.  This will always be null for the prologue and epilogue nodes in any given {@link DoublyLinkedList}.

```typescript
private content: E | null;
```

---

#### `constructor`

Initializes a new DoublyLinkedListNode with the provided contents, parent list, and optional preceding and successive nodes. 

**Parameters**:
 - **content** The content to initialize this node with.
 - **parentList** The {@link DoublyLinkedList} that contains this node.
 - **previousNode** The node that should be set as this node's preceding sibling.
 - **nextNode** The node that should be set as this node's successive sibling.

```typescript
public constructor(content: E | null, parentList: DoublyLinkedList<E>, previousNode?: DoublyLinkedListNode<E>,nextNode?: DoublyLinkedListNode<E>) { ... }
```
