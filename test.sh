#!/bin/bash
set -e

offset=15
length=$(expr $offset + 3)

token="\'OTM2MzUwMDM5NDY1NDE0Njg4.YfL57Q.ZJsuWn9URvRcCJzV9KhWywkYReg\'"
channel_id=936016370628435978
moodle_id="\'afva3166\'"
moodle_pass="\'GreenTea9696\'"

function add() {
  payload=$offset
  payload+=i
  echo $payload
}

cp -f ./bot.py ./hoge.py
sed -e "$offset,$length d" hoge.py > fuga.py
cat fuga.py | sed $(add)TOKEN=$token > hoge.py
cat hoge.py | sed $(add)CHANNEL_ID=$channel_id > fuga.py
cat fuga.py | sed $(add)MOODLE_ID=$moodle_id > hoge.py
cat hoge.py | sed $(add)MOODLE_PASSWORD=$moodle_pass > test.py
rm hoge.py
rm fuga.py
python3 ./test.py
