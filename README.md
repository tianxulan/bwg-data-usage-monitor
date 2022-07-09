# BWG Data Monitor 
A python script to check Bandwagon data usage and generate a text report. 
## Requirement
* Python 3.9
## How to use
1. Download source code
2. Install Dependecey

        pip3 install -r requirements.txt
3. Replace placeholder with your **veid** and **api_key** in *config.yaml* 

        veid: <your veid>
        api_key: <your api key>
4. Run the script

        python3 bwg_data_report.py

## How report looks like
    Abstract: 25/1000 GB(2.5%) used while 3.3% days of this cycle has passed.
    Request Time: July 10, 2022 03:22:22
    Hostname:hostname
    Total Data: 1000 GB
    Used Data: 0.88 GB
    Percent Used: 0.09%
    Data Remaining: 999.12 GB
    Current Cycle: 07/07/2022 - 08/07/2022
    Data Reset Time: August 07, 2022 07:44:25
    Days counter:2/31 days
    *Note: All times use the timezone on your server.

## (Optinal)Do even more with the report
* You can send this report with mail/mailx on your server 

        python3 bwg_data_report.py | mailx -s "New BWG Data Monitoring Report" foo@bar.com

* add *bwg_script.sh* to [crontab](https://linux.die.net/man/5/crontab) so your server could automate the process (8AM Everyday)

        0 8 * * * bash bwg_script.sh
    * To use the bwg_script.sh, you need to modify the script and configure your own path. Same for crontab.