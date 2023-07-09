import getpass
import time

from compas_eve import Message, Subscriber, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport


class CO2Subscriber(Subscriber):
    def message_received(self, message):
        print("CO2: " + str(message.value))


def main():
    host = "broker.hivemq.com"
    set_default_transport(MqttTransport(host=host))

    topic = Topic("/workshop_ds/sensors/co2/" + getpass.getuser(), Message)

    subscriber = CO2Subscriber(topic)
    subscriber.subscribe()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
