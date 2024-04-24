# sets up a configuration file for remote server
# uses the private key ~/.ssh/school
# disables password login

# set path to ssh_config file
$ssh_config='/etc/ssh/ssh_config'

# ensure that it's present
file{'ssh_config':
  path => $ssh_config,
  ensure => present,
}

# back_up config file
exec{"backup config":
  command => "cp ${ssh_config} ${ssh_config}.bak",
  path    => ['/usr/bin/', '/bin'],
}

# create settings
$cmds = ['IdentityFile ~/.ssh/school', 'PasswordAuthentication no',
'KbdInteractiveAuthentication no',]

# execute settings
each($cmds) | $cmd | {
  exec{"${cmd}":
    command => "echo '    '${cmd} >> ${ssh_config}",
    path    => ['/usr/bin/', '/bin'],
  }
}
