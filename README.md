# Index page generator for [nginx](https://www.nginx.com/)
This tool helps you to generate index page for nginx. Resulting page will contain all locations, no matter if it's proxy_pass or static file.

## Installation
### Automatic
    
    curl https://raw.githubusercontent.com/P1-Ro/nipg/master/install.sh | sudo bash

### Manual

1. Clone this repo 
    ```
    mkdir /opt/nipg
    git clone https://github.com/P1-Ro/nipg.git /opt/nipg
    ```

2. Install service 
    ```
    sudo ln -s /opt/nipg/nipg.service /etc/systemd/system/
    ```
   :warning: **If you cloned it to different location you also need to change paths in `nipg.service`**

4. Copy nginx configuration
    ```
       sudo ln -s /opt/nipg/nginx_example/proxy.conf /etc/nginx/
    ```

4. Start service
    ```
   systemctl start nipg 
   ```
   If you want to reload nginx configuration and re-generate index page run `systemctl start nipg`

## Configuration
For this generator to function properly your nginx needs to be setup in specific but easy way (done automatically with install script)

1. Include following line in `default` configuration of nginx
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

### Output customization
Tool generates index page from templates present in templates folder.
When modifying templates `{{links}}` tags needs to be present on place when you want to include generated links.

When modifying link template these self-explanatory tags needs to be present: `{{name}}, {{link}}, {{description}} `

## Usage
With service started an enabled tool watches `sites-available` folder and if there are any changes it creates new index.html page in `/var/www/html`.

## Preview
![Screenshot of web interface](https://github.com/P1-Ro/nipg/blob/master/preview.png)
