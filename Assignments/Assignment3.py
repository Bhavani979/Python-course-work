num_msgs = int(input("Enter total number of messages: "))
conversation = {}
for i in range(num_msgs):
    sender, message = input().split(":", 1)
    sender = sender.strip()
    message = message.strip()
    if sender in conversation:
        conversation[sender].append(message)
    else:
        conversation[sender] = [message]

print(conversation)
print(conversation.keys())

def display_menu():
    actions = [
        "Exit", "Count all messages", "List all unique participants", "Total number of words",
        "Average words per message", "Find the longest message",
        "Find most active participant", "Messages sent by specific participant",
        "Most frequent word by participant", "First and last message by participant",
        "Check participant presence", "Repeated words in chat", 
        "Participant with longest average message length",
        "Count mentions of a user", "Remove repeated messages", "Alphabetical message list",
        "List all questions", "Reply count between two participants", "Check for deleted messages"
    ]
    for i, action in enumerate(actions):
        print(f"{i}. {action}")

def total_messages(conversation):
    return sum(len(msgs) for msgs in conversation.values())

def unique_participants(conversation):
    participants = set(conversation.keys())
    return f"{len(participants)} participants: {participants}"

def total_word_count(conversation):
    full_text = " ".join([" ".join(msgs) for msgs in conversation.values()])
    return len(full_text.split())

def average_words(conversation):
    total_msgs = sum(len(msgs) for msgs in conversation.values())
    total_words = total_word_count(conversation)
    return total_words / total_msgs if total_msgs else 0

def get_longest_message(conversation):
    longest = ""
    for msgs in conversation.values():
        for msg in msgs:
            if len(msg) > len(longest):
                longest = msg
    return longest

def most_messages_user(conversation):
    return max(conversation, key=lambda k: len(conversation[k]))

def messages_by_user(conversation):
    user = input("Enter participant name: ")
    return len(conversation.get(user, []))

def frequent_word_user(conversation):
    user = input("Enter participant name: ")
    if user not in conversation:
        return "User not found"
    words = " ".join(conversation[user]).split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return max(freq, key=freq.get)

def first_last_user_msg(conversation):
    user = input("Enter participant name: ")
    if user in conversation:
        return f"First: {conversation[user][0]}, Last: {conversation[user][-1]}"
    return "User not found"

def is_user_in_chat(conversation):
    user = input("Enter participant name: ")
    return "Present" if user in conversation else "Absent"

def repeated_words(conversation):
    full_text = " ".join([" ".join(msgs) for msgs in conversation.values()])
    words = full_text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return [word for word, count in freq.items() if count > 1]

def user_with_longest_avg_msg(conversation):
    best_user = ""
    max_avg = 0
    for user, msgs in conversation.items():
        avg_len = sum(len(msg) for msg in msgs) / len(msgs)
        if avg_len > max_avg:
            max_avg = avg_len
            best_user = user
    return best_user

def mentions_of_user(conversation):
    user = input("Enter user to search mentions of: ")
    count = 0
    for msgs in conversation.values():
        count += sum(1 for msg in msgs if user in msg)
    return f"{user} is mentioned in {count} messages"

def remove_duplicate_msgs(conversation):
    for user in conversation:
        conversation[user] = list(set(conversation[user]))
    return "Duplicates removed"

def alphabetical_messages(conversation):
    all_msgs = [msg for msgs in conversation.values() for msg in msgs]
    return sorted(all_msgs)

def extract_questions(conversation):
    return [msg for msgs in conversation.values() for msg in msgs if "?" in msg]

def reply_ratio(conversation):
    a, b = input("Enter two participants (e.g. Alice and Bob): ").split(" and ")
    a = a.strip()
    b = b.strip()
    replies = sum(1 for msg in conversation.get(b, []) if a in msg)
    return f"Replies from {b} to {a}: {replies}"

def deleted_messages(conversation):
    return sum(1 for msgs in conversation.values() for msg in msgs if "deleted" in msg)

while True:
    print("="*45)
    print("Menu:")
    display_menu()
    print("="*45)
    user_choice = int(input("Choose an option: "))
    if user_choice == 0:
        break
    elif user_choice == 1:
        print(f"Total messages: {total_messages(conversation)}")
    elif user_choice == 2:
        print(unique_participants(conversation))
    elif user_choice == 3:
        print(f"Total words: {total_word_count(conversation)}")
    elif user_choice == 4:
        print(f"Average words/message: {average_words(conversation):.2f}")
    elif user_choice == 5:
        print(f"Longest message: {get_longest_message(conversation)}")
    elif user_choice == 6:
        print(f"Most active user: {most_messages_user(conversation)}")
    elif user_choice == 7:
        print(f"Messages by user: {messages_by_user(conversation)}")
    elif user_choice == 8:
        print(f"Frequent word by user: {frequent_word_user(conversation)}")
    elif user_choice == 9:
        print(first_last_user_msg(conversation))
    elif user_choice == 10:
        print(is_user_in_chat(conversation))
    elif user_choice == 11:
        print(f"Repeated words: {repeated_words(conversation)}")
    elif user_choice == 12:
        print(f"Longest average message user: {user_with_longest_avg_msg(conversation)}")
    elif user_choice == 13:
        print(mentions_of_user(conversation))
    elif user_choice == 14:
        print(remove_duplicate_msgs(conversation))
    elif user_choice == 15:
        print(f"Messages sorted alphabetically: {alphabetical_messages(conversation)}")
    elif user_choice == 16:
        print(f"Questions asked: {extract_questions(conversation)}")
    elif user_choice == 17:
        print(reply_ratio(conversation))
    elif user_choice == 18:
        print(f"Deleted messages count: {deleted_messages(conversation)}")
    else:
        print("Invalid choice")
