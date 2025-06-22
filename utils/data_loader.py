import csv
import json
import os
from datetime import datetime

# def load_users_from_csv(filepath):
#     with open(filepath, newline='') as f:
#         reader = csv.DictReader(f)
#         users = [row for row in reader]
#         for u in users:
#             u['Username'] += datetime.now().strftime("_%H%M%S")
#         return users

# def load_users_from_json(filepath):
#     with open(filepath) as f:
#         users = json.load(f)
#         for u in users:
#             u['Username'] += datetime.now().strftime("_%H%M%S")
#         return users
    

def load_users_from_csv(filepath):
    users = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            new_user = row.copy()
            new_user['Username'] += datetime.now().strftime("_%H%M%S")
            users.append(new_user)
    return users

def load_users_from_json(filepath):
    users = []
    with open(filepath) as f:
        data = json.load(f)
        for row in data:
            new_user = row.copy()
            new_user['Username'] += datetime.now().strftime("_%H%M%S")
            users.append(new_user)
    return users