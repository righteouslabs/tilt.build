### AUTO-GENERATED ###
# This file was auto-generated by 'tilt dump api-docs' as part of a Tilt release.
# To make changes, modify the following file in the Tilt repository:
#   internal/tiltfile/api/sys/__init__.py
# Generated by Tilt version v0.33.11, built 2024-02-15
### AUTO-GENERATED ###

from typing import List

argv: List[str] = []
"""The list of command line arguments passed to Tilt on start.

`argv[0]` is the Tilt binary name.
"""

executable: str = ""
"""A string giving the absolute path of the Tilt binary.

Based on how Tilt was originally invoked. There is no guarantee that
the path is still pointing to a valid Tilt binary. If the path has
a symlink, the behavior is operating system dependent.
"""
