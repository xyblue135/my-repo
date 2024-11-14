# mysql
https://hub.docker.com/_/
```
version: '3.8'  # 指定Docker Compose文件的版本

services:
  mysql:
    image: mysql:8.0
    container_name: mysql
    environment:
      - MYSQL_ROOT_PASSWORD=123456
      - MYSQL_DATABASE=devops
      - MYSQL_USER=aliang
      - MYSQL_PASSWORD=123456
    volumes:
      - /home/0000/var/lib/mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```
编辑一个docker-compose.yml文件然后docker-compose up d