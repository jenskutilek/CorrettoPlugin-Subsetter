from __future__ import annotations

from pathlib import Path
from sys import path, version_info

import objc
from GlyphsApp.plugins import GeneralPlugin

py_ok = False
if version_info.major == 3:
    if version_info.minor in (10, 11, 12, 13):
        cor_path = Path(__file__).parent / f"CorrettoSubsetter3{version_info.minor}.zip"
        path.append(str(cor_path))
        py_ok = True

if not py_ok:
    from GlyphsApp import Message

    Message(
        f"Python version {version_info.major}.{version_info.minor} "
        "is not supported by Corretto Subsetter."
    )


class CorrettoSubsetterPlugin(GeneralPlugin):
    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
