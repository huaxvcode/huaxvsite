# Ubuntu 安装 MySQL

```bash
sudo apt-get update

sudo apt-get install mysql-server

sudo mysql_secure_installation

sudo systemctl status mysql

sudo systemctl start mysql

sudo systemctl enable mysql
```

```sql
CREATE USER 'huaxvubuntu'@'localhost' IDENTIFIED BY 'huaxvubuntu';

ALTER USER 'huaxvubuntu'@'localhost' IDENTIFIED BY 'huaxvubuntu';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'huaxvubuntu';

mysql -u huaxvubuntu -p
sudo mysql -u root -p
```
