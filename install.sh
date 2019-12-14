mkdir /opt/nipg
git clone https://github.com/P1-Ro/nipg.git /opt/nipg
pip install -r /opt/nipg/requirements.txt
ln -s /opt/nipg/nipg.service /etc/systemd/system/

ln -s /opt/nipg/nginx_example/proxy.conf /etc/nginx/
ln -s /opt/nipg/nginx_example/services.conf /etc/nginx/sites-available
ln -s /opt/nipg/nginx_example/default /etc/nginx/default

systemctl start nipg && systemctl enable nipg && systemctl reload nipg
systemctl reload nginx
