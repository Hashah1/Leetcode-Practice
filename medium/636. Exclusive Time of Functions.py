class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        TimeComplexity: N
        SpaceComplexity: N
        Iterate over the logs
        Have a reesults list indexed by function id
            For each log, increment the time at idx = function_id
        """
        exec_times = [0 for i in range(n)]
        stk = []
        # Get the first log and add it's ID to the stack
        first_log = logs[0].split(":")
        f_id = int(first_log[0])
        stk.append(f_id)
        # Set the prev timestamp
        prev_ts = int(first_log[2])
        # Start from second element.
        i = 1
        while i < len(logs):
            # Get the log
            tokens = logs[i].split(":")
            id_, status, timestamp = int(tokens[0]), tokens[1], int(tokens[2])
            # Add element if stk is empty
            if status == "start":
                # Update prev id's exec time
                if stk:
                    # Update the prev id's exec time
                    exec_times[stk[-1]] += timestamp - prev_ts
                # Add the current function's id to the stack.
                stk.append(id_)
                prev_ts = timestamp
            else:
                # If an end is found, then pop off the prev function
                prev_id = stk.pop()
                exec_times[prev_id] += timestamp - prev_ts + 1
                # Update the prev timestamp
                prev_ts = timestamp + 1
            i += 1
        return exec_times

