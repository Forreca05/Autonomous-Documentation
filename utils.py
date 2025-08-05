
# Create utils.py with utility functions
utils_content = '''import datetime

def format_date(date_obj, format="%Y-%m-%d"):
    """Format a datetime object into a string."""
    return date_obj.strftime(format)

def validate_input(data, expected_type):
    """Validate if the data is of the expected type."""
    return isinstance(data, expected_type)

def create_error_message(message):
    """Create a formatted error message."""
    return f"Error: {message}"
'''

# Create config.py with application configurations
config_content = '''# Configuration settings

# URL for the task storage
TASK_STORAGE_URL = "sqlite:///tasks.db"

# API key for external services (if applicable)
API_KEY = ""

# Path to the application log file
LOG_FILE_PATH = "./logs/app.log"
'''
