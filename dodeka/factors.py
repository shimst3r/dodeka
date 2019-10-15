"""
Copyright (c) 2019, Nils P. Müller <shimst3r@gmail.com>
All rights reserved.

This file is part of dodeka.

`factors.py` implements the functionality for generating the
twelve-factor app checklist.

License: MIT, see https://opensource.org/licenses/MIT
"""

from typing import List, Tuple


def generate_factors() -> List[Tuple[str, str]]:
    """
    generate_factors returns a list of tuples containing the twelve factors.

    >>> generate_factors()[0]
    ("I. Codebase", "One codebase tracked in revision control, many deploys") 
    """
    return [
        ("I. Codebase", "One codebase tracked in revision control, many deploys"),
        ("II. Dependencies", "Explicitly declare and isolate dependencies"),
        ("III. Config", "Store config in the environment"),
        ("IV. Backing services", "Treat backing services as attached resources"),
        ("V. Build, release, run", "Strictly separate build and run stages"),
        ("VI. Processes", "Execute the app as one or more stateless processes"),
        ("VII. Port binding", "Export services via port binding"),
        ("VIII. Concurrency", "Scale out via the process model"),
        (
            "IX. Disposability",
            "Maximize robustness with fast startup and graceful shutdown",
        ),
        (
            "X. Dev/prod parity",
            "Keep development, staging, and production as similar as possible",
        ),
        ("XI. Logs", "Treat logs as event streams"),
        ("XII. Admin processes", "Run admin/management tasks as one-off processes"),
    ]
