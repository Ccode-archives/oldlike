pyinstaller oldlike.py -F --onefile || (echo "pyinstaller error" && exit)
mv dist/oldlike oldlike
