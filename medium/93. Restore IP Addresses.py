class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(indv_ip, idx=0, blk_idx=0):
            # Base case
            if blk_idx == 4:
                if idx == len(s):
                    all_ips.append('.'.join(indv_ip))
                    return True
                elif idx < len(s):
                    # Do not add to all ips
                    return False

            valid = False
            for i in range(idx, idx + 3):
                if i < len(s):
                    indv_ip[blk_idx] += s[i]
                    if (len(indv_ip[blk_idx]) != 1\
                        and indv_ip[blk_idx][0] == "0")\
                    or not (0 <= int(indv_ip[blk_idx]) <= 255):
                        indv_ip[blk_idx] = ""
                        return False
                    valid = dfs(indv_ip, i + 1, blk_idx + 1)

            indv_ip[blk_idx] = ""
            if valid:
                return True
            return False
        all_ips = []
        dfs(["", "", "", ""], 0, 0)
        return all_ips




