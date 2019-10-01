## [WIP] Razer Chroma API Python terminal.
---
Simple  terminal used to test out Razers Chroma SDK via the REST api.  
Tested with Python 3.7  

This is still in super early testing, and developed mainly to learn more about the razer chroma REST api.  


#### Installation and usage: 
```
pip install -r requirements.txt
python razer_api_shell.py
```

#### Commands:
```
help - show all commands
init - connect to the API on localhost
colorname <color> - Set entire keyboard to <color>
controls - set color only on keys usually used for gaming
check - show the current number of keepalive pings
quit - disconnect from api and exit
```

#### Contributing:
Feel free to fork and edit the code.  
If you come up with a new feature, feel free to create a pull request.
