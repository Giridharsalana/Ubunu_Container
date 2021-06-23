docker run -d \
  --name=webtop \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 3000:3000 \
  -v /workspace/Ubunu_Conatiner/WebTop:/config:z \
  --shm-size="4gb" \
  --restart unless-stopped \
  ghcr.io/linuxserver/webtop:ubuntu-xfce