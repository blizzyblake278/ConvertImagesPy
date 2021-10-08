from PIL import Image
# gave error that it cannot write mode RGBA as JPEG. RGBA means
# RED GREEN BLUE ALPA, Alpha is transparency. so you have to
# convert it to RGB so it can read it.

imageOne = Image.open(r'C:\Users\magic\Downloads\Ford-logo-1929-1440x900.png')
imgRGB = imageOne.convert('RGB')
imgRGB.save(r'C:\Users\magic\Downloads\FordLogo.jpg')
print('Conversion done!!!')
