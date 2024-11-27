import time

def shutdown():
  confirm = input("Are you sure you want to shut down? (yes/no): ")
  if confirm.lower() == "yes":
    print("System is shutting down...")
    time.sleep(2)  # Simulate shutdown process
    print("System shutdown complete.")
    exit()
  else:
    print("Shutdown canceled.")

# Call the shutdown function
shutdown()