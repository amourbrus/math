import pymysql

localhost = '172.31.9.229'  # eth0
conn = pymysql.connect(host=localhost,
                       port=3306,
                       user='root',
                       passwd='123456',
                       db='midatadb',
                       charset='utf8')

# sql = """select uid from midatadb.r_application ap
# left join midatadb.r_pic_verify_dispatch rpvd on ap.id = rpvd.application_id
# where ap.status = 12 and ap.country_id = 4 and ap.auth_source = 0 and (rpvd.channel = 1 or rpvd.channel is null)"""

sql = """select uid from midatadb.r_application where country_id=4  """

# 获取游标
cursor = conn.cursor()
print("data %s" % cursor.execute(sql))
print("data %s" % cursor.fetchone())