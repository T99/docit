#### `IContainer`

An interface representing the general form of a data structure that contains elements. 

```typescript
interface IContainer<E> extends Iterable<E>, Streamable<E> { ... }
```

---

#### `#contains`

Returns true if and only if this IContainer contains all of the elements provided as arguments. 

**Parameters**:
 - **elements** The elements to check this container for.

**Returns** true if and only if this IContainer contains all of the elements provided as arguments.

```typescript
contains(...elements: E[]): boolean;
```

---

#### `#size`

Returns the number of elements contained in this IContainer. 

**Parameters**:
 - _None_

**Returns** The number of elements contained in this IContainer.

```typescript
size(): number;
```

---

#### `#isEmpty`

Returns true if and only if this IContainer holds no elements. 

**Parameters**:
 - _None_

**Returns** true if and only if this IContainer holds no elements.

```typescript
isEmpty(): boolean;
```

---

#### `#toArray`

Returns an array representation of the elements contained in this IContainer. 

**Parameters**:
 - _None_

**Returns** An array representation of the elements contained in this IContainer.

```typescript
toArray(): E[];
```

---

#### `#clear`

Removes all of this IContainer's elements, rendering it empty.

**Parameters**:
 - _None_

**Returns** Void.

```typescript
clear(): void;
```
