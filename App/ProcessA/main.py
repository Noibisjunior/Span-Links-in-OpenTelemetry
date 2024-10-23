# app/service_a/main.py
from flask import Flask, request, jsonify
import requests
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Set up Flask app
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

# Set up OpenTelemetry tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(span_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Define a route for processing user data
@app.route('/process', methods=['POST'])
def process_request():
    user_data = request.json.get('data')
    with tracer.start_as_current_span("Service A Processing") as span:
        span.set_attribute("user.data", user_data)
        # Send data to Service B
        response = requests.post("http://localhost:5001/complete", json={"data": user_data})
        span.add_event("Sent request to Service B")
    return jsonify({"status": "Processed", "response": response.json()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
