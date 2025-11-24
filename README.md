# Medicine Reminder & Dosage Tracker

**Domain:** Healthcare & Personal Utility  
**Course:** Vityarthi Python Programming  
**Author:** Rahul Priyadarshi

---

## Phase 1: Problem Definition

### Real-World Problem
Patients and elderly people often forget to take their medicines on time or get confused about the correct dosage. Missed doses can lead to health complications and slower recovery.

### Objective
To develop a user-friendly Command Line Interface (CLI) application that allows users to schedule their medication, view their daily list, and receive real-time alerts when it is time to take a specific dosage.

---

## Phase 2: Requirement Analysis
To solve this problem, the system requires the following features:

1. **Input Mechanism:** Users must be able to input Medicine Name, Dosage, and Scheduled Time.
2. **Storage:** The system must store multiple medicines in a list/dictionary structure.
3. **Real-Time Monitoring:** The system must continuously check the current system time against the scheduled times.
4. **Alert System:** A clear visual alarm must trigger when the time matches.
5. **Error Handling:** The program must allow the user to stop the tracker safely without crashing (using `CTRL+C`).

---

## Phase 3: Top-Down Design (Modularization)
The code is organized into specific functions:

* `add_medicine()`: Captures user input and appends it to the medicine list.
* `show_list()`: Iterates through the stored data to display a formatted schedule.
* `start_alert_system()`: The core engine that runs an infinite loop to compare system time with medicine times.
* `main block`: Handles the menu navigation.

---

## Phase 4: Algorithm Development (Pseudocode)

```text
START
  Initialize empty list 'my_medicines'
  LOOP forever:
    Display Menu (1. Add, 2. View, 3. Start, 4. Exit)
    
    IF Choice is 1 (Add):
      Input Name, Dosage, Time
      Store in Dictionary -> Append to List
      
    ELSE IF Choice is 2 (View):
      Print all items in 'my_medicines'
      
    ELSE IF Choice is 3 (Start Tracker):
      TRY:
        LOOP forever (while True):
          Get Current Time (HH:MM)
          FOR each medicine in list:
            IF medicine_time matches current_time:
              PRINT "ALARM"
              WAIT 60 seconds (to avoid repeat)
          WAIT 1 second
      CATCH KeyboardInterrupt:
        PRINT "Stopping Tracker..."
        
    ELSE IF Choice is 4:
      Break Loop
  END LOOP
STOP
```
### Phase 5: Implementation
---
The source code for this project is written in Python and uses the datetime and time libraries for precise scheduling.
The code is in "vityarthi_projet.py" file attached in this github

### Phase 6: Testing
---
Test Case 1: Adding Data
Input: Name: "Paracetamol", Dosage: "500mg", Time: "14:00"

Result: Data is saved and displayed correctly in the "View List" option.

Test Case 2: The Alert
Action: Set a medicine time to 1 minute from now. Select "Start Tracker".

Result: When the system clock hits that minute, the "ALARM" message prints with the correct dosage.

Test Case 3: Stopping the Tracker
Action: While the tracker is running, press CTRL+C.

Result: The program catches the interrupt and returns to the main menu instead of crashing with a red error message.
### Note: the screenshot of output  is added in screenshot.md file
