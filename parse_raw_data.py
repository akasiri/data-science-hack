import json

def txt_parse(file_path):
    ls = []
    with open(file_path, "rb") as f:
        for line in f:
            l = []
            for token in str(line).strip().split(','):
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
    with open("log_9-1_list.txtdata", "w") as f:
        log_list = txt_parse("../M2C Final Data/log_data/log_data_2015_09_01.csv")
        f.write(json.dumps(log_list))
    with open("app_list.txtdata", "w") as f:
        app_list = txt_parse("../M2C Final Data/application_versions.csv")
        f.write(json.dumps(app_list))
