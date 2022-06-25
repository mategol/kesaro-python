# Kesaro
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
> For example: inject ? > github.exe  will ask you for payload file.

