# YouTube

<h1 align="center">
  <br>
  <a href="Python"><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpythonprogramming.net%2Fstatic%2Fimages%2Ffinance%2Fpython-programming-language.png&f=1&nofb=1" alt="Markdownify" width="200"></a>
  <br>
  YouTube Live Chat Scanner
  <br>
</h1>

<h4 align="center">A simple program to collect YouTube chat data and find high chat activity 

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![theApp](https://user-images.githubusercontent.com/64375555/147840728-5460cad9-c1f1-4b64-867e-fb9e7a892e30.png)
![image](https://user-images.githubusercontent.com/64375555/147840751-5a679264-4193-4295-a26f-ade2f07b94b7.png)


## Key Features

* Collect YouTube chat activity - Get a file with timestamps of a message being sent
  - Adjustable to edit to your needs
* Computed for you
  - Collect timestamps and have it grouped in multiple intervals to find consistency in short or long videos
* Popup to notify you when process is starting and complete

## How To Use

To run this application, you'll need [pyinstaller](https://www.pyinstaller.org/) From your command line:

```bash
# Go to the folder with the downloaded files
$ pip install pyinstaller

# Afterwards
$ pyinstaller --onefile Main.py

# Run the app
$ python Main.py

# May need to install PySimpleGUI && pytchat
python -m pip install SomePackage

sudo apt-get install python3-tk

# If PyInstaller doesn't work for some reason
python -m PyInstaller --onefile Main.py

# python --> python3, depending on your system
# Afterwards, go to dist and just run Main

```

Note: If you want to collect data from multiple videos, you'll need to open a new app instance.

After placing the entire link, name of the YouTube[not important] followed with a colon [:], type the name of the video. Can be anything you want, so long as there is no space. A file with that name should appear with _ChatData.txt appended on it. Just a file with timestamps of when someone typed something. The _StarData.txt grabs those numbers, omits negative timestamps/prestream chat, and ranks them in order of the most popular timestamps to a least populat timestamp. It will display the splitter, how big a range is, their ranking with timestamps, and the amount of comments since the beginning of that time stamp

## Credits

This software uses the following open source packages:

- [pytchat](https://github.com/taizan-hokuto/pytchat)
- [Python](https://www.python.org/downloads/)


## License

GPL-3.0 License

---
> GitHub [@ArisaBonsaiTree](https://github.com/ArisaBonsaiTree)

