# Check-staking-Energi

Check staking Energi is a simple script that checking staking work and in case of errors send e-mail.

# Requirements

- Linux
- Python3 with smtplib
- Energi Core Wallet with staking running

# Installation

- download latest stable version from [this website](https://github.com/DocBox12/Check-staking-Energi/releases)
- extract archive
- move to **src** directory
- execute `chmod +x main.py` command
- fill **config.ini**
- add script to cron

# Config.ini description

[SMTP]
address - SMTP server name or IP
username - SMTP username
password - SMTP password
port - SMTP port
from - from which e-mail the message should be sent
to - e-mail address for the notification
[MESSAGE]
topic - message topic

[ENERGI]
core_path - path to `enegli-cli` program. Example: `/home/username/energicore-2.1.2/bin/energi-cli`

# Support

If you like this script then you can help me send some Energi! Wallet: **Eeoc9ejemURmQKPYaW9byaD3Bx2z1Hb9gb**

# Links

[Energi cryptocurrency website](https://www.energi.world/)
