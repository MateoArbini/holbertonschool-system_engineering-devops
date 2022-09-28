# Command to fix error
exec {'fix':
    command => '/usr/bin/env/sudo sed -i 's/15/2000/g' /etc/default/nginx' }
exec {'restart':
    command => 'sudo service nginx restart' }