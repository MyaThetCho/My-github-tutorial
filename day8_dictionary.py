text = {
    "Hello" : "Hi",
    "How are you" : "Fine, Thank U",
    ":)" : "🙂"
}

message = input("Enter = ")
print(text.get(message, "🙃"))