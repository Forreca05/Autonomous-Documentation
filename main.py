main_content = '''import config
import task_manager  # Assuming task_manager.py exists in the same directory

def load_configurations():
    print("Loading configurations...")
    print(f"Task Storage URL: {config.TASK_STORAGE_URL}")
    print(f"Log File Path: {config.LOG_FILE_PATH}")

def initialize_storage():
    print("Initializing task storage...")    
    # Placeholder for actual initialization logic
    # task_manager.initialize_storage(config.TASK_STORAGE_URL)
 
def display_menu():
    print("Welcome to the Task Manager")   
    print("1. View Tasks")
    print("2. Add Task") 
    print("3. Exit")    
   
def main():
    load_configurations()
    initialize_storage()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            task_manager.view_tasks()
        elif choice == "2":
            task_manager.add_task()
        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
'''

# Write the contents to respective files
with open("utils.py", "w") as f:
    f.write(utils_content)

with open("config.py", "w") as f:
    f.write(config_content)

with open("main.py", "w") as f:
    f.write(main_content)

print("Files utils.py, config.py, and main.py have been created successfully.")

