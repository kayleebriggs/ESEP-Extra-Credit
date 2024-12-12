# ESEP Extra Credit 

class InMemoryDB:
    def __init__(self):
        """Initialize the in-memory database."""
        self.main_db = {}  # Stores committed key-value pairs
        self.transaction_changes = {}  # Tracks uncommitted changes
        self.transaction_active = False  # Tracks whether a transaction is active

    def begin_transaction(self):
        """Start a new transaction."""
        if self.transaction_active:
            raise Exception("Transaction already in progress.")
        self.transaction_active = True
        self.transaction_changes = {}

    def put(self, key, val):
        """Add or update a key-value pair during a transaction."""
        if not self.transaction_active:
            raise Exception("No active transaction.")
        self.transaction_changes[key] = val

    def get(self, key):
        """Retrieve the value associated with a key."""
        if self.transaction_active and key in self.transaction_changes:
            return self.transaction_changes[key]
        return self.main_db.get(key, None)

    def commit(self):
        """Commit the current transaction, making changes permanent."""
        if not self.transaction_active:
            raise Exception("No active transaction to commit.")
        self.main_db.update(self.transaction_changes)
        self.transaction_changes = {}
        self.transaction_active = False

    def rollback(self):
        """Rollback the current transaction, discarding changes."""
        if not self.transaction_active:
            raise Exception("No active transaction to rollback.")
        self.transaction_changes = {}
        self.transaction_active = False

# Test Script, does all the tests from the assignment
def test_inmemorydb():
    db = InMemoryDB()

    # Test get without a key
    print(db.get("A"))  # Output: None

    # Test put without transaction
    try:
        db.put("A", 5)
    except Exception as e:
        print(e)  # Output: No active transaction.

    # Start a transaction and put values
    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # Output: 5 (uncommitted change)

    # Commit the transaction
    db.commit()
    print(db.get("A"))  # Output: 5

    # Start a new transaction, make changes, and rollback
    db.begin_transaction()
    db.put("A", 10)
    print(db.get("A"))  # Output: 10 (uncommitted change)
    db.rollback()
    print(db.get("A"))  # Output: 5

    # Test multiple keys
    db.begin_transaction()
    db.put("B", 15)
    db.put("C", 20)
    print(db.get("B"))  # Output: 15
    print(db.get("C"))  # Output: 20
    db.commit()
    print(db.get("B"))  # Output: 15
    print(db.get("C"))  # Output: 20

    # Test commit without an active transaction
    try:
        db.commit()
    except Exception as e:
        print(e)  # Output: No active transaction to commit.

    # Test rollback without an active transaction
    try:
        db.rollback()
    except Exception as e:
        print(e)  # Output: No active transaction to rollback.

if __name__ == "__main__":
    test_inmemorydb()
