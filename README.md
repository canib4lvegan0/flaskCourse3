## Repository dedicated to study of RESTFull with Flask

Python


### Digital Ocean CLI

#####[nginx running and status]
- sudo systemctl (status, reload, stop, start, restart) nginx

#####[nginx config]
- sudo vi /etc/nginx/sites-enabled/items-rest.conf

#####[uwsgi running]
- sudo systemctl (reload, stop, start, restart) uwsgi_items_rest

#####[uwsgi service config]
- sudo vi /etc/systemd/system/uwsgi_items_rest.service

#####[logs]
- sudo vi /var/www/html/items-rest/log/uwsgi.log
- sudo vi /var/www/html/items-rest/log/emperor.log
- sudo vi /var/log/nginx/access.log