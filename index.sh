#!/bin/bash
mv 'task.py' 'file_operations'

sudo chmod +x 'file_operations'
sudo cp 'file_operations' '/usr/bin/'
alias 'file_operations'='python3 file_operations'


cd ..
sudo rm -r file_operations
