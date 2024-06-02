import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet
from unifundchatbot import tokenize, stem, bag_of_words

# Ensure these functions work as expected

# Check if GPU is available, else use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents and scholarships data from JSON
with open('scholarships_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Combine intents and scholarships into a single list
intents = data['intents']
scholarships = data['scholarships']
merged_data = intents + scholarships

# Extract words, tags, and training data from intents
all_words = []
tags = []
xy = []

for intent in intents:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        words = tokenize(pattern)
        all_words.extend(words)
        xy.append((words, tag))

# Create a unique tag for scholarships
scholarship_tag = "scholarship"

# Extract words and training data from scholarships
for scholarship in scholarships:
    words = tokenize(scholarship['title'])
    all_words.extend(words)
    xy.append((words, scholarship_tag))

# Stem and remove duplicates from all_words
all_words = [stem(word) for word in all_words if word != '?']
all_words = sorted(set(all_words))

# Create training data
X_train = []
y_train = []

for (pattern_words, tag) in xy:
    bag = bag_of_words(pattern_words, all_words)
    X_train.append(bag)
    label = tags.index(tag) if tag in tags else len(tags)  # Assign a unique index for scholarships
    y_train.append(label)

# Add scholarship tag to tags list
if scholarship_tag not in tags:
    tags.append(scholarship_tag)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Define dataset class for PyTorch
class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return torch.tensor(self.x_data[index], dtype=torch.float32).to(device), torch.tensor(self.y_data[index], dtype=torch.long).to(device)

    def __len__(self):
        return self.n_samples

# Hyperparameters
batch_size = 8
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)  # Adjusted to handle dynamic tags list
learning_rate = 0.001
num_epochs = 2500

# Create DataLoader
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)

# Define and train the model
model = NeuralNet(input_size, hidden_size, output_size).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

print(f'Final loss: {loss.item():.4f}')

# Save the model
data = {
    'model_state': model.state_dict(),
    'input_size': input_size,
    'output_size': output_size,
    'hidden_size': hidden_size,
    'all_words': all_words,
    'tags': tags
}

FILE = "data.pth"
torch.save(data, FILE)
print(f'Training complete. Model saved to {FILE}')
