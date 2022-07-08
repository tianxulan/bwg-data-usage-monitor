import bwg_usage_lookup as bul
import yaml
GB_TO_BYTE_FACTOR = 1073741824
from datetime import datetime,timedelta
import pytz
def main():
    # Read user config
    with open("local_config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    # bwg lookup and compose email
    # lookup_result = bul.bwg_lookup(config)
    lookup_result = {'hostname': 'Abandonments', 'plan_monthly_data': 1073741824000, 'monthly_data_multiplier': 1, 'data_counter': 946972627, 'data_next_reset': 1659829465}
    processed_result = data_process(lookup_result)
    compose_subject(lookup_result)
    compose_body(lookup_result)

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
    result["date_start_pst"] = start_pst.strftime("%B %d, %Y")
    result["date_start_cst"] = start_pst.astimezone(cst_tz).strftime("%m/%d/%Y")
    result["date_reset_pst"] =  reset_pst.strftime("%B %d, %Y")
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
    result["data_used_percent"] = "{:.2f}".format(data_used_percent) + "%"
    
# Compose the subject of email
# INPUT-[data]:<Dict> Processed result
# OUTPUT: <String> the subject of email 
def compose_subject(data):
    subject_string = f"BWG Data Monitor: 25/1000 GB(2.5%) used" 


# Compose the body of email
# INPUT-[data]:<Dict> Processed result
# OUTPUT: <String> the body of email 
def compose_body(data):
    body_string = ""
    


if __name__ == "__main__":
    main()