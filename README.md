# dash-jetnoise
Post to stop.jetnoise.net with one button via Amazon IoT

Use ```zip -r upload.zip report.py requests requests-2.9.1.dist-info``` to make bundle to upload to lambda

### if you have an amazon IoT device
1. connect your Amazon IoT device to Amazon IoT and select a new function
2. enter your own cookie and uuid data
3. upload this as your lambda function on amazon iot dev

### if you don't and wish to use a different trigger, or eventually connect
1. enter your own cookie and uuid data
2. upload this as your lambda function on amazon iot dev
3. connect your Amazon IoT device or different trigger and select this function
