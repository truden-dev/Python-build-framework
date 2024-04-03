"""Main program"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Auth:
    """Cognite auth parameters"""

    tenant_id: str | None = os.getenv("TENANTID")
    project: str | None = os.getenv("PROJECT")
    base_url: str | None = os.getenv("BASEURL")
    token: str | None = os.getenv("TOKEN")


def main():
    """Main function"""
    my_auth: Auth = Auth()
    print(my_auth)
    print("This is a welcome message")


if __name__ == "__main__":
    main()
