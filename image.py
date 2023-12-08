from PIL import Image

image = Image.open('data/example.png')

image_data = image.load()

height,width = image.size

for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = image_data[loop1,loop2]


        if 0 <= r <= 255 and 0 <= g <= 100 and 0 <= b <= 100:
            image_data[loop1,loop2] = 255,255,255
        elif r < 150 and g < 150 and b < 150:
            image_data[loop1,loop2] = 0,0,0
        elif r > 150 and g > 150 and b > 150:
            image_data[loop1,loop2] = 255,255,255
        else:
            avg = max(int((r+g+b)/3) - 75, 0)
            image_data[loop1,loop2] = avg, avg, avg


image.save('processed.png')

image.show()