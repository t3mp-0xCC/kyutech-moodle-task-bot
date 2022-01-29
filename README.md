# kyutech-moodle-task-bot    
Discord bot that gets task list from Kyutech Univ moodle  
## Setup
### 1. install depends  
**Debian (or Ubuntu)**  
1. Install depends packages  

`$ sudo apt install python3-pip xvfb firefox`

2. Install geckodriver  

`$ wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz`  
`$ tar -xvzf geckodriver*`
`$ chmod +x geckodriver`
`$ sudo mv ./geckodriver /usr/local/bin`
**Arch Linux**  
1. Install depends packages  
`$ sudo  pacman -S python-pip xorg-server-xvfb geckodriver firefox`  

### 2. install pip package
`$ pip install -r requirements.txt`  

### 3. Add some information  
Add some const at https://github.com/t3mp-0xCC/kyutech-moodle-task-bot/blob/main/bot.py#L11 

Optional: custom prefix  
Default prefix is `$`  
If it overlaps with other bots, overwrite here https://github.com/t3mp-0xCC/kyutech-moodle-task-bot/blob/main/bot.py#L17  
## Commands
`help`: show help  
`list`: show moodle check schedule  list  
`add <time>`: add time to the check schedule list  
e.g.  `add 8:00`  
`remove <time>`: remove time from the schedule list  
