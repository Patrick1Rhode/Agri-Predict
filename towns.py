import MySQLdb
db = MySQLdb.connect("localhost","root","","zambia_weather")
hello ='Mwiza'
x = """CREATE TABLE IF NOT EXISTS %s (
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;"""  % hello

cursor = db.cursor()
cursor.execute(x)

    sql = cursor.execute("INSERT INTO chililabombwe VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
    0, cloud, condition_text, code, condition_icon, temperature, humidity, wind_degree, wind_dir, wind_speed, localtime,
    region, tz_id))
    db.commit()