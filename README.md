# bwg-data-usage-monitor
A python script to check Bandwagon data usage and report result to your email. Use  crontab to run this script on a daily/weekly basic to monitoring your data useage without visiting KiwiVM Panel. 

## How report looks like
    Subject: BWG Data Monitor: 25/1000 GB(2.5%) used
    Body:
        2.5% data has been used while this cycle has passed 3.3%.
        Request Time(CST) : 1970/01/02 
        Hostname:hostname
        Total Data: 1000 GB
        Used Data: 25 GB
        Percent Used: 2.5%
        Data Remaining:975 GB
        Data Reset Time: 1970/01/01 (CST)
        Days counter:1/30 Days
        Timezone info: Request Time(PST) = 1970/1/1, Data Reset Time(PST) = 1970/2/1
        
