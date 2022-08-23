import time
from unicodedata import name
import requests, json, pprint

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSNkIiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMjk1NDQ0LCJpYXQiOjE2NjA3NTk0NDR9.bILcGIrPRXPWRrWBZDKRLsZdtTKKqPUpZ4NZZ-U3k5g"

def print_jokes():
    resp = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    x = json.loads(resp.text)
    print(x["joke"])
    return None

def get_activity_steps(token):
    myheader = {"Authorization": "Bearer"+ " " + token}
    myurl = "https://api.fitbit.com/1/user/-/activities/steps/date/2022-08-16/7d.json"
    getSteps = requests.get(url=myurl, headers=myheader).json()
    pprint.pprint(getSteps)
    return None

def get_name(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl = "https://api.fitbit.com/1/user/-/profile.json"
    getProfile = requests.get(url=myurl, headers=myheader).json()
    user = getProfile["user"]
    name = user["fullName"]
    return name

def get_hearrate(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl  = "https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json"
    resp  = requests.get(url=myurl, headers=myheader).json()
    activity_heart = resp['activities-heart']
    jsn_str = activity_heart[0]
    value  = jsn_str['value']
    restingHeartRate  = value['restingHeartRate']
    heart_rate_log = resp['activities-heart-intraday']['dataset']
    recent_heart_rate = heart_rate_log[-1]
    t = time.strptime(recent_heart_rate['time'], "%H:%M:%S")
    timevalue_12hour = time.strftime( "%I:%M %p", t)
    heart_rate = recent_heart_rate['value']
    return timevalue_12hour, heart_rate

def get_steps(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/today.json"
    resp = requests.get(url=myurl, headers=myheader).json()
    summary = resp['summary']
    steps = summary['steps']
    return  steps

def get_sleep(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl = "https://api.fitbit.com/1.2/user/-/sleep/list.json?beforeDate=today&sort=desc&offset=0&limit=3"
    resp = requests.get(url=myurl, headers=myheader).json()
    sleep_log = resp['sleep']
    if sleep_log[0]['isMainSleep']==True:
        recent_main_sleep = sleep_log[0]
    elif sleep_log[1]['isMainSleep']==True:
        recent_main_sleep = sleep_log[1]
    else:
        recent_main_sleep = sleep_log[2] 
    return recent_main_sleep['minutesAsleep']

def get_activeness(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/today.json"
    resp = requests.get(url=myurl, headers=myheader).json()
    sedentary = resp['summary']['sedentaryMinutes']
    very_active = resp['summary']['veryActiveMinutes']
    active = resp['summary']['fairlyActiveMinutes']+resp['summary']['lightlyActiveMinutes']+resp['summary']['veryActiveMinutes']
    return sedentary, very_active, active


today = time.strftime("%Y-%m-%d")

print('Printing some random jokes\n')
print_jokes()

print("\n")
get_activity_steps(token)

name = get_name(token)
print("\nUser's name is {}\n".format(name))

timestamp, HR = get_hearrate(token)
print("{}'s most recent heart rate recorded at {} is {} beats per minute\n".format(name, timestamp, HR))

steps = get_steps(token)
print('{} walked {} steps today\n'.format(name, steps))

sleeps = get_sleep(token)
hour, min = divmod(sleeps, 60)
print('{} slept for {} hours and {} minutes last night.\n'.format(name, hour, min))

sedentary, very_active, active = get_activeness(token)
sH, sM = divmod(sedentary, 60)
vaH, vaM = divmod(very_active, 60)
aH, aM = divmod(active, 60)
print('Today, {} were sedentary for {} hours {} mins'.format(name, sH, sM))
print('and active for {} hours {} minutes with {} hours {} minutes in the very high activity zone'.format(aH, aM, vaH, vaM))