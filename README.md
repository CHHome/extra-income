# extra-income
毕业设计 --外包项目网站 -- vue+python+flask+uwsgi+uginx




## 启动程序：
### 启动后台：
1. cd back 
virtualenv --no-site-packages extra_env
2. pip install -r requirements.txt 
3. python run.py走起
> 以上开启后台dev环境
4. uwsgi extra_uwsgi.ini
5. sudo ln -s /home/genhongchan/code/python_web/extra-income/back/extra_nginx.conf  /etc/nginx/conf.d/
6. sudo /etc/init.d/nginx start

> 以上开启product环境，开启uwsgi+nginx **4-6为本人Ubuntu启动方式,pro环境下忽略3**


### 启动前端：
1. cd front
2. npm install
3. npm run dev走起
> 以上开启前端dev环境
4. npm run build

> 以上开启前端pro环境，**pro环境下忽略3**

