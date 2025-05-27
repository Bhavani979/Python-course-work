import os
import re

# Directory for storing reviews
REVIEW_DIR = "book_reviews"

# Ensure directory exists
if not os.path.exists(REVIEW_DIR):
    os.makedirs(REVIEW_DIR)

# Simple sentiment keywords
positive_keywords = [
    'amazing', 'wonderful', 'great', 'fantastic', 'excellent', 'loved', 'incredible', 'outstanding',
    'beautiful', 'enjoyed', 'brilliant', 'awesome', 'compelling', 'engaging'
]

negative_keywords = [
    'boring', 'bad', 'terrible', 'awful', 'poor', 'disappointing', 'worst', 'hate', 'dull',
    'confusing', 'uninteresting', 'predictable', 'slow', 'mediocre'
]

def analyze_sentiment(content):
    pos_found = re.findall(r'\b(?:' + '|'.join(positive_keywords) + r')\b', content, re.IGNORECASE)
    neg_found = re.findall(r'\b(?:' + '|'.join(negative_keywords) + r')\b', content, re.IGNORECASE)

    print(f"\n🔍 Positive Words: {pos_found}")
    print(f"🔍 Negative Words: {neg_found}")

    if len(pos_found) > len(neg_found):
        print("✅ Sentiment: Positive Review")
    elif len(neg_found) > len(pos_found):
        print("❌ Sentiment: Negative Review")
    else:
        print("⚖️ Sentiment: Neutral or Mixed Review")

def analyze_review():
    print("\n--- Analyze Book Reviews ---")
    choice = input("Analyze a specific review or all? (specific/all): ").strip().lower()

    if choice == "specific":
        filename = input("Enter the filename: ").strip()
        filepath = os.path.join(REVIEW_DIR, filename)
        try:
            with open(filepath, 'r') as file:
                content = file.read()
                print("\n--- Review Content ---\n" + content)
                analyze_sentiment(content)
        except FileNotFoundError:
            print("❌ File not found.")
    elif choice == "all":
        files = os.listdir(REVIEW_DIR)
        if not files:
            print("📂 No reviews to analyze.")
            return
        for filename in files:
            filepath = os.path.join(REVIEW_DIR, filename)
            with open(filepath, 'r') as file:
                content = file.read()
                print(f"\n📘 {filename}")
                print("-------------------")
                analyze_sentiment(content)
    else:
        print("❌ Invalid choice.")

def create_review():
    print("\n--- Create a New Book Review ---")
    filename = input("Enter a filename: ").strip()
    content = input("Enter the content of the review:\n")
    
    filepath = os.path.join(REVIEW_DIR, filename)
    with open(filepath, 'w') as file:
        file.write(content)
    print("✅ Review saved successfully.")

def modify_review():
    print("\n--- Modify Existing Book Review ---")
    files = os.listdir(REVIEW_DIR)
    if not files:
        print("📂 No reviews to modify.")
        return
    print("📄 Available Reviews:")
    for f in files:
        print(f"- {f}")

    filename = input("Enter the filename to modify: ").strip()
    filepath = os.path.join(REVIEW_DIR, filename)
    if not os.path.exists(filepath):
        print("❌ File not found.")
        return

    with open(filepath, 'r') as file:
        old_content = file.read()
        print("\n--- Current Review ---\n" + old_content)

    new_content = input("\nEnter the new content:\n")
    with open(filepath, 'w') as file:
        file.write(new_content)
    print("✅ Review updated successfully.")

def main():
    print("📚 Welcome to Book Review Sentiment Checker 📚")

    while True:
        print("\n--- Menu ---")
        print("1. Analyze Book Reviews")
        print("2. Create New Review")
        print("3. Modify Existing Review")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == '1':
                analyze_review()
            elif choice == '2':
                create_review()
            elif choice == '3':
                modify_review()
            elif choice == '4':
                print("👋 Exiting... Happy Reading!")
                break
            else:
                print("❌ Invalid option. Please choose 1-4.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
