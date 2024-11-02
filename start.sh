#!/bin/bash

# Atualiza o locale para português
apt-get update && apt-get install -y locales
locale-gen pt_BR.UTF-8
update-locale LANG=pt_BR.UTF-8

# Inicia o bot
python main.py
