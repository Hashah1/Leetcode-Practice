class Solution(object):
    def reorderLogFiles(self, logs):
        def reorder(log):
            # Get the id and the body of the log string
            log_id, log_body = log.split(" ", 1)
            # If string is an alpha, put it into the tuple with prefix 0,
            # so it can be sorted/placed before numeric logs.
            return (0, log_body, log_id) if log_body[0].isalpha() else (1,)
        # Sort based off the tuples returned
        return sorted(logs, key = reorder)
if __name__ == "__main__":
    a = Solution()
    a = a.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
    pass