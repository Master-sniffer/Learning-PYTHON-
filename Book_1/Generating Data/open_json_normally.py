import json

filename='eq_data_1_day_m1.json'
with open (filename) as f:
  all_ed_data=json.load(f)
readable_file= 'readable_json_file.json'
with open (readable_file, 'w') as f:
  json.dump(all_ed_data, f, indent=4)


