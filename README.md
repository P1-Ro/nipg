# Index page generator for [nginx](https://www.nginx.com/)
This tool helps you to generate index page for nginx. This page will contain all locations which you configure, be it proxy_pass or static files.

## Installation
### Automatic
    ```
    curl https://raw.githubusercontent.com/P1-Ro/nipg/master/install.sh | sudo bash
    ```

### Manual

1. Clone this repo 
    ```
    mkdir /opt/nipg
    git clone https://github.com/P1-Ro/nipg.git /opt/nipg
    ```

2. Install dependecies
    ```
   pip install -r /opt/nipg/requirements.txt
   ```

3. Install service 
    ```
    sudo ln -s /opt/nipg/nipg.service /etc/systemd/system/
    ```
   :warning: **If you cloned it to different location you also need to change paths in `nipg.service`**

4. Copy nginx configuration
    ```
       sudo ln -s /opt/nipg/nginx_example/proxy.conf /etc/nginx/
    ```

4. Start service and enable it on boot
    ```
   systemctl start nipg && systemctl enable nipg
   ```
   If service is already running and you want to force generation use `systemctl reload nipg`

## Configuration
For this generator to function properly your nginx needs to be setup in specific but easy way

1. Include following line in `default` coonfiguration of nginx
    ```
   include sites-available/services.conf;
    ```
2. In `\etc\nginx\sites-available\services.conf` put anything which you want to proxy pass
    ```
   location /your_location/ { # Description which will be shown in index page
        proxy_pass        <your url here>;
        include           proxy.conf;
    }
   ```
   
   Only locations which have `{` followed by `#` will be included in index page.
   Text which follows after `#` server is description to given location (optional).

### App customization
Apps generate index page from templates present in templates folder.
When modifying templates `{{links}}` tags needs to be present on place when you want to include generated links.

When modyfying link template these self-explanatory tags needs to be present: `{{name}}, {{link}}, {{description}} `

## Usage
With service started an enabled app watches `sites-available` folder and if there are any changes it creates new index.html page in `/var/www/html`.

## Preview
![Screenshot of web interface](https://github.com/P1-Ro/nipg/blob/master/preview.png)
