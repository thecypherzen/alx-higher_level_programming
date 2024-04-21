# installs flask on machine using pip3
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# first uninstalls all dependencies if they exist already
=======
>>>>>>> a32828b... build(asd:0x0A): add task 1 solution
=======
# first uninstalls all dependencies if they exist already
>>>>>>> 014f41f... fix(asd:0x0A): resolve task 1 import err
=======
>>>>>>> a32828b... build(asd:0x0A): add task 1 solution
=======
# first uninstalls all dependencies if they exist already
>>>>>>> 014f41f... fix(asd:0x0A): resolve task 1 import err

package{'python3':
  ensure  => installed,
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
$packages = ['jinja2','werkzeug','itsdangerous','importlib-metadata','click', 'flask']
each($packages) | $pkg | {
  exec{"pip3_remove ${pkg}":
    command => "pip3 uninstall --yes ${pkg}",
    path    => ['/bin/usr', '/bin'],
    onlyif  => "pip3 show ${pkg}",
  }
  exec{"apt_remove ${pkg}":
    command => "apt-get remove python3-${pkg}",
    path    => ['/bin/usr', '/bin'],
    onlyif  => "pip3 show ${pkg}",
  }
}

exec{'install_flask':
  command => 'pip3 install flask==2.1.0 werkzeug==2.1.1',
  path    => ['/usr/bin', '/bin'],
}
=======
package{'pip3':
=======
package{'python3-pip':
>>>>>>> bef1aad... fix(asd:0x0A): fix package name error in task 1
=======
package{'pip3':
>>>>>>> a32828b... build(asd:0x0A): add task 1 solution
=======
package{'python3-pip':
>>>>>>> bef1aad... fix(asd:0x0A): fix package name error in task 1
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
<<<<<<< HEAD
>>>>>>> a32828b... build(asd:0x0A): add task 1 solution
=======
$packages = ['jinja2','werkzeug','itsdangerous','importlib-metadata','click', 'flask']
each($packages) | $pkg | {
  exec{"pip3_remove ${pkg}":
    command => "pip3 uninstall --yes ${pkg}",
    path    => ['/bin/usr', '/bin'],
    onlyif  => "pip3 show ${pkg}",
  }
  exec{"apt_remove ${pkg}":
    command => "apt-get remove python3-${pkg}",
    path    => ['/bin/usr', '/bin'],
    onlyif  => "pip3 show ${pkg}",
  }
}

exec{'install_flask':
<<<<<<< HEAD
   command => 'pip3 install flask==2.1.0 werkzeug==2.1.1',
   path    => ['/usr/bin', '/bin'],
}
>>>>>>> 014f41f... fix(asd:0x0A): resolve task 1 import err
=======
  command => 'pip3 install flask==2.1.0 werkzeug==2.1.1',
  path    => ['/usr/bin', '/bin'],
}
>>>>>>> 8c05ea9... style(asd:0x0A): pylintyfy task 1 file
=======
>>>>>>> a32828b... build(asd:0x0A): add task 1 solution
=======
$packages = ['jinja2','werkzeug','itsdangerous','importlib-metadata','click', 'flask']
each($packages) | $pkg | {
   exec{"pip3_remove $pkg":
	  command => "pip3 uninstall --yes $pkg",
	  path    => ['/bin/usr', '/bin'],
	  onlyif  => "pip3 show $pkg",
   }
   exec{"apt_remove $pkg":
      command => "apt-get remove python3-$pkg",
	  path    => ['/bin/usr', '/bin'],
	  onlyif  => "pip3 show $pkg",
   }
}

exec{'install_flask':
   command => 'pip3 install flask==2.1.0 werkzeug==2.1.1',
   path    => ['/usr/bin', '/bin'],
}
>>>>>>> 014f41f... fix(asd:0x0A): resolve task 1 import err
