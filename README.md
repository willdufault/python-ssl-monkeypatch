# python-ssl-monkeypatch

Compatability monkeypatch to disable the stricter default SSL verify flags (X509_STRICT, X509_PARTIAL_CHAIN) introduced in Python 3.13.  
[Python ssl docs](https://docs.python.org/3/library/ssl.html#:~:text=The%20context%20now%20uses%20VERIFY_X509_PARTIAL_CHAIN%20and%20VERIFY_X509_STRICT%20in%20its%20default%20verify%20flags.)
