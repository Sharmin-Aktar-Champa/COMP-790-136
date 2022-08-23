from unicodedata import name
import requests, json, pprint

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRUTkiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNjYxMzUwODMzLCJpYXQiOjE2NjA3NDYwMzN9.-6KKpR38nXavOTwsBrJBKuMQD3thwGeFDguLTMiOPM0"

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
    myurl  = "https://api.fitbit.com/1/user/-/activities/heart/date/2022-08-20/1d/5min.json"
    resp  = requests.get(url=myurl, headers=myheader).json()
    #print(resp)
    activity_heart = resp['activities-heart']
    jsn_str = activity_heart[0]
    value  = jsn_str['value']
    restingHeartRate  = value['restingHeartRate']
    return restingHeartRate

def get_steps(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/today.json"
    resp = requests.get(url=myurl, headers=myheader).json()
    summary = resp['summary']
    steps = summary['steps']
    return  steps

def get_sleep(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl = ""
    resp = requests.get(url=myurl, headers=myheader).json()
    return None

def get_activeness(token):
    myheader = {"Authorization":"Bearer "+token}
    myurl = ""
    resp = requests.get(url=myurl, headers=myheader).json()
    return None

print('Printing some random jokes\n')
print_jokes()
print("\n")
get_activity_steps(token)
print("\n")
name = get_name(token)
print("User's name is {}\n".format(name))
HR = get_hearrate(token)
print("{}'s resting heart rate is {} BPM".format(name, HR))
steps = get_steps(token)
print('{} walked {} steps today\n'.format(name, steps))