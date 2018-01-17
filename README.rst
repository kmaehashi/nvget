nvget
=====

Requirements
------------

Python 2.7, 3.3, 3.4, 3.5 or 3.6

Run Using Docker
----------------

::

  docker pull kmaehashi/nvget
  export NVGET_USER="your.email@example.net"
  export NVGET_PASSWORD="p@ssw0rd"
  docker run --rm -e NVGET_USER -e NVGET_PASSWORD -u "${UID}" -v "${PWD}:/download" kmaehashi/nvget "https://developer.nvidia.com/compute/machine-learning/nccl/secure/v2.1/prod/nccl_2.1.2-1+cuda8.0_x86_64"
