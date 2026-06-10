import datetime

def main():
    print("=== DevOps Phone Practice ===")
    print(f"Current time: {datetime.datetime.now()}")
    print("First script complete - automation started")
    
    # Simple example automation
    tasks = ["Health check", "Backup", "Deploy"]
    for task in tasks:
        print(f"✓ {task} task logged")

if __name__ == "__main__":
    main()
