class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """    
        subdomain_dict = {}
        for domain_entry in cpdomains:
            # 1. Split input by ' ' to separate domain and it's count.
            input_domain = domain_entry.split(" ")
            count = int(input_domain[0])
            # 2. Split subdomain into list of subdomains.
            subdomain_list = []
            # Get number of '.' in domain.
            num_subdomains = input_domain[1].count(".")
            # For each occurrence, split into respective list of subdomains
            i = 0
            for i in range(num_subdomains):
                subdomain_list.append(input_domain[1].split(".", i)[i]) 
            # Append top level domain. Since range is not stop inclusive
            i+=1
            subdomain_list.append(input_domain[1].split(".", i)[i])

            # Convert each item in subdomain_list to a dictionary with count
            for indv_subdomain in subdomain_list:
                # 4. Add dict to result dict if unique.
                # If it isn't, then increment already occurring key's value
                key = indv_subdomain # Set key to the current domain value
                # If domain already exists in current dictionary
                if key in subdomain_dict.keys():
                    # Update dictionary
                    # Add the counts
                    count_to_add = int(subdomain_dict[key])
                    subdomain_dict.update({indv_subdomain:(count + count_to_add)})
                else: 
                    # Add to dictionary
                    subdomain_dict.update({key:count})

        # Convert to appropriate result format and return list
        return [ (str(v) + " " + k) for k,v in subdomain_dict.items() ]
                

