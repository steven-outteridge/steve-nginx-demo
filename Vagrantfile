Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.network "private_network", ip: "192.168.0.233"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbooks/prov-docker.yml"
  end

end
