# Cat Detector
Motion detector with Telegram controls and notifications used to spy on my cats when I'm not at home.
## Requirements
- Webcam
- Telegram bot
- Chat ID
- Docker

### Webcam
Any webcam recognized by the computer will work, it is streamed in http://0.0.0.0:8888
### Telegram bot
To control and receive notifications, you will need to create a Telegram bot (using ___Botfather___ bot in Telegram for example https://t.me/botfather).
### Chat ID
You don't want other people to be monitoring and viewing your cats' photos, so you'll need to create a chat on Telegram, add your bot and get the ___chat ID___ (there are many bots in Telegram that returns your ___chat ID___ like https://telegram.im/@rawdatabot).
### Docker
Just run the image with:
~~~bash
docker run -e BOT_TOKEN=YOUR_BOT_TOKEN -e CHAT_ID=YOUR_CHAT_ID ghcr.io/r-dvl/cat-detector:latest
~~~
And now enjoy watching them destroy your home.

<img src="https://i.gyazo.com/fd2e902c259fb6a44b80e83b58c6c787.jpg" alt="Crazy cats detected" width="376" height="647"/>
