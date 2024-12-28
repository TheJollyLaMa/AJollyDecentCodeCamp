import datetime

class Subscription:
    def __init__(self, subscriber_name, plan_name, plan_price):
        self.subscriber_name = subscriber_name
        self.plan_name = plan_name
        self.plan_price = plan_price
        self.start_date = datetime.date.today()

    def __str__(self):
        return (f"Subscriber: {self.subscriber_name}\n"
                f"Plan: {self.plan_name}\n"
                f"Price: ${self.plan_price:.2f} per month\n"
                f"Start Date: {self.start_date}")

class SubscriptionManager:
    def __init__(self):
        # Could replace with a database or file storage in a real app
        self.active_subscriptions = []

    def add_subscription(self, subscriber_name, plan_name, plan_price):
        new_subscription = Subscription(subscriber_name, plan_name, plan_price)
        self.active_subscriptions.append(new_subscription)
        print(f"\nSubscription created for {subscriber_name} on the {plan_name} plan.\n")

    def list_subscriptions(self):
        if not self.active_subscriptions:
            print("\nNo active subscriptions.")
            return

        print("\n--- Active Subscriptions ---")
        for idx, subscription in enumerate(self.active_subscriptions, start=1):
            print(f"\nSubscription #{idx}")
            print(subscription)
        print("----------------------------")

    def remove_subscription(self, subscriber_name):
        """Remove a subscription by subscriber's name (simple example)."""
        initial_count = len(self.active_subscriptions)
        self.active_subscriptions = [
            sub for sub in self.active_subscriptions
            if sub.subscriber_name.lower() != subscriber_name.lower()
        ]
        if len(self.active_subscriptions) < initial_count:
            print(f"\nSubscription for {subscriber_name} has been removed.")
        else:
            print(f"\nNo subscription found for {subscriber_name}.")

def main():
    manager = SubscriptionManager()

    while True:
        print("\n==== Simple Subscription Manager ====")
        print("1. Add a new subscription")
        print("2. List all subscriptions")
        print("3. Remove a subscription")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            subscriber_name = input("Enter subscriber's name: ").strip()
            plan_name = input("Enter plan name (e.g., Basic, Premium): ").strip()
            # A real app might check the plan name in a database or a config
            try:
                plan_price = float(input("Enter monthly plan price (e.g., 9.99): ").strip())
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            manager.add_subscription(subscriber_name, plan_name, plan_price)

        elif choice == "2":
            manager.list_subscriptions()

        elif choice == "3":
            subscriber_name = input("Enter subscriber's name to remove: ").strip()
            manager.remove_subscription(subscriber_name)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()