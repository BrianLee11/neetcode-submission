class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_emails = set()

        for email in emails:
            local_name, domain = email.split("@")
            if '+' in local_name:
                index_first_plus_sign = local_name.index('+')
                local_name = local_name[:index_first_plus_sign].replace(".","")                
            candidate_name = local_name + '@' + domain
            set_emails.add(candidate_name)

        return len(set_emails)