import mysql.connector


class Good:
    id = 0
    name_cn = ''
    name_en = ''
    barcode = ''
    category = ''
    production_date = None
    expiry_date = None
    image = ''
    cost_price = 0.0
    selling_price = 0.0
    type = ''
    expiry_notification_date = None
    inventory = 0



# 建立数据库连接
cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='mydatabase')

# 创建查询
cursor = cnx.cursor()
query = ("SELECT * FROM goods")

# 执行查询
cursor.execute(query)

# 遍历结果集并创建 Good 实例
goods_list = []
for row in cursor:
    good = Good()
    good.id = row[0]
    good.name_cn = row[1]
    good.name_en = row[2]
    good.barcode = row[3]
    good.category = row[4]
    good.production_date = row[5]
    good.expiry_date = row[6]
    good.image = row[7]
    good.cost_price = row[8]
    good.selling_price = row[9]
    good.type = row[10]
    good.expiry_notification_date = row[11]
    good.inventory = row[12]
    goods_list.append(good)

# 关闭连接
cursor.close()
cnx.close()
