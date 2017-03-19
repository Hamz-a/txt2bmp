# txt2bmp
This is inspired by this [hak5 episode](http://www.hak5.org/episodes/hak5-925). You can generate your own bitmaps with custom commands:

```
python txt2bmp.py -i "cmd.exe /T:02"
Width=4, height=2
rgb( 47,  32, 101)  rgb( 48,  58,  84)  rgb(  0,   0,  50)  rgb(  0,   0,   0)
rgb( 10,  13,   0)  rgb(150,  10,  13)  rgb(100, 109,  99)  rgb(120, 101,  46)
```

Print or write down those numbers so that you can make your bitmap in your favourite image editor (mspaint?) or you can generate it directly:

```
$ python txt2bmp.py -i "cmd.exe /T:02" -b payload.bat
Saved as bitmap in: payload.bat
```

You can even choose some [source code](main.cpp) and [save it](main.bmp) if you want to:

```
$ python txt2bmp.py -f main.cpp -b main.bmp
Saved as bitmap in: main.bmp
```

![preview](preview.png?raw=true)

## Usage

Use `-h` for help:

```
$ python txt2bmp.py -h
usage: txt2bmp.py [-h] (-i INPUT | -f FILE) [-b BITMAP] [-t TEXT] [-p PIXELS]

Convert text to bmp.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input text from cli
  -f FILE, --file FILE  Input text from file
  -b BITMAP, --bitmap BITMAP
                        Save image as bitmap
  -t TEXT, --text TEXT  Save rgb values to file
  -p PIXELS, --pixels PIXELS
                        Print RGB values
```

### Input

You can directly pass text from the command line via `-i`:

```
$ python txt2bmp.py -i "hello world"
Width=4, height=2
rgb(108, 114, 111)  rgb(  0,   0, 100)  rgb(  0,   0,   0)  rgb(  0,   0,   0)
rgb( 10,  13,   0)  rgb(104,  10,  13)  rgb(108, 108, 101)  rgb(119,  32, 111)
```

You can also use `-f` to read from file:

```
$ python txt2bmp.py -f input.txt
Width=4, height=2
rgb(108, 114, 111)  rgb(  0,   0, 100)  rgb(  0,   0,   0)  rgb(  0,   0,   0)
rgb( 10,  13,   0)  rgb(104,  10,  13)  rgb(108, 108, 101)  rgb(119,  32, 111)
```

### Output

By default it will print out the rgb values. You can also be explicit by using `-p`:

```
$ python txt2bmp.py -i "hello world" -p
Width=4, height=2
rgb(108, 114, 111)  rgb(  0,   0, 100)  rgb(  0,   0,   0)  rgb(  0,   0,   0)
rgb( 10,  13,   0)  rgb(104,  10,  13)  rgb(108, 108, 101)  rgb(119,  32, 111)
```

You can save the rgb values as text using `-t`:

```
$ python txt2bmp.py -i "so many helloworld" -t haha.txt
Saved as text in: haha.txt
```

Or save it as a bitmap image using `-b`:

```
$ python txt2bmp.py -i "so many helloworld" -b testorz.bmp
Saved as bitmap in: testorz.bmp
```
