
## // Define the LED pin
const int ledPin = 13; // Most Arduinos have an onboard LED on pin 13

void setup() {
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  
  // Start serial communication at 9600 baud rate
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming byte
    char receivedChar = Serial.read();

    // Check the received command
    switch (receivedChar) {
      case 'H': // Turn the LED on
        digitalWrite(ledPin, HIGH);
        Serial.println("LED turned ON");
        break;
      case 'L': // Turn the LED off
        digitalWrite(ledPin, LOW);
        Serial.println("LED turned OFF");
        break;
      // Add more cases here for other commands
      default:
        // If the command is unrecognized, send an error message
        Serial.print("Error: Unknown command - ");
        Serial.println(receivedChar);
        break;
    }
  }
}
