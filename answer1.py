class TokenCounter:
    def __init__(self):
        self.collection = []

    def ingest(self, tokens):
        self.collection.append(tokens)

    def appearance(self, prefix):
        total_count = 0
        prefix_count = 0

        for tokens in self.collection:
            total_count += 1
            if tokens.startswith(prefix):
                prefix_count += 1

        if total_count == 0:
            result = 0
        else:
            result = prefix_count / total_count

        return result


token_counter = TokenCounter()

while True:
    command = input("Enter a command (ingest or appearance): ")
    if command == "ingest":
        tokens = input("Enter the string tokens: ")
        token_counter.ingest(tokens)
    elif command == "appearance":
        prefix = input("Enter the prefix: ")
        result = token_counter.appearance(prefix)
        print(f"# > {result}")
    else:
        break

# Space Complexity:

# The space complexity of the TokenCounter class is O(n), where n is the number of tokens ingested. It is because the tokens are stored in the self.collection list, which requires space proportional to the number of tokens.
    
# Time Complexity:

# The time complexity of the ingest method is O(1) because it simply appends the tokens to the self.collection list, which has constant time complexity.

# The time complexity of the appearance method is O(n * m), where n is the number of tokens ingested and m is the average length of the tokens. This is because the method iterates over the self.collection list once and checks if each token starts with the given prefix. The check has a time complexity of O(m) in the worst case, which is done for each token.