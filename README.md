# Safe-Snack-Dispenser

**Group Members:** Sai Vedagiri, Albert Zou, and Abhay Rao

## Design Description
Our design for approaching the Safe Snack Dispenser mini-project involves the use of a Raspberry Pi 4 to power functionality. With an ultrasonic sensor and a motor, the dispenser is completely hands-free and simply requires a waving motion in front of the sensor to have an M&M dispensed. On top of this, our group would like to implement a JavaScript website in the Raspberry Pi and add natural language processing functionality to trigger the dispenser with just a command like, “Dispense!”. In other words, we would like to allow voice commands to help visually-impaired users.

## Functionality
To start, the user has two ways of dispensing an M&M, hovering his or her hand close to the ultrasonic sensor or saying the word “dispense”. If a hand is placed near the ultrasonic sensor, it will detect an object within close proximity and trigger a Python script to dispense one M&M by rotating the servo appropriately. When the servo turns, the bottle cap is designed to automatically passively reload the filter with another M&M and the filter is designed to drop an M&M into the tray or other apparatus placed below the product. When words are said in proximity to the microphone, the microphone will pick up the audio and send it to a locally running Code OSS live server on port 5500. This server will parse this audio in realtime and display the text on the screen (used for debugging purposes only) and look for the term “dispense”. If the term is detected, it will change the color of the text on the webpage to green and send a request to the Python Flask server which is also being run locally on port 80. This Flask server will take this request and move the servo an appropriate amount, similar to the way it would dispense if triggered with the ultrasonic. At the conclusion of this motion, it will send back a response, stating that the action was complete. To prevent abuse of this system, it will cancel out any duplicate invocations of the dispense commands within 3 seconds of one another.

## Usage
Visit [this website](https://dispenser.saivedagiri.com) to view the code in action.
