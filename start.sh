#!/bin/bash

function checkSetUp {
  if [ $? -ne 0 ]; then
    sudo bash shell/setUpEnv.sh
    python main.py
  fi
}

python main.py

checkSetUp

