#IP="172.16.29.77"
IP="172.16.29.33"
TARGET_PATH="pi_distance_sensor/"

scp -r * pi@$IP:$TARGET_PATH
