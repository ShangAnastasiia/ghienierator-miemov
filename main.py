from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")

top_text = input("Введите верхний текст: ")
   
print(top_text)
memes = "m.png"
image = Image.open(memes)
draw = ImageDraw.Draw(image)

#font = ImageFont.truetype('arial.ttf', size=70)
text = draw.textbbox((0, 0), top_text) # font
draw.text((10, 10), top_text)  #font=font, fill="black"

image.save("new_meme.png")

