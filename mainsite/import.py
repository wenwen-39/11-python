import csv,sys,os
project_dir = './mainsite/'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'wen.settings'
import django
django.setup()
from mainsite.models import company
data = csv.reader(open("./mainsite/data.csv",encoding="utf-8"),delimiter=",",)
for row in data:
    if row[0] !='time':
        unit = company()
        unit.time = row[0]
        unit.place = row[1]
        unit.dead = row[2]
        unit.Injured = row[3]
        unit.car = row[4]
        unit.longitude = row[5]
        unit.latitude = row[6]
        unit.save()