from setuptools import setup

setup(
    name="nxbt",
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=[
        "dbus-python",
        "Flask",
        "Flask-SocketIO",
        "eventlet==0.33.3",
        "blessed==1.17.10",
        "pynput==1.7.1",
        "psutil==5.6.6",
        "cryptography",
        "jinja2",
        "itsdangerous",
        "Werkzeug",
    ],
    extra_require={
        "dev": [
            "pytest"
        ]
    }
)
