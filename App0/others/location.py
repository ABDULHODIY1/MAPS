from transformers import DALL_E



# DALL·E modelini yaratish
model = DALL_E.from_pretrained("openai/IMAGE_DALL_E_64")
# So'rovnoma yuborish
text = "Qizil rasmning ichida ichki rangdagi kvadrat tashkil etgan"
inputs = model(text, return_tensors="pt")
image = inputs.pixel_values
# Rasmini saqlas
image.save("dalle_generated_image.png")


