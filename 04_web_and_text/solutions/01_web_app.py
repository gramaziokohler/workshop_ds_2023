import getpass

import streamlit as st
from compas_eve import Message, Publisher, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport

st.markdown("# Robots 🤖")
st.write("This accepts **markdown** syntax!")

value = st.slider("Angle:", min_value=0, max_value=135)
st.write("Updating servo to ", value)

host = "broker.hivemq.com"
set_default_transport(MqttTransport(host=host))

topic = Topic("/workshop_ds/values/" + getpass.getuser(), Message)

publisher = Publisher(topic)
publisher.publish(Message(value=value))
