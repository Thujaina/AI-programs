# stack_demo.py
stack = []

def push(val):
    stack.append(val)
    print(f"Pushed {val}")

def pop():
    if not stack:
        return "Stack is empty"
    return f"Popped {stack.pop()}"

push(10)
push(20)
print(pop())
print(pop())
print(pop())