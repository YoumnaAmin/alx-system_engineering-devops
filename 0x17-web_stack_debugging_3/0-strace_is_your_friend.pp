# Puppet manifest to fix Apache 500 Internal Server Error by correcting file permissions and ensuring Apache configuration

exec { 'fix-apache-permissions':
  command => '/bin/chown -R www-data:www-data /var/www/html && /bin/chmod -R 755 /var/www/html',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
  onlyif  => '/usr/bin/test $(stat -c %U /var/www/html) != www-data || /usr/bin/test $(stat -c %a /var/www/html) -ne 755',
}

file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => "
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html

	ErrorLog \${APACHE_LOG_DIR}/error.log
	CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>",
  notify  => Exec['fix-apache-permissions'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/sites-available/000-default.conf'],
  require   => Exec['fix-apache-permissions'],
}
