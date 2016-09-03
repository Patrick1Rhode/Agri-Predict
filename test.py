from apixu.client import ApixuClient, ApixuException
import rethinkdb as r
import json
import csv

api_key = 'd2fa8368108944eda2e81337160309'
client = ApixuClient(api_key)
#db = MySQLdb.connect("localhost", "root", "", "zambia_weather")
#cursor = db.cursor()

#Database connection from rethinkdb
conn = r.connect('localhost', 28015).repl()


# Town names array, helps to grab the data for each specific town.
towns_one = ['Chadiza', 'Chama', 'Chavuma', 'Chembe', 'Chibombo', 'Chiengi', 'Chililabombwe', 'Chilubi', 'Chingola', 'Chinsali']
towns_two = ['Chipata', 'Chirundu', 'Choma', 'Gwembe', 'Isoka', 'Kabwe', 'Kafue', 'Kalabo']
towns_three = ['Kalomo', 'Kaoma', 'Kapiri', 'Kasama', 'Kasempa', 'Kataba', 'Katete', 'Kawambwa', 'Kazembe']
towns_four = ['Kazungula', 'Kitwe', 'Livingstone', 'Luangwa', 'Luanshya', 'Lukulu', 'Lundazi']
towns_five = ['Lusaka', 'Maamba', 'Makeni', 'Mansa', 'Mazabuka', 'Mbala', 'Mbereshi', 'Milenge']
towns_six = ['Mkushi', 'Mongu', 'Monze', 'Mpika', 'Mporokoso', 'Mpulungu', 'Mufulira', 'Mumbwa', 'Muyombe']
towns_seven = ['Mwinilunga', 'Nchelenge', 'Ndola', 'Ngoma', 'Nkana', 'Pemba', 'Petauke', 'Samfya', 'Senanga']
towns_eight = ['Serenje', 'Sesheke', 'Shiwa', 'Ngandu', 'Siavonga', 'Sikalongo', 'Sinazongwe', 'Solwezi', 'Zambezi', 'Zimba']

towns = towns_one + towns_two + towns_three + towns_four + towns_five + towns_six + towns_seven + towns_eight

for x in towns:
    print x
    current = client.getCurrentWeather(q=x)
    
    #r.db('test').table_create('weather_2').run()
    ''' tables = """CREATE TABLE IF NOT EXISTS %s (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `cloud` int(5) DEFAULT NULL,
          `condition_text` varchar(20) DEFAULT NULL,
          `condition_code` int(5) DEFAULT NULL,
          `icon` text,
          `temperature` float DEFAULT NULL,
          `humidity` int(5) DEFAULT NULL,
          `wind_degree` int(5) DEFAULT NULL,
          `wind_dir` varchar(5) DEFAULT NULL,
          `wind_kph` float DEFAULT NULL,
          `localtime` text,
          `region` varchar(30) DEFAULT NULL,
          `tz_id` varchar(50) DEFAULT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;""" % x

    cursor = db.cursor()
    cursor.execute(tables) '''

    # Data from API
    cloud = current['current']['cloud']
    code = current['current']['condition']['code']
    condition_icon = current['current']['condition']['icon']
    condition_text = current['current']['condition']['text']
    humidity = current['current']['humidity']
    temperature = current['current']['temp_c']
    wind_degree = current['current']['wind_degree']
    wind_dir = current['current']['wind_dir']
    wind_speed = current['current']['wind_kph']
    localtime = current['location']['localtime']
    region = current['location']['region']
    tz_id = current['location']['tz_id']

    r.table("weather").insert({
       
        "cloud": cloud,
        "code": code,
        "condition_icon": condition_icon,
        "condition_text": condition_text,
        "humidity": humidity,
        "temperature": temperature,
        "wind_degree": wind_degree,
        "wind_dir": wind_dir,
        "wind_speed": wind_speed,
        "localtime": localtime,
        "region": region,
        "tz_id": tz_id
    }).run(conn)
    


