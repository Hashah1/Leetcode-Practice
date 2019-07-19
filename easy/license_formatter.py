class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # Split into respective groups
        license_groups = S.split('-')  # 5F3Z-2e-9-w -> [5F3Z, 2e, 9, w]
        print(license_groups)
        for j in range(len(license_groups) - 1, -1, -1 ):
            if j >= len(license_groups):
                j = len(license_groups) - 1
            # Check the length of the group and rearrange accordingly.
            while len(license_groups[j]) != K:
                if len(license_groups[j]) < K:  # Expand group
                    # Grab a character from end of prev_group
                    license_groups[j] = license_groups[j - 1][-1] + license_groups[j]
                    # Update previous group
                    license_groups[j - 1] = license_groups[j - 1][:-1]
                    # Delete any empty groups
                    if license_groups[j - 1] is '':
                        del license_groups[j - 1]
                        j -= 1
        pass

            
if __name__ == "__main__":
    a = Solution()
    a = a.licenseKeyFormatting("5F3Z-2e-9-w", 4)
    pass