# Disable stricter default verify flags (X509_STRICT, X509_PARTIAL_CHAIN) introduced in Python 3.13.
# https://docs.python.org/3/library/ssl.html#:~:text=The%20context%20now%20uses%20VERIFY_X509_PARTIAL_CHAIN%20and%20VERIFY_X509_STRICT%20in%20its%20default%20verify%20flags.

import ssl

_old_create_default_context = ssl.create_default_context

def _new_create_default_context(*args, **kwargs):
    ctx = _old_create_default_context(*args, **kwargs)
    if hasattr(ssl, "VERIFY_X509_STRICT"):
        ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT
    if hasattr(ssl, "VERIFY_X509_PARTIAL_CHAIN"):
        ctx.verify_flags &= ~ssl.VERIFY_X509_PARTIAL_CHAIN
    return ctx

ssl.create_default_context = _new_create_default_context
