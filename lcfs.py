cur_time = 0
num_processes_done = 0
wait_stack = Stack()
cur_pid = None

while num_processes_done < processes.shape[0]:
    # Step 1 (handle end of the process)
    if cur_pid is not None:
        if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
            processes.loc[cur_pid, "End"] = cur_time
            cur_pid = None
            num_processes_done += 1
    # Step 2 (handle arriving processes)
    ready_processes = processes[processes["Arrival"] == cur_time]
    for pid, _ in ready_processes.iterrows():
        wait_stack.push(pid)

    # Step 3 (assign a process to the processor)
    if cur_pid is None and len(wait_stack) > 0:
        cur_pid = wait_stack.pop()
        processes.loc[cur_pid, "Start"] = cur_time
    cur_time += 1
    
processes.head()

# calculating average wait time
processes["Wait"] = processes["Start"] - processes["Arrival"]
average_wait_time = processes["Wait"].mean()
print(average_wait_time)

# compare maximum wait times
fcfs_max_wait = processes["FCFS Wait"].max()
lcfs_max_wait = processes["Wait"].max()
print(f"fcfs_max_wait:", fcfs_max_wait)
print(f"lcfs_max_wait:", lcfs_max_wait)
# fcfs_max_wait: 570
# lcfs_max_wait: 989.0

# calculating average turnaround time
processes.head()
processes["Turnaround"] = processes["End"] - processes["Arrival"]
average_turnaround_time = processes["Turnaround"].mean()
print(average_turnaround_time)
