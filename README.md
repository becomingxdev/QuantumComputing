<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">QUANTUMCOMPUTING</h1></p>
<p align="center">
	<em><code>❯ becomingxdev</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/becomingxdev/QuantumComputing?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/becomingxdev/QuantumComputing?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/becomingxdev/QuantumComputing?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/becomingxdev/QuantumComputing?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>❯ This repository contains the Python-based microservice for the Q-Crypt project. Its primary function is to simulate the BB84 Quantum Key Distribution (QKD) protocol and generate a secure, one-time quantum key for the main chat application. It also features a built-in intrusion detection mechanism to check for eavesdroppers</code>

---

##  Features

<code>❯ Quantum Key Generation: Simulates the BB84 protocol to create a shared, secret key. Eavesdropper Detection: Calculates a quantum bit error rate (QBER) to detect potential security breaches during key exchange. RESTful API: Exposes a simple HTTP endpoint that the main application can call to request a key. Lightweight and Modular: Designed as a microservice, making it easy to integrate with any backend system.</code>

---

##  Project Structure

```sh
└── QuantumComputing/
    ├── LICENSE
    ├── README.md
    ├── bb84.py
    ├── main.py
    ├── pythonFundamentals1.py
    ├── quantum_intro.py
    └── requirements.txt
```


###  Project Index
<details open>
	<summary><b><code>QUANTUMCOMPUTING/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/becomingxdev/QuantumComputing/blob/master/pythonFundamentals1.py'>pythonFundamentals1.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/becomingxdev/QuantumComputing/blob/master/bb84.py'>bb84.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/becomingxdev/QuantumComputing/blob/master/main.py'>main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/becomingxdev/QuantumComputing/blob/master/quantum_intro.py'>quantum_intro.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/becomingxdev/QuantumComputing/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with QuantumComputing, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install QuantumComputing using one of the following methods:

**Build from source:**

1. Clone the QuantumComputing repository:
```sh
❯ git clone https://github.com/becomingxdev/QuantumComputing
```

2. Navigate to the project directory:
```sh
❯ cd QuantumComputing
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run QuantumComputing using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/becomingxdev/QuantumComputing/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/becomingxdev/QuantumComputing/issues)**: Submit bugs found or log feature requests for the `QuantumComputing` project.
- **💡 [Submit Pull Requests](https://github.com/becomingxdev/QuantumComputing/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/becomingxdev/QuantumComputing
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/becomingxdev/QuantumComputing/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=becomingxdev/QuantumComputing">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.

---

##  Acknowledgments

- All the things in this repository are learned and created by Dev Hitesh Desai. Learned from Gemini AI. All the resources used here opensourced. Thank You for hearing me out.

---
