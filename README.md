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
    api_key = os.environ.get("OPENSKIN_API_KEY")
    if not api_key:
        raise RuntimeError("set OPENSKIN_API_KEY before running")

    async with client(api_key) as api_client:
        platform = openskin_client.PlatformV2Api(api_client)
        account = await platform.get_v2_principal()
        print(account.tier)


asyncio.run(main())
```

The client uses `https://api-v2.openskin.dev` by default. Create an API key in
the [OpenSkin dashboard](https://platform.openskin.dev/dashboard).

See the [API reference](https://platform.openskin.dev/docs/platform) for the
available operations. Requests and responses are typed with Pydantic.
Endpoints that require `Idempotency-Key` or `If-Match` expose those headers as
required method arguments.

Licensed under the MIT License.
