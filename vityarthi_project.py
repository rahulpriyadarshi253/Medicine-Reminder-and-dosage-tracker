import time
import datetime

# --- Vityarthi Project: Medicine Reminder and Dosage Tracker ---
# --- Author: [ Rahul Priyadarshi] ---

my_medicines = []

def add_medicine():
    print("\n--- Add a New Medicine ---")
    name = input("Enter your Medicine Name: ")
    dosage = input("Enter Dosage ")
    alarm_time = input("Enter Time (HH:MM in 24-hour format,): ")
    
    med_details = {
        "name": name,
        "dosage": dosage,
        "time": alarm_time
    }
    my_medicines.append(med_details)
    print(f"Saved! I will remind you to take {name} at {alarm_time}.")

def show_list():
    """Prints all saved medicines."""
    print("\n--- Your Medicine List ---")
    if len(my_medicines) == 0:
        print("No medicines are added yet.")
    else:
        for med in my_medicines:
            print(f"- {med['name']} ({med['dosage']}) at {med['time']}")

def start_alert_system():
    """The main loop that checks the time continuously."""
    print("\n--- Tracker Started (Keep this window open) ---")
    print("Press CTRL+C to stop the program.")
    try:
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            
            for med in my_medicines:
                if med["time"] == now:
                    print("\n" + "#" * 30)
                    print(f" ALARM! Time to take medicine named: {med['name']}")
                    print(f" Dosage: {med['dosage']}")
                    print("#" * 30 + "\n")
                    time.sleep(60) 
            
            time.sleep(1) 
            
    except KeyboardInterrupt:
        
        print("\n\nStopping tracker...")
        print("Returning to Main Menu...")
    
while True:
    print("\n=== REMINDER OF MEDICINE AND DOSAGE TRACKER ===")
    print("1. Add your Medicine")
    print("2. View The List")
    print("3. Start Tracker")
    print("4. Exit")
    
    choice = input("Select an option from (1-4): ")
    
    if choice == "1":
        add_medicine()
    elif choice == "2":
        show_list()
    elif choice == "3":
        start_alert_system()
    elif choice == "4":
        print("Be healthy! Thanks .")
        break
    else:
        print("Your choice is invalid, please try again.")