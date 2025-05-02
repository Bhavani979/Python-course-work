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
    for i in range(len(actions)):
        print(f"{i}. {actions[i]}")

def total_messages(conversation):
    count = 0
    for msgs in conversation.values():
        count += len(msgs)
    return count

def unique_participants(conversation):
    participants = set()
    for user in conversation:
        participants.add(user)
    return f"{len(participants)} participants: {participants}"

def total_word_count(conversation):
    count = 0
    for msgs in conversation.values():
        for msg in msgs:
            words = msg.split()
            count += len(words)
    return count

def average_words(conversation):
    total_msgs = 0
    total_words = 0
    for msgs in conversation.values():
        total_msgs += len(msgs)
        for msg in msgs:
            total_words += len(msg.split())
    if total_msgs == 0:
        return 0
    return total_words / total_msgs

def get_longest_message(conversation):
    longest = ""
    for msgs in conversation.values():
        for msg in msgs:
            if len(msg) > len(longest):
                longest = msg
    return longest

def most_messages_user(conversation):
    max_msgs = 0
    most_active = ""
    for user in conversation:
        count = len(conversation[user])
        if count > max_msgs:
            max_msgs = count
            most_active = user
    return most_active

def messages_by_user(conversation):
    user = input("Enter participant name: ")
    if user in conversation:
        return len(conversation[user])
    return 0

def frequent_word_user(conversation):
    user = input("Enter participant name: ")
    if user not in conversation:
        return "User not found"
    all_words = {}
    for msg in conversation[user]:
        for word in msg.split():
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1
    max_count = 0
    most_common = ""
    for word in all_words:
        if all_words[word] > max_count:
            max_count = all_words[word]
            most_common = word
    return most_common

def first_last_user_msg(conversation):
    user = input("Enter participant name: ")
    if user in conversation and conversation[user]:
        return f"First: {conversation[user][0]}, Last: {conversation[user][-1]}"
    return "User not found or no messages"

def is_user_in_chat(conversation):
    user = input("Enter participant name: ")
    if user in conversation:
        return "Present"
    return "Absent"

def repeated_words(conversation):
    all_words = {}
    for msgs in conversation.values():
        for msg in msgs:
            for word in msg.split():
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1
    result = []
    for word in all_words:
        if all_words[word] > 1:
            result.append(word)
    return result

def user_with_longest_avg_msg(conversation):
    max_avg = 0
    best_user = ""
    for user in conversation:
        total_length = 0
        count = 0
        for msg in conversation[user]:
            total_length += len(msg)
            count += 1
        if count > 0:
            avg_len = total_length / count
            if avg_len > max_avg:
                max_avg = avg_len
                best_user = user
    return best_user

def mentions_of_user(conversation):
    user = input("Enter user to search mentions of: ")
    count = 0
    for msgs in conversation.values():
        for msg in msgs:
            if user in msg:
                count += 1
    return f"{user} is mentioned in {count} messages"

def remove_duplicate_msgs(conversation):
    for user in conversation:
        seen = set()
        unique = []
        for msg in conversation[user]:
            if msg not in seen:
                seen.add(msg)
                unique.append(msg)
        conversation[user] = unique
    return "Duplicates removed"

def alphabetical_messages(conversation):
    all_msgs = []
    for msgs in conversation.values():
        for msg in msgs:
            all_msgs.append(msg)
    all_msgs.sort()
    return all_msgs

def extract_questions(conversation):
    questions = []
    for msgs in conversation.values():
        for msg in msgs:
            if "?" in msg:
                questions.append(msg)
    return questions

def reply_ratio(conversation):
    a, b = input("Enter two participants (e.g. Alice and Bob): ").split(" and ")
    a = a.strip()
    b = b.strip()
    count = 0
    if b in conversation:
        for msg in conversation[b]:
            if a in msg:
                count += 1
    return f"Replies from {b} to {a}: {count}"

def deleted_messages(conversation):
    count = 0
    for msgs in conversation.values():
        for msg in msgs:
            if "deleted" in msg:
                count += 1
    return count

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
