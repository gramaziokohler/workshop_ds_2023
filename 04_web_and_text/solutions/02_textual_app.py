import getpass

from compas_eve import Message, Publisher, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.validation import Number
from textual.widgets import Button, Header, Input, Label, Markdown

EXAMPLE_MARKDOWN = """\
# Robots

Interestingly enough, `Textual` also supports Markdown for app design.

This app is a pure text-based (ie terminal) app!
But it still suppors mouse, and a lot of other unusual features for a text-based app.

---
"""


class WorkshopDistributedSystemsApp(App):
    CSS = """
    Label {
        margin: 1 4;
    }
    Horizontal {
        margin: 0 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Vertical(
            Header(show_clock=True),
            Markdown(EXAMPLE_MARKDOWN),
            Label("Enter an even number between 1 and 100 that is also a palindrome."),
            Input(
                placeholder="Enter a number between 0 and 135...",
                validators=[
                    Number(minimum=0, maximum=135),
                ],
            ),
            Horizontal(
                Button("Send", variant="primary"),
                Button.error("Quit"),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if str(event.button.label) == "Quit":
            self.exit()
        elif str(event.button.label) == "Send":
            topic = Topic("/workshop_ds/values/" + getpass.getuser(), Message)

            publisher = Publisher(topic)
            publisher.publish(Message(value=float(self.query_one(Input).value)))


if __name__ == "__main__":
    host = "broker.hivemq.com"
    set_default_transport(MqttTransport(host=host))

    app = WorkshopDistributedSystemsApp()
    app.run()
