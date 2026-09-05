# OpenSkin Python SDK

Async Python client for the OpenSkin Platform API. Python 3.10 or newer is
required.

## Install

```sh
pip install openskin-client
```

## Example

```python
import asyncio
import os

import openskin_client
from openskin_client.openskin import client


async def main() -> None:
    async with client(os.environ["OPENSKIN_API_KEY"]) as api_client:
        platform = openskin_client.PlatformV2Api(api_client)
        health = await platform.get_v2_health()
        print(health.status)


asyncio.run(main())
```

The client uses `https://api-v2.openskin.dev` by default. Create an API key in
the [OpenSkin dashboard](https://platform.openskin.dev/dashboard).

Requests and responses are typed with Pydantic. Required headers such as
`Idempotency-Key` and `If-Match` are method arguments.

Licensed under the MIT License.
