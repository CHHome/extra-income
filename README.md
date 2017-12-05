# extra-income
毕业设计 --外包项目网站 -- vue+python+flask+uwsgi+uginx




## 启动步骤：
### 启动后台：
1. cd back 
2. virtualenv --no-site-packages extra_env
3. pip install -r requirements.txt 
4. python run.py
> 以上开启后台dev环境
5. uwsgi extra_uwsgi.ini
6. sudo ln -s /home/genhongchan/code/python_web/extra-income/back/extra_nginx.conf  /etc/nginx/conf.d/
7. sudo /etc/init.d/nginx start

> 以上开启pro环境，开启uwsgi+nginx **5-7为本人Ubuntu启动方式,pro环境下忽略3**


### 启动前端：
1. cd front
2. npm install
3. npm run dev
> 以上开启前端dev环境
4. npm run build

> 以上开启前端pro环境，**pro环境下忽略3**

