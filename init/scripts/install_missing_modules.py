import subprocess
import sys

def install_if_missing(module_name):
    try:
        __import__(module_name)
        print(f"✅ {module_name} is already installed.")
    except ImportError:
        print(f"📦 Installing {module_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

def main():
    with open("pythonDependencies.txt", "r") as file:
        modules = [line.strip() for line in file if line.strip()]
    
    for module in modules:
        install_if_missing(module)

if __name__ == "__main__":
    main()
