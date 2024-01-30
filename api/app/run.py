import sys
print(sys.path)

from app import create_app

if __name__ == '__main__':
    app = create_app('config.py')
    app.run()
