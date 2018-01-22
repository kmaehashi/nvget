nvget
=====

A script to download assets from `NVIDIA Developer https://developer.nvidia.com/`_ website.
You need to have a valid NVIDIA Developer account, have enrolled to the program required to download the asset and have agreed with the terms of the corresponding license agreement.

Requirements
------------

* Python 2.7, 3.3, 3.4, 3.5 or 3.6
* Google Chrome (with headless support)
* ChromeDriver

Run Using Docker
----------------

::

  docker pull kmaehashi/nvget
  export NVGET_USER="your.email@example.net"
  export NVGET_PASSWORD="p@ssw0rd"
  alias nvget-docker='docker run --rm -e NVGET_USER -e NVGET_PASSWORD -u "${UID}" -v "${PWD}:/download" kmaehashi/nvget'

  nvget-docker "https://developer.nvidia.com/compute/machine-learning/nccl/secure/v2.1/prod/nccl_2.1.2-1+cuda8.0_x86_64"
