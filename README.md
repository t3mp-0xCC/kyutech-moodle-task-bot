# kyutech-moodle-bot    
Discord bot that gets task list from Kyutech Univ moodle  
## Setup
1. `$ pip install -r requirements.txt`
2. `$ pacman -S xorg-server-xvfb geckodriver firefox`  
(You may need to change this command if you are using another package manager)  
3. Add some const at https://github.com/t3mp-0xCC/kyutech-moodle-task-bot/blob/main/bot.py#L11 
 
Optional: custom prefix  
Overwrite here https://github.com/t3mp-0xCC/kyutech-moodle-task-bot/blob/main/bot.py#L17  
## Commands
`help`: show help  
`list`: show moodle check schedule list  
`add <time>`: add time to the schedule list  
ex. `$add 8:00`  
`remove <time>`: remove time from the schedule list  
