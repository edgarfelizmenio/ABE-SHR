VAGRANTFILE_API_VERSION = "2"
DEFAULT_BOX = "ubuntu/trusty64"

ENV["LC_ALL"] = "en_US.UTF-8"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.define("ABE-SHR") do |abe_shr|
        abe_shr.vm.box = DEFAULT_BOX
        abe_shr.vm.provider "virtualbox" do |v|
            v.name = "ABE-SHR"
            v.customize ["modifyvm", :id, "--memory", 1024]
        end

        abe_shr.vm.network "public_network", ip: "192.168.1.101"

        abe_shr.vm.synced_folder ".", "/home/ABE-SHR"

        abe_shr.vm.provision "update", type: :shell do |shell|
            shell.inline = "apt-get -y -q update"
        end

        abe_shr.vm.provision "install_htop", type: :shell do |shell|
            shell.inline = "apt-get -y -q install htop"
        end

        abe_shr.vm.provision "install", type: :shell do |shell|
            shell.path = "install.sh"
        end

    end
    
end