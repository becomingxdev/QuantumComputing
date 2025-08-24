#Q-Crypt Python Key Generator

<p>This repository contains the Python-based microservice for the Q-Crypt project. Its primary function is to simulate the BB84 Quantum Key Distribution (QKD) protocol and generate a secure, one-time quantum key for the main chat application. It also features a built-in intrusion detection mechanism to check for eavesdroppers.</p>

📋 Table of Contents
Features

Technical Stack

Installation and Setup

API Endpoint Usage

Underlying Principles (BB84 Protocol)

Contribution

License

✨ Features
Quantum Key Generation: Simulates the BB84 protocol to create a shared, secret key.

Eavesdropper Detection: Calculates a quantum bit error rate (QBER) to detect potential security breaches during key exchange.

RESTful API: Exposes a simple HTTP endpoint that the main application can call to request a key.

Lightweight and Modular: Designed as a microservice, making it easy to integrate with any backend system.

💻 Technical Stack
Python: The core programming language.

Flask: A lightweight web framework used to create the API endpoint.

Qiskit: IBM's open-source framework for working with quantum computers and simulators.

🚀 Installation and Setup
Follow these steps to get the service running locally.

Clone the Repository

git clone https://github.com/your-username/q-crypt-python-backend.git
cd q-crypt-python-backend

Create a Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

Run the Service
Start the Flask server.

flask run

The service will now be running on http://127.0.0.1:5000.

🔗 API Endpoint Usage
The service exposes a single GET endpoint.

Endpoint: /generate_key

Method: GET

Response:

Success: A JSON object containing the generated key and the intrusion status.

{
  "key": "1011010100101110...",
  "status": "secure"
}

Intrusion Detected: The status will indicate a security breach.

{
  "key": null,
  "status": "eavesdropper_detected"
}

⚛️ Underlying Principles (BB84 Protocol)
The BB84 protocol is a quantum cryptography protocol that enables two parties (typically named Alice and Bob) to create a shared, random, secret key. It works by encoding bits of information onto polarized "photons."

Preparation: Alice generates a random stream of bits and randomly selects a basis (rectilinear + or diagonal x) for each bit.

Transmission: She sends these polarized photons to Bob.

Measurement: Bob, who does not know the bases Alice used, randomly chooses a basis for each photon and measures its state.

Sifting: Alice and Bob publicly compare the bases they used for each photon. They discard any measurements where their bases did not match.

Key Generation: The remaining bits, where their bases matched, form the final secret key.

Crucially, if an eavesdropper ("Eve") tries to intercept and measure the photons, they will be forced to guess the basis. This measurement will alter the state of the photon, introducing a detectable error rate in the final key.

🤝 Contribution
We welcome contributions! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.