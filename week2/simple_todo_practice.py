# simple_todo_practice.py
def add_task(text):
    with open("todo.txt", "a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

def list_tasks():
    try:
        with open("todo.txt", "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                print(i, "-", line.strip())
    except FileNotFoundError:
        print("No tasks yet.")

# Demo interaction (run to try)
add_task("Buy milk")
add_task("Do Python practice")
print("--- Current tasks ---")
list_tasks()
