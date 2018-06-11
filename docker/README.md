According to https://docs.docker.com/docker-for-mac/faqs docker for mac doesn't
support pass through for USB devices, so we have to use [Docker
Toolbox](https://docs.docker.com/toolbox/overview/#ready-to-get-started)

You'll also need the [Oracle VM VirtualBox Extension
Pack](https://www.virtualbox.org/wiki/Downloads). Note that you'll need to be
sure to have a compatible version of VirtualBox and the extension pack. If you
have an existing installation of virtualbox, you may need to update it.

First we create a virtual box VM to use
```
docker-machine create virtualbox
```

Then we stop it so we can configure it to enable USB ports
```
docker-machine stop virtualbox
```

Open up virtualbox, go to the VM named `virtualbox`, right click to open
settings. Go to Ports -> USB and enable the controller. Use the button
with the green plus to add the Lattice FTUSB Interface Cable.

Start the virtual machine again
```
docker-machine start virtualbox
```

It prompts us to use this command to see how to configure our shell
```
$ docker-machine env virtualbox
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/lenny/.docker/machine/machines/virtualbox"
export DOCKER_MACHINE_NAME="virtualbox"
# Run this command to configure your shell:
# eval $(docker-machine env virtualbox)
```

So we follow the instructions
```
eval $(docker-machine env virtualbox)
```

Now we load up our image
```
docker run -it --rm --device=/dev/ttyUSB0 --privileged lennyt/magma:latest /bin/bash
```