# app/service_b/main.py
from flask import Flask, request, jsonify
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

# Define a route for completing the task
@app.route('/complete', methods=['POST'])
def complete_task():
    user_data = request.json.get('data')
    with tracer.start_as_current_span("Service B Completion") as span:
        span.set_attribute("user.data", user_data)
        
        # Create a span link if there is a trace context from Service A
        parent_context = trace.get_current_span().get_span_context()
        span.add_link(trace.Link(parent_context))
        
        span.add_event("Data processed in Service B")
    return jsonify({"status": "Completed", "processed_data": user_data})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
