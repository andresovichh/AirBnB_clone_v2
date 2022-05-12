"/data/web_static/releases/test/"
 )
# create directories
 for i in "${dirs[@]}"
 do
 if [[ ! -f "$i" ]]
 then
 sudo mkdir -p "$i"
 fi
 done

# create html
if [[ ! -f "/data/web_static/releases/test/index.html" ]]
then
sudo touch "/data/web_static/releases/test/index.html"
echo "Hola Andres" > /data/web_static/releases/test/index.html
fi
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
"0-setup_web_static.sh" 40L, 1076C                       33,21         75%