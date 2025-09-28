import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Vansh Wagh"

#Tokens :  [25216, 3274, 0, 3673, 1308, 382, 160582, 71, 486, 24111]

tokens = enc.encode(text)

print("Tokens : ", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 160582, 71, 486, 24111])
print("Decoded : ", decoded)