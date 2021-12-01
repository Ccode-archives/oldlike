pyinstaller oldlike.py -F --onefile || (echo "pyinstaller error" && exit)
rm -rf build
rm -rf oldlike.spec
mv dist/oldlike oldlike
rm -rf dist
