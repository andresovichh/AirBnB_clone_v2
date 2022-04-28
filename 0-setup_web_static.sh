#!/usr/bin/env bash
# Script that install nginx
sudo apt-get update
sudo apt-get -y install nginx
echo "Hello World" > /var/www/html/index.nginx-debian.html
sudo service nginx start
sudo sed -i '/listen \[::\]:80 default_server;/a\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default
sudo sed -i '/listen \[::\]:80 default_server;/a\\tadd_header X-Served-By \"\$HOSTNAME\";' /etc/nginx/sites-available/default
sudo sed -i '/TGUlwu4 permanent;$/a\\terror_page 404 /custom_404.html;' /etc/nginx/sites-available/default
echo "Ceci n'est pas une page" >/var/www/html/custom_404.html
sudo service nginx restart
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello from RayBar!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
exit 0
