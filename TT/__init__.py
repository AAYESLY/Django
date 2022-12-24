import pymysql
# pymysql.version_info = (1, 3, 13, "final", 0) # 遇到mysql-client版本的报错的临时解决，不能保证框架不出现问题（不建议）
pymysql.install_as_MySQLdb()