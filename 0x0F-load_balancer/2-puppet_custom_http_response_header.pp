#Automatization of tasks, but this time using puppet

#Execution
exec {'update':
    command  => 'sudo apt update',
    provider => shell,
    before   => Exec['nginx'],
}

#Nginx Install
exec {'nginx':
    command => sudo apt-get install -y nginx,
    provider => shell,
    before => Exec['custom header'],
}

#Trying to modify the header
exec {'custom header':
    command => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
    provide => shell,
    before  => Exec['restart'],
}

#Restarting nginx
exec {'restart':
    command  => 'sudo service nginx restart',
    provider => shell,
}
