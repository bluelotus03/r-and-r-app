# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.box = "gusztavvargadr/windows-10"
  #config.vm.communicator = "ssh"
  #config.winssh.shell = "powershell"
  #config.vm.network "forwarded_port", host: 33389, guest: 3389, id: "rdp", auto_correct: true

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.34.10"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  # vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
    vb.cpus = "4"
    vb.memory = "8192"
    vb.customize ["modifyvm", :id, "--vram", "256"]
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  config.vm.provision "shell", privileged: true, inline: <<-'SHELL'
    choco install -y jdk8 python mysql apache-httpd
    # mysql: C:\tools\mysql\current
    # mysql setup: mysql.exe -h 127.0.0.1 -uroot
    # apache: C:\Users\vagrant\AppData\Roaming\Apache24\conf
    Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled false
    # setting 
    iex (new-object system.net.webclient).DownloadString("https://git.io/JfvET")
    w32tm /resync
    Set-TimeZone -Name "Eastern Standard Time"

    mysql.exe -h 127.0.0.1 -uroot -e 'CREATE DATABASE basic_web'
    mysql.exe -h 127.0.0.1 -uroot -e "CREATE USER 'root'@'%' IDENTIFIED BY 'password'; GRANT ALL PRIVILEGES ON basic_web.* TO 'root'@'%'; FLUSH PRIVILEGES;"
  SHELL
  config.vm.provision :reload
  config.vm.provision "shell", privileged: true, inline: <<-SHELL
    choco install -y tomcat
    Set-Service -Name tomcat9 -StartupType Automatic
    net start tomcat9
  SHELL
end
