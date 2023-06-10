# Kesaro-python

A complete software for injecting your payload to any Windows executable.

# Disclaimer

> Information and code provided on this repository are for educational purposes only. The creator is no way responsible for any direct or indirect damage caused due to the misusage of the information. Everything you do, you are doing at your own risk and responsibility.

# Installation

For now, this is Windows only software. You can install it with:
```
git clone https://github.com/mategol/kesaro-python
pip install -r requirements.txt
python main.py
```

# Commands

`inject SOURCE > TARGET` - inject your payload (SOURCE) into any executable (TARGET)<br />
> You can use question mark (?) instead of path to make the software prompt you to manually choose desired files.<br />
> For example: inject ? > github.exe  will ask you only for payload file and use specified target file.

<br />
more coming soon...

# Example

### I prepared simple program printing elements from "for" loop for demonstration
It can be whatever payload you want to use. It's best to use executable that is running in background.

<img src="https://user-images.githubusercontent.com/44233157/175880994-af80b20a-bae4-4098-8fed-95e79ff958b7.gif" />

### For my target file, I will use VirtualBox Installer. Sorry Oracle... just for demonstration.
It can be any executable working for Windows.

<img src="https://user-images.githubusercontent.com/44233157/175882173-adf18d54-2422-4009-b823-7e45662ba62f.gif" />

### Injecting payload

Now, showtime. Execute command `inject main.exe > virtualbox.exe` and software will automatically compile files together.

### Output file

I renamed output file to VBox-Setup.exe. Remember, if Windows will throw you errors on file execution, just rename it. Look, both files are executed together (packed in VBox-Setup.exe).

<img src="https://user-images.githubusercontent.com/44233157/175884323-39a8f440-596c-4e99-887c-65b4716efc0d.gif" />

All properties were also cloned.

<img src="https://user-images.githubusercontent.com/44233157/175885091-6985fe6f-06e4-41a4-b267-f0ca30f9364b.JPG" />

# ToDo
✅ Injecting payload to any executable  
✅ Command Line Interface  
✅ Cloning target file's properties  
❌ Properties editor for fast and intuitive editing of properties  
❌ Preset maker for injecting Python source code directly to target file  
❌ software compatibility with Linux OS
