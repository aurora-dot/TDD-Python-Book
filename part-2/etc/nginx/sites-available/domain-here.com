server {
    listen 80;
    server_name domain-here.com;

    location /static {
        alias /home/elspeth/sites/domain-here.com/static;
    }

    location / {
        proxy_pass http://unix:/tmp/domain-here.com.socket;
        proxy_set_header Host $host;
    }
}