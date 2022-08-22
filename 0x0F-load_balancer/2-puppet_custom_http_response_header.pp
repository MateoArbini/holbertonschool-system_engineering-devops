#Automatization of tasks, but this time using puppet

#Execution
exec {'update':
    command  => 'sudo apt update',
    provider => shell,
}

#Nginx Install
package {'nginx':
    ensure => installed,
    name   => 'nginx',
}

#Trying to modify the header
file_line {'custom header':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    after  => 'server_name _;',
    line   => '    location /{
    add_header X-Served-By ${hostname}',
    },
}

exec {'restart':
    command  => 'sudo service restart nginx',
    provider => shell,
}
