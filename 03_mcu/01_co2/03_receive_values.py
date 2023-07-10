import time

from compas_eve import Message, Subscriber, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport


# TODO: Follow the same structure as 02_grasshopper\02_receive_values
# with the following differences:
#  1. Create a CO2Subscriber instead of a ValueSubscriber
#  2. When subscribing to the topic, use the following name: `/workshop_ds/sensors/co2/#`
