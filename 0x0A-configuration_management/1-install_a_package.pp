# installs flask on machine using pip3
# first uninstalls all dependencies if they exist already

package{'python3':
  ensure  => installed,
}

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