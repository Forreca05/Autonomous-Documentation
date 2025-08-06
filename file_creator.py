# file_creator.py

# Conteúdo de utils.py (aqui é só um exemplo simples; modifique conforme necessário)
utils_content = '''def format_task(task):
    return f"- {task}"
'''

# Conteúdo de config.py
config_content = '''# Configurações globais do Task Manager
TASK_STORAGE_URL = "data/tasks.json"
LOG_FILE_PATH = "logs/task_manager.log"
'''

# Conteúdo de main.py
main_content = '''import config
import task_manager  # Certifique-se de que task_manager.py existe

def load_configurations():
    print("Loading configurations...")
    print(f"Task Storage URL: {config.TASK_STORAGE_URL}")
    print(f"Log File Path: {config.LOG_FILE_PATH}")

def initialize_storage():
    print("Initializing task storage...")
    # Aqui você pode adicionar lógica real de inicialização
    # Exemplo: task_manager.initialize_storage(config.TASK_STORAGE_URL)

def display_menu():
    print("\\nWelcome to the Task Manager")
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

# Escrita dos arquivos
with open("utils.py", "w") as f:
    f.write(utils_content)

with open("config.py", "w") as f:
    f.write(config_content)

with open("main.py", "w") as f:
    f.write(main_content)

print("✅ Arquivos utils.py, config.py e main.py foram criados com sucesso.")
