import getpass
import time

from compas_eve import Message, Subscriber, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport


class ValueSubscriber(Subscriber):
    def message_received(self, message):
        print("Received value: {}".format(message.value))


def main():
    host = "broker.hivemq.com"
    set_default_transport(MqttTransport(host=host))

    topic = Topic("/workshop_ds/values/" + getpass.getuser(), Message)

    subscriber = ValueSubscriber(topic)
    subscriber.subscribe()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        subscriber.unsubscribe()


if __name__ == "__main__":
    main()
