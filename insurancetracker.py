class InsurancePolicy:
    def __init__(self, policy_number, provider, coverage_amount, premium, expiration_date):
        self.policy_number = policy_number
        self.provider = provider
        self.coverage_amount = coverage_amount
        self.premium = premium
        self.expiration_date = expiration_date

    def __str__(self):
        return (f"Policy Number: {self.policy_number}, "
                f"Provider: {self.provider}, "
                f"Coverage Amount: ${self.coverage_amount}, "
                f"Premium: ${self.premium}, "
                f"Expiration Date: {self.expiration_date}")

class InsuranceTracker:
    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)
        print(f"Added policy: {policy.policy_number}")

    def update_policy(self, policy_number, **kwargs):
        for policy in self.policies:
            if policy.policy_number == policy_number:
                for key, value in kwargs.items():
                    setattr(policy, key, value)
                print(f"Updated policy: {policy.policy_number}")
                return
        print(f"Policy number {policy_number} not found.")

    def view_policies(self):
        if not self.policies:
            print("No policies found.")
        for policy in self.policies:
            print(policy)

# Example usage
tracker = InsuranceTracker()

# Adding policies
tracker.add_policy(InsurancePolicy("12345", "ABC Insurance", 100000, 1200, "2025-12-31"))
tracker.add_policy(InsurancePolicy("67890", "XYZ Insurance", 50000, 600, "2023-06-30"))

# Viewing policies
print("\nCurrent Policies:")
tracker.view_policies()

# Updating a policy
tracker.update_policy(policy_number="12345", coverage_amount=150000, premium=1300)

# Viewing policies after update
print("\nUpdated Policies:")
tracker.view_policies()
