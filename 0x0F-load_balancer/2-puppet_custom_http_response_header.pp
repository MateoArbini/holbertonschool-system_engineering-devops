#Automatization of tasks, but this time using puppet

#Execution
exec {'update':
    command  => 'sudo apt-get -y update',
    provider => shell,
    before   => Exec['nginx'],
}

#Nginx Install
exec {'nginx':
    command  => 'sudo apt-get -y install nginx',
    provider => shell,
    before  => Exec['custom header'],
}

#Trying to modify the header
exec {'custom header':
    provider => shell,
    command  => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
    before   => Exec['restart'],
}

#Restarting nginx
exec {'restart':
    command  => 'sudo service nginx restart',
    provider => shell
}
