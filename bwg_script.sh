#!/bin/bash
cd /root/bwg-data-usage-monitor
/usr/local/bin/python3.9 /root/bwg-data-usage-monitor/bwg_data_report.py | mailx -s "New BWG Data Monitoring Report" foo@bar.com