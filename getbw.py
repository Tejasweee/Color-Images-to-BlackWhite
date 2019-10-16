import os
from PIL import Image


if not 'BlackWhite' in os.listdir():
    os.makedirs('BlackWhite')

at_start=len(os.listdir('BlackWhite'))
def convertbw(file):
    '''Converts given file (if image' to black and white image'''
    if not ((('.py') in file) or (('BlackWhite') in file)): 
        try:
            with Image.open(file) as imgfile:
                imgfile = imgfile.convert('L')
                filepath='BlackWhite' +'/' + file
                imgfile.save(filepath)
            print('Successfully converted:', file)
        except Exception as e:
            print('Failed to convert ' + file)
            print(e)
            
def check():
    for file in os.listdir():
        if file not in os.listdir('BlackWhite'):
            convertbw(file)

if __name__ =='__main__':
    check()

    at_end=len(os.listdir('BlackWhite'))
    count= at_end-at_start
    print('')
    print('Successfully converted '+ str(count)+ ' images in 'BlackWhite' folder.')
