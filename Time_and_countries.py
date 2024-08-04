from datetime import datetime

def country_gmt_timing(country_name):
    country_gmt_data={2:["southafrica","sweden","botswana","hesse","eswatini","libya","mozambique","namibia","albania","andorra","angoala","rwanda","sudan","zambia","zimbabwe","austria","belguim","bosnia","congo","czechia","denmark","france","germany","gibraltar","hungary","italy","kosovo","liechtenstion","monaco","morocco","netherland","nigeria","poland","sanmarino","serbia","slovakia","slovenia","spain","norway","swizerland","vaticancity"],
        1:["ireland","england","gabon","algeria"],3:["egypt","turkey","tanzania","russia","finland","bulgaria","estonia","greece","israel","jordan","lithuania","palestine","romania","syria","ukraine","belarus","comoros",
        "djibouti","eritria","ethopia","iraq","kenya","kuwait","madagascar","qatar","somalia","uganda","yemen"],
        4:["armenia","azerbaijan","mauritius","seychelles","unitedarabemirates","uae","oman"],
        5:["kazakhstan","maldivies","pakistan","afganistan","tajikistan","uzbekistan","india","srilanka"],
        6:["burma","bangladesh","bhutan","kyrgyztan","nepal"],7:["thailand","cambodia","indonesia","vietnam"],8:['singapore','taiwan',"philippines","mongolia","malaysia","china"],9:["palau","japan","korea"],10:["australia","papuanewguinea"],11:["vanuata","micronesia"],12:["newzealand","marshallisland","kribati","fiji"],0:["burkanifaso","gambia","iceland"],-1:["portugal"],-3:["suriname","chile"],-4:["usa","canada","hanover","georgia","venezuela","brazil","bahamas","haiti","dominica","cuba","bolivia"],-5:["texas","ecuadar","jamaica","mexixo","panama","peru"],-10:["Hawaii"]
    }
    for gmt in country_gmt_data:
        if country_name in country_gmt_data[gmt]:
            return gmt
def country_exact_clock(country_gmt_timing):
    gmt=datetime.now()
    
    gmt_hour=gmt.hour
    
    gmt_minutes=gmt.minute
    half_hour_data=["india","srilanka","afganistan","burma"]
    if country_name in half_hour_data:#condition or adding half hour
        country_hour,country_minutes=add_half_hour(gmt_minutes,gmt_hour)
    else:
        country_hour=country_gmt_timing+gmt_hour
        country_minutes=gmt_minutes
    country_hour,date=date_and_time(country_hour)
    
    am_pm_timing,country_hour=am_pm(country_hour)
    final=final_date_and_time(country_hour,country_minutes,am_pm_timing,date,gmt)
def date_and_time(country_hour):
    
    date=0
    if country_hour>=24:
        country_hour-=24
        date=+1
    if country_hour<0:
        country_hour=24+country_hour
        date=-1
    
    return country_hour,date
def am_pm(country_hour):
    print(country_hour)
    if country_hour>=12:
        
        if country_hour==12:
            return "PM",country_hour
        else:
            country_hour=country_hour%12
            return "PM",country_hour
        
    else:
        return "AM",country_hour
def day_finder(date,month,year):
    last_two_digit_year=int(year[2:])
    year_remainder=last_two_digit_year//4
    month_code=[0,0,3,3,6,1,4,6,2,5,0,3,5]
    year_code=2
    weekdays=['Sunday',"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    sum=(year_remainder+last_two_digit_year+month_code[month]+year_code)%7
    return weekdays[sum]


def final_date_and_time(country_hour,country_minutes,am_pm,date,gmt):
     print("Country_Name:",country_name)
     date=gmt.day+date
     month=gmt.month
     year=gmt.year
     day=day_finder(date,month,str(year))
     print("Day:",day)
     print("Date:{}-{}-{}".format(date,month,year))
     print("Time:{}:{}:{} {}".format(country_hour,country_minutes,gmt.second,am_pm))
     
    
        
def add_half_hour(gmt_minutes,gmt_hour):
        country_minutes=gmt_minutes+30
        if country_minutes>60:#minutes should be less than 60
            add_hour=country_minutes//60#if the minutes is greater than 60 we should consuder it a hour
            country_minutes=country_minutes%60#the remaining minutes
            country_hour=gmt_hour+country_gmt_timing+add_hour
        else:
            country_hour=gmt_hour+country_gmt_timing
        return country_hour,country_minutes
    
    
    
    

#execution
print("Enter the name of the country")
country_name=input().lower()
country_gmt_timing=country_gmt_timing(country_name)
exact_timing=country_exact_clock(country_gmt_timing)

