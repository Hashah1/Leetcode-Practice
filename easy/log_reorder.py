class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        for log in logs:
            # Get the body of the log minus the id
            log_body = log.split()[1:]
            
            # Check if the log is numeric. Only need to check first char
            # If it is, then append to end of list and delete
            # current index.
            if log_body[0].,,,isdigit()
                
            few