# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # A Fedora 36 box that works with multiple hypervisors
  # https://app.vagrantup.com/generic/boxes/fedora36
  config.vm.box = "generic/fedora36"

  config.vm.hostname = 'theturingway'

  # Sync the project directory between the host and vagrant environment
  config.vm.synced_folder "./", "/vagrant"

  # Options for the VirtualBox provider
  config.vm.provider "virtualbox" do |vb|
    # Set a reasonable amount of virtual CPUs and memory
    vb.cpus = 2
    vb.memory = 2048
  end

  # Options for the libvirt provider
  config.vm.provider "libvirt" do |lv, override|
    # Set a reasonable amount of virtual CPUs and memory
    lv.cpus = 2
    lv.memory = 2048

    # For Linux users with libvirt, NFS is used to sync directories
    # We set this to use TCP and not UDP as this is safer
    # TCP is the default for more modern NFS versions
    override.vm.synced_folder "./", "/vagrant", nfs_udp: false
  end

  # Options for the Hyper-V provider
  config.vm.provider "hyperv" do |hv|
    # Set a reasonable amount of virtual CPUs and memory
    hv.cpus = 2
    hv.memory = 2048
  end

  # Script to install the build dependencies
  $script = <<-'SCRIPT'
  # Install pip
  dnf install -y python3-pip
  # Install build dependencies
  sudo -u vagrant pip install --no-warn-script-location -r /vagrant/book/website/requirements.txt
  SCRIPT

  # Run the script using the shell provisioner
  config.vm.provision "shell", inline: $script
end
