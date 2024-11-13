# backend/swagger_config.py
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Real Estate Price Prediction API",
        "description": "API documentation for real estate price prediction",
        "version": "1.0.0"
    }
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/",
}
