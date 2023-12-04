class Database:
    def __init__(self):
        self.data = {}
        self.transaction_data = {}
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            print("Error: Transaction already in progress")
            return
        self.in_transaction = True

    def put(self, key, value):
        if not self.in_transaction:
            print("Error: No transaction in progress")
            return

        self.transaction_data[key] = value

    def get(self, key):
        if key in self.transaction_data:
            return self.transaction_data[key]
        return self.data.get(key, None)

    def commit(self):
        if not self.in_transaction:
            print("Error: No transaction in progress")
            return

        self.data.update(self.transaction_data)
        self.transaction_data.clear()
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            print("Error: No transaction in progress")
            return

        self.transaction_data.clear()
        self.in_transaction = False


def main():
    db = Database()
    print('Welcome to the database! Please use the command "help" for available commands :)')
    while True:
        command = input("Enter command: ").split()
        if command[0] == "begin_transaction":
            db.begin_transaction()
        elif command[0] == "put":
            if len(command) != 3:
                print("Usage: put <key> <value>")
                continue
            key, value = command[1], int(command[2])
            db.put(key, value)
        elif command[0] == "get":
            if len(command) != 2:
                print("Usage: get <key>")
                continue
            key = command[1]
            result = db.get(key)
            print(f"Value: {result}")
        elif command[0] == "commit":
            db.commit()
            print("Transaction committed.")
        elif command[0] == "rollback":
            db.rollback()
            print("Transaction rolled back.")
        elif command[0] == "exit":
            break
        elif command[0] == "help":
            print("Available commands: begin_transaction, put, get, commit, rollback, exit")
        else:
            print("Invalid command. Available commands: help, begin_transaction, put, get, commit, rollback, exit")


if __name__ == "__main__":
    main()