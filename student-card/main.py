import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def card(student_id, name, dob):

    # Tạo hình ảnh thẻ sinh viên rỗng với kích thước 350x220 pixel
    img = Image.new('RGB', (350, 220), color=(255, 255, 255))

    # Tải font chữ và thiết lập kích thước
    title_font = ImageFont.truetype('arial.ttf', 22)
    sub_title_font = ImageFont.truetype('arial.ttf', 14)
    content_font = ImageFont.truetype('arial.ttf', 12)

    # Vẽ thông tin sinh viên lên hình ảnh
    draw = ImageDraw.Draw(img)

    # Vẽ nền màu xanh lá cây cho tiêu đề
    draw.rectangle((0, 0, 350, 50), fill=(50, 205, 100))

    # Vẽ tiêu đề thẻ sinh viên
    draw.text((120, 10), "Thẻ Sinh Viên", font=title_font, fill=(255, 255, 255))

    # Vẽ thông tin sinh viên
    draw.text((120, 60), "Mã sinh viên:", font=sub_title_font, fill=(0, 0, 0))
    draw.text((220, 60), student_id, font=content_font, fill=(0, 0, 0))

    draw.text((120, 100), "Họ và tên:", font=sub_title_font, fill=(0, 0, 0))
    draw.text((200, 100), name, font=content_font, fill=(0, 0, 0))

    draw.text((120, 140), "Ngày sinh:", font=sub_title_font, fill=(0, 0, 0))
    draw.text((200, 140), dob, font=content_font, fill=(0, 0, 0))

    # Tải ảnh của sinh viên và vẽ lên thẻ
    photo = Image.open('D:\zvatar.jpg')
    photo = photo.resize((80, 80))
    img.paste(photo, (20, 60))

    # Lưu hình ảnh thẻ sinh viên
    img.save(f"{student_id}.jpg")

df = pd.read_excel('D:\input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
data = []
for row in df.iterrows():
    row_data = []
    for value in row[1]:
        row_data.append(value)
        data.append(row_data)
    card(row_data[1],row_data[2] + " " + row_data[3],row_data[4])