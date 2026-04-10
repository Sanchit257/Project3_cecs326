# by Sanchit Kaushik
# ID:032434634
# date: 4/10/2026

class BankersAlgorithm:
    #initializes the banker's algorithm
    def __init__(self, n , m, available, max_matrix, allocation): 
        self.n = n  # # of processes
        self.m = m  # # of resource types
        self.available = available.copy() #copies available resources
        self.max_matrix = [row.copy() for row in max_matrix]
        self.allocation = [row.copy() for row in allocation]
        
        self.need = self.calculate_need()
    
    def calculate_need(self):
        #calculates need matrix
        need = []
        for i in range(self.n):
            need_row = []
            for j in range(self.m):
                need_row.append(self.max_matrix[i][j] - self.allocation[i][j])
            need.append(need_row)
        return need
    
    def is_safe(self):
        #checks if the system is in a safe state
        work = self.available.copy() #copies available resources
        finish = [False] * self.n #initializes finish array
        safe_sequence = []
        
        #tries to find safe sequence
        while len(safe_sequence) < self.n:
            found = False
            
            for i in range(self.n):
                if not finish[i]:
                    #checks if process i's needs can be satisfied
                    can_allocate = True #initializes can_allocate
                    for j in range(self.m):
                        if self.need[i][j] > work[j]:
                            can_allocate = False 
                            break
                    
                    if can_allocate:
                        #process i can finish, adds its resources back to work
                        for j in range(self.m):
                            work[j] += self.allocation[i][j]
                        
                        safe_sequence.append(i)
                        finish[i] = True
                        found = True
                        break
            
            # system is unsafe if no process could be allocated in this iteration
            if not found:
                return False, []
        
        return True, safe_sequence
    
    def request_resources(self, process_id, request):
        #handles a resource request from a process
        print(f"\nProcess {process_id} requests resources {request}")
        
        #checks if request exceeds need
        for j in range(self.m):
            if request[j] > self.need[process_id][j]:
                print(f"Error: Process has exceeded its maximum claim.")
                return False
        
        #checks if request exceeds available resources
        for j in range(self.m):
            if request[j] > self.available[j]:
                print(f"Error: Not enough resources available.")
                return False
        
        #pretends to allocate resources (save current state)
        original_available = self.available.copy()
        original_allocation = [row.copy() for row in self.allocation]
        original_need = [row.copy() for row in self.need]
        
        #modifies state as if resources were allocated
        for j in range(self.m):
            self.available[j] -= request[j]
            self.allocation[process_id][j] += request[j]
            self.need[process_id][j] -= request[j]
        
        #checks if system remains in safe state
        is_safe, safe_sequence = self.is_safe()
        
        if is_safe:
            print("System is in a safe state.")
            print(f"Safe Sequence: {safe_sequence}")
            print(f"Resources allocated to process {process_id}.")
            return True
        else:
            #restores original state
            self.available = original_available
            self.allocation = original_allocation
            self.need = original_need
            print("System would be in an unsafe state.")
            print(f"Request denied for process {process_id}.")
            return False
    
    def print_state(self):
        #prints current system state
        print("\n-----Current System State-----")
        print(f"Available Resources: {self.available}")
        
        print("\nMax Matrix:")
        for i, row in enumerate(self.max_matrix):
            print(f"Process {i}: {row}")

        print("\nAllocation Matrix:")
        for i, row in enumerate(self.allocation):
            print(f"Process {i}: {row}")
        
        print("\nNeed Matrix:")
        for i, row in enumerate(self.need):
            print(f"Process {i}: {row}")
        print("=" * 30)


#tests the implementation with the given data
if __name__ == "__main__":
    n = 5  # # of processes
    m = 3  # # of resource types
    
    #available vector
    available = [3, 3, 2]
    
    #maximum matrix
    max_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    
        #allocation matrix
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    
    #creates banker's algorithm instance
    banker = BankersAlgorithm(n, m, available, max_matrix, allocation)
    
    #prints initial state
    banker.print_state()

    ###################### test cases ###################################

    #test case 1 runs safe test
    print("Test Case 1: Run safe test")
    is_safe, safe_sequence = banker.is_safe()
    if is_safe:
        print("System is in a safe state.")
        print(f"Safe Sequence: {safe_sequence}")
    else:
        print("System is NOT in a safe state.")
    
    #test case 2 process 1 requests resource
    print("Test Case 2: Process 1 requests [1, 0, 2]")
    request = [1, 0, 2]
    banker.request_resources(1, request)
    
    #test case 3 process 4 requests resource
    print("Test Case 3: Process 4 requests [3, 3, 1]")
    request = [3, 3, 1]
    banker.request_resources(4, request)
    
    #additional test process 0 requests resource
    print("Additional Test: Process 0 requests [0, 2, 0]")
    request = [0, 2, 0]
    banker.request_resources(0, request)