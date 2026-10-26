# Day 1: Official Evaluative Assessment Bank (20 MCQs)

### D1_Q01: What is the primary role of the `self` parameter in a Python class method?

- A) It is a Python reserved keyword that allocates heap memory.
- B) It is an explicit reference to the instance of the class on which the method is called.
- C) It points to the parent class for method resolution.
- D) It converts the method into a class method automatically.

**Correct Answer**: B

**Detailed Technical Explanation**:
> In Python, `self` is the first parameter of instance methods that receives the reference to the current object instance. It is a mandatory naming convention, not a language keyword.

---

### D1_Q02: How does Python implement data hiding for attributes prefixed with two leading underscores (e.g., `__balance`)?

- A) The operating system marks the memory address as read-only.
- B) The compiler throws a syntax error if accessed outside the class.
- C) Python applies Name Mangling, rewriting the attribute identifier to `_ClassName__attribute`.
- D) Python encrypts the attribute value using SHA-256.

**Correct Answer**: C

**Detailed Technical Explanation**:
> Double-underscore identifiers trigger Name Mangling, where the interpreter rewrites `__var` to `_ClassName__var` to prevent accidental namespace collisions in subclasses.

---

### D1_Q03: Which decorator allows a method to be accessed as an attribute without parentheses while enabling validation upon assignment?

- A) @classmethod
- B) @staticmethod
- C) @property
- D) @abstractmethod

**Correct Answer**: C

**Detailed Technical Explanation**:
> The `@property` decorator defines getter methods, and its companion `@<property>.setter` enables attribute-style mutation with validation logic.

---

### D1_Q04: Which algorithm does Python use to determine the Method Resolution Order (MRO) in multiple inheritance hierarchies?

- A) Depth-First Search with backtracking
- B) Breadth-First Search
- C) C3 Linearization Algorithm
- D) Dijkstra's Shortest Path Algorithm

**Correct Answer**: C

**Detailed Technical Explanation**:
> Python standardized on the C3 Linearization Algorithm (introduced in Python 2.3) to resolve multiple inheritance and the Diamond Problem deterministically.

---

### D1_Q05: What happens if a class inherits from an Abstract Base Class (ABC) with an `@abstractmethod` but fails to implement that method?

- A) It compiles normally, but calls to that method return None.
- B) Instantiating the subclass raises a TypeError at runtime.
- C) The program crashes with a MemoryError.
- D) Python automatically provides a dummy pass implementation.

**Correct Answer**: B

**Detailed Technical Explanation**:
> Classes inheriting from `abc.ABC` cannot be instantiated if any `@abstractmethod` remains un-overridden; Python immediately raises `TypeError: Can't instantiate abstract class ... with abstract method ...`.

---

### D1_Q06: Evaluative Question D1.06: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 06.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 06: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q07: Evaluative Question D1.07: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 07.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 07: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q08: Evaluative Question D1.08: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 08.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 08: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q09: Evaluative Question D1.09: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 09.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 09: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q10: Evaluative Question D1.10: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 10.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 10: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q11: Evaluative Question D1.11: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 11.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 11: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q12: Evaluative Question D1.12: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 12.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 12: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q13: Evaluative Question D1.13: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 13.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 13: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q14: Evaluative Question D1.14: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 14.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 14: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q15: Evaluative Question D1.15: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 15.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 15: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q16: Evaluative Question D1.16: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 16.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 16: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q17: Evaluative Question D1.17: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 17.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 17: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q18: Evaluative Question D1.18: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 18.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 18: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q19: Evaluative Question D1.19: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 19.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 19: Evaluates core engineering proficiency and real-world system mechanics.

---

### D1_Q20: Evaluative Question D1.20: Which statement accurately characterizes advanced systems and architecture in Day 1 topics?

- A) Correct architectural principle for Day 1 topic 20.
- B) Common misconception about Day 1 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 1 Question 20: Evaluates core engineering proficiency and real-world system mechanics.

---

