# BWG Data Monitor 
A python script to check Bandwagon data usage and generate a text report. Use the report with mail/mailx and crontab to send daily/weekly report to your inbox. 
## Requirement
* Python 3.6+
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
    Subject: New BWG Data Monitoring Report
    Body:
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
        
