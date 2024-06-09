#!/bin/bash

KEY_PATH=$1

eval $(ssh-agent -s)
ssh-add $KEY_PATH
ssh -T git@hf.com