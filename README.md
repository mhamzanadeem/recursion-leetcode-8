# Recursion LeetCode Solutions (8 Problems)

All 8 problems solved **recursively**. Each solution identifies the **base case** and **recursive case**.

---

## Problem List

| # | Problem | File | Base Case | Recursive Case |
|---|---------|------|-----------|----------------|
| 509 | Fibonacci Number | `fibonacci_number.py` | f(0)=0, f(1)=1 | f(n) = f(n-1) + f(n-2) |
| 344 | Reverse String | `reverse_string.py` | left >= right | swap, recurse(left+1, right-1) |
| 125 | Valid Palindrome | `valid_palindrome.py` | left >= right | compare ends, recurse inward |
| 231 | Power of Two | `power_of_two.py` | n==1 (yes), n<=0 or odd (no) | recurse(n / 2) |
| 206 | Reverse Linked List | `reverse_linked_list.py` | head is None or single node | reverse rest, attach head at end |
| 24 | Swap Nodes in Pairs | `swap_nodes_in_pairs.py` | head is None or single node | swap pair, recurse on rest |
| 1047 | Remove Adjacent Duplicates | `remove_all_adjacent_duplicates_in_string.py` | len <= 1 | remove first pair, recurse |
| 2095 | Delete Middle Node | `delete_the_middle_node_of_a_linked_list.py` | 0 or 1 node | find middle via count, skip it |

---

## Recursion Tree Drawings

### 1. Fibonacci Number - fib(5)

```
                        fib(5)
                       /      \
                  fib(4)        fib(3)
                 /     \        /     \
            fib(3)   fib(2)  fib(2)  fib(1)
           /    \    /    \    /    \
       fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
       /    \
   fib(1) fib(0)
```

- **Base cases reached:** fib(1)=1 (5 times), fib(0)=0 (3 times)
- **Result:** 5
- **Note:** This tree shows why naive recursion is O(2^n) - repeated subproblems

---

### 2. Power of Two - isPowerOfTwo(16)

```
                isPowerOfTwo(16)
                        |
                isPowerOfTwo(8)
                        |
                isPowerOfTwo(4)
                        |
                isPowerOfTwo(2)
                        |
                isPowerOfTwo(1)  <-- Base Case: returns True
```

- **Base case:** n == 1 returns True
- **Recursive case:** n is even, recurse with n/2
- **Result:** True (16 = 2^4)
- **Time:** O(log n) - halving each step

---

## Reverse Linked List: Recursive vs Iterative Comparison

### Recursive Version
```python
def reverseList(self, head):
    if not head or not head.next:
        return head
    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head
```
- **Time:** O(n)
- **Space:** O(n) - call stack

### Iterative Version
```python
def reverseList(self, head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```
- **Time:** O(n)
- **Space:** O(1) - constant

### Comparison Summary
| Aspect | Recursive | Iterative |
|--------|-----------|-----------|
| Time | O(n) | O(n) |
| Space | O(n) stack | O(1) |
| Readability | Cleaner, elegant | More verbose |
| Risk | Stack overflow on long lists | None |
| Preference | Learning/interviews | Production code |

**Verdict:** Iterative is preferred for production due to O(1) space. Recursive is great for understanding the concept and for interviews.

---

## How to Run

```bash
python fibonacci_number.py
python reverse_string.py
python valid_palindrome.py
python power_of_two.py
python reverse_linked_list.py
python swap_nodes_in_pairs.py
python remove_all_adjacent_duplicates_in_string.py
python delete_the_middle_node_of_a_linked_list.py
```

---

## Acceptance Criteria Checklist

- [x] All 8 problems solved recursively
- [x] Base case and recursive case identified for each problem
- [x] Recursion trees drawn for 2 problems (Fibonacci, Power of Two)
- [x] Reverse Linked List solved both ways with comparison
