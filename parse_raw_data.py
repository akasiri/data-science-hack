import json
app_usage_events_column = 'entry_date device_id application_version_id type start_date run_time end_date continuation'.split()
application_versions_column = 'application_version_id package_name name version develop'ype catergor

def txt_parse(file_path):
    ls = []
    with open(file_path, "r") as f:
        for line in f:
            print(line)
            l = []
            for token in str(line).split(','):
                l.append(token)
            ls.append(l)
    return ls

def build_dict(raw_data):
    did_device = dict()
    for row in raw_data:
        did_device[row[0]] = row[1:]
    return did_device

if __name__ == "__main__":
    with open("device_dict.json", "w") as f:
        device_dict = build_dict(txt_parse("../M2C Final Data/devices.csv"))
        f.write(json.dumps(device_dict))
    with open("log_list.json", "w") as f:
        log_list = txt_parse("../M2C Final Data/log_data/.csv")
        f.write(json.dumps(device_dict))
    with open("app_list.json", "w") as f:
        log_list = txt_parse("../M2C Final Data/application_versions.csv")
        f.write(json.dumps(device_dict))
