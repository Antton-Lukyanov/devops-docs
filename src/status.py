"""Module providing a status function."""

def get_status():
    """Return the current system status."""
    temp_variable = 42  # Эта переменная вызовет ошибку Pylint
    return "System is operational"

if __name__ == "__main__":
    print(get_status())