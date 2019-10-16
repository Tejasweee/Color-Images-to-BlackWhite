import sys

def installer(package):
    print('Installing..', package)
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image
    print('Pillow is already installed...')
except ImportError:
    installer('Pillow')

print('All requirements satisfied...')
