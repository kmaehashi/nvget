|Travis|_

.. |Travis| image:: https://api.travis-ci.org/kmaehashi/nvget.svg?branch=master
.. _Travis: https://travis-ci.org/kmaehashi/nvget

nvget
=====

A script to download assets from `NVIDIA Developer <https://developer.nvidia.com/>`_ website.
You need to have a valid NVIDIA Developer account, have enrolled to the program required to download the asset and have agreed with the terms of the corresponding license agreement.

Requirements
------------

* Python 2.7, 3.3, 3.4, 3.5 or 3.6
* Google Chrome (with headless support)
* ChromeDriver

See ``Dockerfile`` for the detailed setup procedures.

Run Using Docker
----------------

It is recommended to run ``nvget`` using the Docker image hosted on `DockerHub <https://hub.docker.com/r/kmaehashi/nvget/>`__, as it's a bit tough work to install Google Chrome and ChromeDriver correctly.

::

  # Pull images from DockerHub.
  docker pull kmaehashi/nvget

  # Set NVIDIA Developer credentials to the environment variable, and add alias.
  # These steps are just for convenience; add these lines to your ``.bashrc``.
  export NVGET_USER="your.email@example.net"
  export NVGET_PASSWORD="p@ssw0rd"
  alias nvget-docker='docker run --rm -e NVGET_USER -e NVGET_PASSWORD -u "${UID}" -v "${PWD}:/download" kmaehashi/nvget'

  # Download the file.
  nvget-docker "https://developer.nvidia.com/compute/machine-learning/nccl/secure/v2.1/prod/nccl_2.1.2-1+cuda8.0_x86_64"

Development
-----------

Modify the local ``nvget`` source tree and ``docker build -t nvget-dev -f Dockerfile-dev .`` to build new image for testing.

License
-------

MIT License
