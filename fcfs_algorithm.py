cur_time = 0
num_processes_done = 0
wait_queue = Queue()
cur_pid = None

# Copy and paste tempalte code here
while num_processes_done < processes.shape[0]:
    # Check if current process finished
    if cur_pid is not None:
        if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
            # Step 1 code goes here
            processes.loc[cur_pid, "End"] = cur_time
            cur_pid = None
            num_processes_done += 1

    # Handle arriving processes
    # Step 2 code goes here
    # Get all rows from processes with an arrival time equal to cur_time
    ready_processes =processes[processes["Arrival"] == cur_time]
    # Add the pid of each process in ready_processes to wait_queue
    for pid, _ in ready_processes.iterrows():
        wait_queue.enqueue(pid)

    # Assign a process to the processor
    if cur_pid is None and len(wait_queue) > 0:
        # Step 3 code goes here
        # Get and remove the ID of the process at the front of the queue
        cur_pid = wait_queue.dequeue()
        processes.loc[cur_pid, "Start"] = cur_time

    cur_time += 1
    
print(processes.head())


# calculating wait times
processes["Wait"] = processes["Start"] - processes["Arrival"]
average_wait_time = processes["Wait"].mean()
print(average_wait_time)

# calculating Turnaround times
processes["Turnaround"] = processes["End"] - processes["Arrival"]
average_turnaround_time = processes["Turnaround"].mean()
print(average_turnaround_time)
