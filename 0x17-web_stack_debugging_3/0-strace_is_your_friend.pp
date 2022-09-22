# Error fix: Modified file name extension from .phpp to .php, modified status from 500 to OK

exec { 'fix':
  command  => "/usr/bin/env sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}
