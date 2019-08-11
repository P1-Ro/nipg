# Index page generator for [nginx](https://www.nginx.com/)
This tool helps you to generate index page for nginx. This page will contain all locations which you configure, be it proxy_pass or static files.

## Installation
1. Clone this repo 
    ```
    mkdir /opt/nipg
    git clone https://github.com/P1-Ro/nipg.git /opt/nipg
    ```

2. Install dependecies
    ```
   pip3 install -r /opt/nipg/requirements.txt
   ```

3. Install service 
    ```
    sudo cp /opt/nipg/nipg.service /etc/systemd/system/
    ```
   :warning: **If you cloned it to different location you also need to change paths in `nipg.service`**

4. Start service and enable it on boot
    ```
   systemctl start nipg && systemctl enable nipg
   ```

## Configuration
For this generator to function properly your nginx needs to be setup in specific but easy way
### nginx configuration
1. Copy proxy configuration. This configuration will be shared by location which use proxy_pass
    ```
   cp ./nginx_example/proxy.conf /etc/nginx/
    ```
2. Include following line in `default` coonfiguration of nginx
    ```
   include sites-available/services.conf;
    ```
3. In sites available create `services.conf` with content like this
    ```
   location /your_location/ { # Description which will be shown in index page
        proxy_pass        <your url here>;
        include           proxy.conf;
    }
   ```
   
   Only locations which have `{` followed by `#` will be included in index page.
   Text which follows after `#` server as description to given location (optional).
   
   For more examples see `nginx_example` folder.

### App configuration
Apps generate index page from templates present in templates folder.
When modifying templates `{{links}}` tags needs to be present on place when you want to include generated links.

When modyfying link template these self-explanatory tags needs to be present: `{{name}}, {{link}}, {{description}} `

## Usage
With service started an enabled app watches `sites-available` folder and if there are any changes it creates new index.html page in `/var/www/html`.

## Preview
![Screenshot of web interface](https://github.com/P1-Ro/nipg/blob/master/preview.png)