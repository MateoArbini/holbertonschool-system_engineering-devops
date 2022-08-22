#Automatization of tasks, but this time using puppet
#
#Execution
#exec {'update':
#    command  => 'sudo apt update',
#    provider => shell,
#}
#
#Nginx Install
#exec {'nginx':
#    command => sudo apt-get install -y nginx,
#    provider => shell,
#}
#
#Trying to modify the header
#file_line {'custom header':
#    ensure => present,
#    path   => '/etc/nginx/sites-available/default',
#    after  => 'server_name _;',
#    line   => '    location /{
#    add_header X-Served-By \$HOSTNAME;',
#    },
#}
#
#exec {'restart':
#    command  => 'sudo service nginx restart',
#    provider => shell,
#}
exec {'master command':
    command => sudo apt update; sudo apt-get install -y nginx;
               sudo sed -i "/listen 80 default_server/a add_header X-Served-By '$HOSTNAME';" /etc/nginx/sites-enabled/default;
               sudo service nginx restart,
    provider => shell,
}
