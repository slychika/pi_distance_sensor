#IP="10.102.1.3"
IP="10.102.1.4"
TARGET_PATH="pi_distance_sensor/"

scp -r * pi@$IP:$TARGET_PATH
