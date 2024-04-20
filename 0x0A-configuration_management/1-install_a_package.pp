# installs flask on machine using pip3

package{'python3':
  ensure  => installed,
}

package{'python3-pip':
  ensure => installed,
}

exec{'install_flask':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => 'pip3 show flask',
}


#exec{'test':
#  command   => 'echo my_test_command',
#  path      => ['/usr/bin/', '/bin'],
#  onlyif    => 'ls . | grep "README.md" | wc -l',
#  logoutput => true,
#}
