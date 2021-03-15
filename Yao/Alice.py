class Alice:
    # Initialize private data
    def __init__(self):
        self.x = 10
        print(f"Alice: x value is {self.x}")

    # Receive the encrypted y value and perform comparison
    def compare(self, y_enc):
        print(f"Alice: receive encrypted y value from Bob")
        result = y_enc >= self.x
        if result.get_plain_text().item() == 1.0:
            print("Alice: x is lower or equal to y")
        else:
            print("Alice: x is greater than y")

        # Return encrypted result
        return result
