exec { 'apt-get update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['InstallNginx'],

sed -i s/127.0.0.1/127.0.0.2/ ~/hosts.new