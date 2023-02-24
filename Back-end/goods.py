import mysql.connector
from flask import Flask, request, jsonify
import pymysql

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



app = Flask(__name__)

# 创建数据库连接
db = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='store',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 新增商品的路由
@app.route('/products', methods=['POST'])
def add_product():
    # 获取请求中的商品信息
    product = request.json
    if not product:
        return jsonify({'error': 'Missing product information'}), 400
    
    # 向商品数据表插入新记录
    try:
        with db.cursor() as cursor:
            sql = """
            INSERT INTO products (name_cn, name_en, barcode, category, production_date, expiry_date, image_url, cost_price, selling_price, stock)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                product.get('name_cn'),
                product.get('name_en'),
                product.get('barcode'),
                product.get('category'),
                product.get('production_date'),
                product.get('expiry_date'),
                product.get('image_url'),
                product.get('cost_price'),
                product.get('selling_price'),
                product.get('stock')
            ))
            db.commit()
            # 获取新记录的 ID 并返回
            product_id = cursor.lastrowid
            return jsonify({'id': product_id}), 201


