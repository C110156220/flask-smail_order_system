import pymysql , datetime

        
def select(db,type=None,id=None):
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='frywhat')
    if type =='con':
        sql = "SELECT * FROM `%s`" % db
    elif type != None:
        sql = "SELECT fd_id,name,price FROM `%s` WHERE type = '%s' ; " % (db,type)
    else:
        if id != None:
            sql = "SELECT fd_id,name,price FROM `%s` where fd_id=%d" % (id)
        else:
            sql = "SELECT fd_id,name,price FROM `%s`" % (db)
    cursor = conn.cursor()
    cursor.execute(sql)
    r = cursor.fetchall()
    cursor.close()
    conn.close()
    return r 

    
    # conn('cur').close()
    # result = conn('cur').fetchall()
    # conn('con').close()
    # return result
    

def delete(who,id):
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='frywhat')

    if who == 'boss':
        sql = "DELETE FROM fdlist WHERE `fdlist`.`fd_id` = %d" % (id)
    elif who == 'cus':
        sql = "DELETE FROM fdorder WHERE `fdorder`.`order_id` = %d" % (id)
    else :
        print('error')
        return 'error'
    cursor = conn.cursor()
    print(sql)
    cursor.execute(sql)
    conn.commit()
    print('ok')
    cursor.close()
    conn.close()
    return 1


def update(arg):
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='frywhat')
    sql="UPDATE `fdlist` SET `type` = \'%s\', `name` = \'%s\', `price` = %d WHERE `fdlist`.`fd_id` = %d;" % (arg[1],arg[2],int(arg[3]),int(arg[0]))
    print(sql)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return 1 

def insert(db,*value):
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='frywhat')

    cursor = conn.cursor()
    if db == 'fdlist':
        sql = "INSERT INTO `fdlist` (`fd_id`, `type`, `name`, `price`) VALUES (NULL,\'%s\',\'%s\',\'%s\');" %(value[0],value[1],value[2])
        return
    elif db == 'fdorder':
        t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print(t)
        sql = "INSERT INTO `fdorder` (`order_id`, `時間`, `訂單內容`) VALUES (NULL,\'{}\',\'{}\');".format(str(t),value[0])
        print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return 1 
        except Exception  :
            print(Exception)
            return 0

