#making a puppet file to change our config. The files should be created in
#the same way as we created in the previous project

file_line { 'Identity file':
  ensure => 'present'
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
file_line { 'disable password login':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
