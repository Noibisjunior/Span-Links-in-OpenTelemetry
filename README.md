Mastering Trace Analysis with Span Links using openTelemetry and Signoz (A Practical Guide)

Overview

This repository provides a complete guide and code example for understanding and implementing span links with OpenTelemetry and visualizing them using SigNoz. 
Span links allow you to connect related spans across different traces, making it easier to analyze complex service interactions, especially in distributed systems.

In this tutorial, you'll learn:

1. How to set up OpenTelemetry instrumentation in Python.
2. How to create and link spans between services.
3. How to configure SigNoz for monitoring and trace visualization.
4. How to interpret trace graphs using span links to gain insights into service dependencies.

Prerequisites
Python 3.7+
Docker (for running SigNoz)
Basic knowledge of microservices and distributed tracing concepts

Getting Started

```bash
# Clone the repository
git clone https://github.com/Noibisjunior/Span-Links-in-OpenTelemetry.git 


# Navigate to the project directory
cd Span-Links-in-OpenTelemetry


#Navigate to each service directory and install the required dependencies:
cd app/ProcessA

# Install dependencies
pip install -r requirements.txt

cd ../ProcessB
pip install -r requirements.txt
```

3. Set Up SigNoz
Ensure that Docker is running on your machine. Then, follow the instructions:

`docker run -p 3301:3301 -p 4317:4317 -p 4318:4318 -p 8080:8080 \`
    `-v ~/signoz-data:/data \`
    `--name signoz \`
    `signoz/signoz:latest`

Visit `http://localhost:3301` to access the SigNoz dashboard

4. Start the Services
Run each service in separate terminal windows:

```bash
# In the ProcessA directory
python main.py

# In the ProcessB directory
python main.py
```

```bash
Repository Structure
exploring-opentelemetry-span-links/
├── README.md
├── ProcessA/
│   ├── main.py
│   └── requirements.txt
├── ProcessB/
│   ├── main.py
│   └── requirements.txt
└── .gitignore
```
Contributing
Contributions are welcome! If you have suggestions or improvements, 
feel free to open an issue or submit a pull request.

Contact
For any questions or support, feel free to reach out to [Noibisjunior22@gmail.com].

