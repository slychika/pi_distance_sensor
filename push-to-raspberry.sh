SENSOR1_IP="10.102.1.4"
SENSOR2_IP="10.102.1.3"
TARGET_PATH="pi_distance_sensor/"

scp distanceSense.py pi@$SENSOR1_IP:$TARGET_PATH
scp distanceSense.py pi@$SENSOR2_IP:$TARGET_PATH
