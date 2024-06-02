import random
import json
import torch
from model import NeuralNet
from unifundchatbot import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('scholarships_data.json', 'r') as f:
    merged_data = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(sentence):
    sentence_tokens = tokenize(sentence)
    X = bag_of_words(sentence_tokens, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    if predicted.item() >= len(tags):
        return "I do not understand..."

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in merged_data['intents']:
            if tag == intent["tag"]:
                return random.choice(intent["responses"])

        if tag == "scholarship":
            sentence_str = " ".join(sentence_tokens)
            for scholarship in merged_data['scholarships']:
                if scholarship['title'].lower() in sentence_str.lower():
                    if "url" in sentence_str.lower():
                        return f"URL: {scholarship['url']}"
                    elif "award" in sentence_str.lower():
                        return f"Award: {scholarship['award']}"
                    elif "criteria" in sentence_str.lower():
                        return f"Criteria: {scholarship['criteria']}"
                    elif "deadline" in sentence_str.lower():
                        return f"Deadline: {scholarship['deadline']}"
                    elif "eligibility" in sentence_str.lower():
                        return f"Eligibility: {scholarship['eligibility_description']}"
                    else:
                        return (f"Title: {scholarship['title']}\n"
                                f"Award: {scholarship['award']}\n"
                                f"Criteria: {scholarship['criteria']}\n"
                                f"Deadline: {scholarship['deadline']}\n"
                                f"URL: {scholarship['url']}")

        return "I am not sure what to respond to that."
    else:
        return "I do not understand..."

# Only run this part if executing this script directly
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence.lower() == "quit":
            break
        response = get_response(sentence)
        print(f"{bot_name}: {response}")