# Software workshop #2: control all the thingz!

## Step-by-step guide

### Get workshop files and configure our tools

1. Open a new window of VS Code
2. On the `Source Code` tab (left-most navbar), click `Clone repository` and enter the following URL:
    
    ```bash
    https://github.com/gramaziokohler/workshop_ds_2023.git
    ```
    
3. When asked, selected the destination folder where you want to clone the repository, e.g. `Documents`, and click `Open` when the process completes.
4. Open a terminal (can be directly inside VS Code) and run the following from the folder in which you cloned the repository:

```bash
conda env create -f environment.yml
```

1. Make sure VS Code is setup for our workshop:
    1. Installed extensions: Python, GitLens, and CircuitPython (for the microcontroller)
    2. Terminal profile is set to `cmd` (if you see yellow text in the terminal, it means it’s not set correctly to `cmd`)
    3. Select the environment created in the previous step (you need to open a Python file for that)

### Exercises

1. The format of the workshop is split into `listening` vs `coding` times. For each of the subtopics, the context and the solution will be shown briefly, and then you’ll have time to practice it on your machine.
2. For the exercises with microcontrollers (raspberry pi pico), **pair with another person and work together**.
3. Most exercises have a solution provided and a starting point / template to code on top.

* `01_scripts`: the first exercises shows the basic principles of event-based communication using publisher/subscriber using an in-memory transport. Then, moves into using an external MQTT transport, which means now the communication can happen between separate process, or even computers!
* `02_grasshopper`: follows the same principles as previous examples, but now the sending side is Grasshopper.
* `03_mcu`: we start with the microcontroller! We are using a Raspberry Pi Pico that runs CircuitPython on it. There are several different examples of code to run on the microcontroller. Running code on this microcontroller is as simple as opening the `code.py` file in the drive that appears on own computer when the device is connected over USB, and simply save. The code will start right away.
* `04_web_and_text`: these are two examples of creating web and text applications is a very simple way.

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
