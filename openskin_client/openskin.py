"""Small entry points around the generated OpenSkin client."""

from .api_client import ApiClient
from .configuration import Configuration

PRODUCTION_BASE_URL = "https://api-v2.openskin.dev"
V2_TEST_BASE_URL = "https://api-v2-v2-test.up.railway.app"


def client(api_key: str, base_url: str = PRODUCTION_BASE_URL) -> ApiClient:
    """Create an API client. Use it as an async context manager."""
    configuration = Configuration(host=base_url)
    configuration.api_key["PlatformAPIKey"] = api_key
    return ApiClient(configuration)
