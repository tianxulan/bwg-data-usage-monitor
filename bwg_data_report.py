import bwg_usage_lookup as bul
import yaml
GB_TO_BYTE_FACTOR = 1073741824
from datetime import datetime,timedelta
import pytz
from string import Template
def main():
    # Read user config
    with open("local_config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    # bwg lookup 
    lookup_result = bul.bwg_lookup(config)
    processed_result = data_process(lookup_result) 
    # compose email  
    with open('email_body.txt', 'r') as f:
        src = Template(f.read())
        email_body = src.substitute(processed_result)
        print(email_body)
    

# Process lookup result
# INPUT-[lookup_result]:<Dict> Processed response from bwg api
# OUTPUT: <Dict> Processed result
def data_process(lookup_result):
    result = {}
    # information
    result["hostname"] = lookup_result["hostname"]
    # time
    now_pst = datetime.now()
    result["time_now_pst"] = now_pst.strftime("%B %d, %Y %H:%M:%S")
    cst_tz = pytz.timezone("Asia/Shanghai")
    result["time_now_cst"] = now_pst.astimezone(cst_tz).strftime("%B %d, %Y %H:%M:%S")
    reset_pst = datetime.fromtimestamp(lookup_result["data_next_reset"])
    result["time_reset_pst"] = reset_pst.strftime("%B %d, %Y %H:%M:%S")
    result["time_reset_cst"] = reset_pst.astimezone(cst_tz).strftime("%B %d, %Y %H:%M:%S")
    
    # get cycle start to reset date
    first = reset_pst.replace(day=1)  
    lastMonth = first - timedelta(days=1)
    start_pst = lastMonth.replace(day=reset_pst.day)
    result["date_start_pst"] = start_pst.strftime("%m/%d/%Y")
    result["date_start_cst"] = start_pst.astimezone(cst_tz).strftime("%m/%d/%Y")
    result["date_reset_pst"] =  reset_pst.strftime("%m/%d/%Y")
    result["date_reset_cst"] =  reset_pst.astimezone(cst_tz).strftime("%m/%d/%Y")
    days_cycle = reset_pst - start_pst
    result["days_cycle"] = str(days_cycle.days)
    days_passed = now_pst - start_pst
    result["days_passed"] = str(days_passed.days)
    result["days_passed_percent"] = "{:.1f}".format(days_passed.days/days_cycle.days * 100) + "%"
    # get days counter

    # data used
    data_used_GB = lookup_result["data_counter"] / GB_TO_BYTE_FACTOR
    data_total_GB = lookup_result["plan_monthly_data"] * lookup_result["monthly_data_multiplier"] / GB_TO_BYTE_FACTOR 
    data_used_percent = (data_used_GB / data_total_GB) * 100
    result["data_used_GB"] = "{:.2f}".format(data_used_GB)
    result["data_total_GB"] = "{:0.0f}".format(data_total_GB)
    result["data_remain_GB"] = "{:.2f}".format(data_total_GB - data_used_GB)
    result["data_used_percent"] = "{:.2f}".format(data_used_percent) + "%"
    return result 

if __name__ == "__main__":
    main()