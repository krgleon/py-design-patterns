# Represents the final HTTP request object
class HttpRequest:
    def __init__(self, method, url, headers=None, params=None, body=None):
        # Store basic components of an HTTP request
        self.method = method
        self.url = url
        self.headers = headers or {}  # Default to empty dict if None
        self.params = params or {}
        self.body = body

    def send(self):
        # Simulated sending of the HTTP request
        # In a real-world app you'd use libraries like requests or httpx
        return f"Sending {self.method} to {self.url} with headers={self.headers}, params={self.params}, body={self.body}"

# Builder class to incrementally construct an HttpRequest
class HttpRequestBuilder:
    def __init__(self, method: str, url: str):
        # Initialize with required fields
        self._method = method
        self._url = url
        # Optional parts start empty or None
        self._headers = {}
        self._params = {}
        self._body = None

    # Adds a header to the request
    def add_header(self, key: str, value: str):
        self._headers[key] = value
        return self  # Enables method chaining

    # Adds a query parameter
    def add_param(self, key: str, value: str):
        self._params[key] = value
        return self

    # Sets the request body
    def set_body(self, content: str):
        self._body = content
        return self

    # Final step: build and return the HttpRequest instance
    def build(self) -> HttpRequest:
        return HttpRequest(
            method=self._method,
            url=self._url,
            headers=self._headers,
            params=self._params,
            body=self._body
        )

# Example usage:
# Build a POST request with headers, a body, and a query parameter
request = (
    HttpRequestBuilder("POST", "https://api.example.com/users")
    .add_header("Authorization", "Bearer token123")         # Add auth token
    .add_header("Content-Type", "application/json")         # Set content type
    .set_body('{"name": "Khronozg"}')                       # Provide JSON body
    .add_param("verbose", "true")                           # Add query parameter
    .build()                                                # Build final HttpRequest
)

# Simulate sending the request
print(request.send())
