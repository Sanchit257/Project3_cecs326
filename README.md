# Banker’s Algorithm Simulation (CECS 326 – Project 3)

## Author
Sanchit Kaushik  
ID: 032434634  

## Description
This project implements the Banker’s Algorithm in Python to simulate resource allocation in an operating system while avoiding deadlocks. The program determines whether the system is in a safe state and handles resource requests from processes.

The implementation includes:
- Available vector
- Maximum matrix
- Allocation matrix
- Need matrix (calculated as Max − Allocation)

---

## Requirements
- Python 3.x
- No external libraries required

---

## How to Run

1. Download the file:
   - bankers.py

2. Open a terminal in the directory containing the file.

3. Run the program:
   python bankers.py

---

## Program Behavior

The program will:

1. Print the initial system state:
   - Available resources
   - Max matrix
   - Allocation matrix
   - Need matrix

2. Run test cases:

### Test Case 1: Safety Check
- Verifies if the system is in a safe state
- Outputs a safe sequence if one exists

### Test Case 2: Valid Resource Request
- Process 1 requests [1, 0, 2]
- Should be granted if the system remains safe

### Test Case 3: Invalid Resource Request
- Process 4 requests [3, 3, 1]
- Should be denied due to insufficient resources

### Additional Test
- Process 0 requests [0, 2, 0]

---

## Notes
- The program follows the Safety Algorithm and Resource-Request Algorithm
- Output is printed directly to the console
- No extra output beyond required results