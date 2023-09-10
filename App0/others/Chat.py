# # import openai
# #
# # api_key = "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"  # O'z API kalitini kiritish kerak
# #
# # openai.api_key = api_key
# #
# # response = openai.Completion.create(
# #   engine="text-davinci-002",
# #   prompt="Salom, men GPT-3.5 modelman. Sizning savolingizni javobini topish uchun men sizga yordam bera olishim mumkin. Savolingizni yozing:",
# #   max_tokens=50
# # )
# #
# # print(response.choices[0].text.strip())
# import torch
# import torch.nn as nn
# import torch.optim as optim
# import random
#
# class Chatbot(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(Chatbot, self).__init__()
#         self.hidden_size = hidden_size
#
#         self.embedding = nn.Embedding(input_size, hidden_size)
#         self.gru = nn.GRU(hidden_size, hidden_size)
#         self.out = nn.Linear(hidden_size, output_size)
#         self.softmax = nn.LogSoftmax(dim=1)
#
#     def forward(self, input, hidden):
#         embedded = self.embedding(input).view(1, 1, -1)
#         output = embedded
#         output, hidden = self.gru(output, hidden)
#         output = self.out(output[0])
#         output = self.softmax(output)
#         return output, hidden
#
#     def initHidden(self):
#         return torch.zeros(1, 1, self.hidden_size)
#
#
# def chat_with_bot():
#   input_size =  10
#   hidden_size = 256  # Yashirin tarmoq o'lchami
#   output_size =  100
#   learning_rate = 0.01
#
#   # Chatbot modelini yaratish
#   chatbot = Chatbot(input_size, hidden_size, output_size)
#
#   # Modelni o'qitish uchun optimizatsiya algoritmini tanlash
#   optimizer = optim.SGD(chatbot.parameters(), lr=learning_rate)
#
#   # Modelni o'qitish uchun funksiya (masalan, nll_loss) tanlash
#
#   # Modelni o'qitish jarayoni
#   # ...
#
#   # Suhbatlash jarayoni
#   while True:
#     user_message = input("Siz: ")
#     response = chatbot_response(user_message, chatbot)
#     print("Bot: " + response)
#
#     if user_message.lower() == "exit":
#       break
#
# def tensorFromSentence(sentence, word_to_index):
#   # Berilgan so'rovi so'zlar bazasiga ko'rsatib, indekslarga o'zgartirish
#   # "sentence" matnini kalit so'zlarga bo'lib ajratamiz
#   words = sentence.split()
#   indexes = [word_to_index[word] for word in words]
#   # Indeks ketma-ketligini PyTorch tensoriga o'zgartirish
#   tensor = torch.tensor(indexes, dtype=torch.long)
#   return tensor
#
#
# # def tensorFromSentence(user_message):
# #   pass
# #
# #   def generateResponse(input_tensor, hidden, chatbot):
# #     # Chatbot javobini generatsiya qilish uchun funksiya
# #     response = []
# #     max_length = MAX_LENGTH  # O'zingizning ma'lumotlarizga qarab kerakli maksimal uzunlikni aniqlang
# #     with torch.no_grad():
# #       while True:
# #         output, hidden = chatbot(input_tensor, hidden)
# #         topv, topi = output.topk(1)
# #         response.append(topi.item())
# #
# #         if topi.item() == EOS_token or len(response) >= max_length:
# #           break
# #         pass
#
# def chatbot_response(user_message, chatbot):
#   # Foydalanuvchi so'rovlari uchun model javobini generatsiya qilish
#   input_tensor = tensorFromSentence(user_message)
#   hidden = chatbot.initHidden()
#
#   response = generateResponse(input_tensor, hidden, chatbot)
#
#   return response
# if __name__ == "__main__":
#   chat_with_bot()
import torch
import torch.nn as nn
import torch.optim as optim
import random

class Chatbot(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Chatbot, self).__init__()
        self.hidden_size = hidden_size

        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size)
        self.out = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        embedded = self.embedding(input).view(1, 1, -1)
        output = embedded
        output, hidden = self.gru(output, hidden)
        output = self.out(output[0])
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size)

def chat_with_bot():
    input_size = 10
    hidden_size = 256
    output_size = 100
    learning_rate = 0.01

    chatbot = Chatbot(input_size, hidden_size, output_size)

    optimizer = optim.SGD(chatbot.parameters(), lr=learning_rate)

    while True:
        user_message = input("Siz: ")
        response = chatbot_response(user_message, chatbot)
        print("Bot: " + response)

        if user_message.lower() == "exit":
            break

def tensorFromSentence(sentence, word_to_index):
    words = sentence.split()
    indexes = [word_to_index[word] for word in words]
    tensor = torch.tensor(indexes, dtype=torch.long)
    return tensor


def generateResponse(input_tensor, hidden, chatbot):
  response = []
  max_length = 50
  EOS_token = "<EOS>"

  with torch.no_grad():
    input_length = input_tensor.size(0)
    hidden = chatbot.initHidden()

    for ei in range(input_length):
      output, hidden = chatbot(input_tensor[ei], hidden)

    for _ in range(max_length):
      output, hidden = chatbot(input_tensor, hidden)
      topv, topi = output.topk(1)
      if topi.item() == EOS_token:
        break
      else:
        response.append(topi.item())

  response_text = ' '.join([str(item) for item in response])  # Natijani stringga aylantirish
  return response_text


# So'zlar bazasini o'zingizning ma'lumotlaringiz bo'yicha o'zgartiring
word_to_index = {
    "salom": 0,
    "men": 1,
    "siz": 2,
    # Qo'shimcha so'zlar va indekslar
}

def chatbot_response(user_message, chatbot):
    input_tensor = tensorFromSentence(user_message, word_to_index)
    hidden = chatbot.initHidden()
    response = generateResponse(input_tensor, hidden, chatbot)
    return response

if __name__ == "__main__":
    chat_with_bot()
