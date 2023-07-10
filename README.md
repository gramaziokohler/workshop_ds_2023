# Software workshop #2: control all the thingz!

## Step-by-step guide

### Get workshop files and configure our tools

1. Open a new window of VS Code
2. On the `Source Code` tab (left-most navbar), click `Clone repository` and enter the following URL:
    
    ```bash
    https://github.com/gramaziokohler/workshop_ds_2023.git
    ```
    
3. When asked, select the destination folder where you want to clone the repository, e.g. `Documents`, and click `Open` when the process completes.
4. Open a terminal (can be directly inside VS Code) and run the following command from the folder in which you cloned the repository:

```bash
conda env create -f environment.yml
```

1. Make sure VS Code is setup for our workshop:
    1. Installed extensions: Python, GitLens, and CircuitPython (for the microcontroller)
    2. Terminal profile is set to `cmd` (if you see yellow text in the terminal, it means it’s not set correctly to `cmd`) [Only Windows]
    3. Select the environment created in the previous step (you need to have any Python file open in VS Code for the selector to appear)

### Exercises

1. The format of the workshop is split into `listening` vs `coding` times. For each of the subtopics, the context and the solution will be shown briefly, and then you’ll have time to practice it on your machine. It's recommended that, even if the solutions are available, you **re-type them**, instead of copy&paste them.
2. For the exercises with microcontrollers (Raspberry Pi Pico), **pair with another person and work together**.
3. Most exercises have a starting point / template to guide you, and additionally there is the full solution provided (in the `solutions` folder of each topic).

* `01_scripts`: the initial exercises shows the basic principles of event-based communication using publisher/subscriber with an in-memory transport (default). Then, it moves on to using an external MQTT transport. This enables communication between separate process and even separate computers!
* `02_grasshopper`: follows the same ideas as previous examples, but now the sending side is Grasshopper.
* `03_mcu`: we start with the microcontroller! We are using a Raspberry Pi Pico (not the same as a Raspberry Pi!) that runs CircuitPython on it. This board has no operating system at all, it's not a computer. There are several different examples of code to run on the microcontroller. Running code on this microcontroller is as simple as opening the `code.py` file in the drive that shows up on `File Explorer` (or `Finder`)  when the device is connected over USB, and simply save. Every time you save, the code will start right away. **No compile time!**
* `04_web_and_text`: finally, we have two examples of creating web-based and terminal-based applications is a very simple way using `Streamlit` and `Textual` respectively.

---

## `compas_eve`: Event extensions for COMPAS

This is a new COMPAS package that facilitates event-based communication. It works on both CPython and IronPython.

There are 4 main concepts:
* **Topic**: it's a named "mailbox". The name of a topic looks like a path with components separated by slashes. We can send (ie. publish) messages to a topic without knowing or caring who will receive it. This concept is represented by the `Topic` class in `compas_eve`.
* **Publisher**: sends messages to a topic. The class `Publisher` represents this concept. You can use the class directly, or alternatively, you can create a subclass and implement the method `message_published(self, message)` to be able to handle or do custom stuff when a message is published.
* **Subscriber**: receives messages from a topic. The class `Subscriber` represents this concept. To handle received messages, create a subclass and implement the method `message_received(self, message)`.
* **Transport**: defines the way in which messages are transported from publishers to subscribers. By default, `compas_eve` uses an in-memory transport, ie. it only works for a single process, but it's useful for testing. To use a transport that works across processes, computers, networks, galaxies, use a different one, like `MqttTransport`.

---

## Terminology

- A **distributed system** is a system whose components are located on different networked computers, which communicate and coordinate their actions by [passing messages](https://en.wikipedia.org/wiki/Message_passing) to one another.
- A **queue** is a 1-to-1 destination of messages. The message is received by only one of the consuming receivers. Messages sent to a queue are stored on disk or memory until someone picks it up or it expires.
- A **bus** is a 1-to-many model of distribution. The destination in this model is usually called topic. The same published message is received by all consuming subscribers. You can also call this the 'broadcast' model. For topic's the message delivery is 'fire-and-forget' - if no one listens, the message just disappears.

## Benefits

- Producers and consumers are decoupled.
- No point-to-point integrations. It's easy to add new consumers to the system.
- Consumers can respond to events immediately as they arrive.
- Highly scalable and distributed.
- Subsystems have independent views of the event stream.

## Disadvantages

- New failure modes

## Milestones to go through the workshop

- Script to script communication
- Grasshopper to script [and vice-versa] communication
- Control a remote microcontroller
- Retrieve data from sensors
- Web and Text apps
