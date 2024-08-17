"""
Explanation:

1. Loop Over Possible Values of y:
   The outer loop iterates over potential message counts (y), trying to find a valid split.

2. Calculate Suffix:
   For each message, the suffix <x/y> is calculated.

3. Check Maximum Length:
   Ensure that the text chunk plus the suffix does not exceed the limit.

4. Add Messages:
   Messages are added to the list with their respective suffixes.

5. Verify Correct Splitting:
   If the number of messages equals y and all text is used, the function returns the list of messages.
"""


def solution(text, limit):
    # Start by checking if y = 0 (which means no messages should be generated)
    if limit <= 0:
        return []  # If the limit is less than or equal to 0, return an empty list immediately

    # Loop over possible values for y, including starting from 0
    for y in range(0, len(text) + 1):
        # If y = 0, we expect to return an empty list
        if y == 0:
            continue  # Skip processing for y = 0

        messages = []  # Initialize a list to store the resulting messages
        i = 0  # Initialize the starting index of the text

        # Loop over each message number from 1 to y
        for x in range(1, y + 1):
            suffix = f"<{x}/{y}>"  # Create the <x/y> suffix
            max_len = limit - len(suffix)  # Calculate the remaining space for the text in the current message

            if max_len <= 0:
                break  # If the remaining space is not enough to hold any text, exit the loop

            if x < y:
                next_chunk = text[i:i + max_len]  # If not the last message, take a full chunk
            else:
                next_chunk = text[i:]  # If it's the last message, take the rest of the text

            if len(next_chunk) + len(suffix) > limit:
                break  # If the length of the next chunk plus the suffix exceeds the limit, exit the loop

            messages.append(next_chunk + suffix)  # Add the sliced message with the suffix to the messages list
            i += len(next_chunk)  # Move the index forward by the length of the chunk

        # If the number of messages generated matches y and all text is used, return the messages
        if len(messages) == y and i == len(text):
            return messages

    # If no valid splitting was found, return an empty list
    return []


# Example usage
print("My output: ",solution("abcdefghijklmonpqrstuvwxyz", 8))
