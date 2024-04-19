# A creates the file /tmp/school

$content = 'I love Puppet'

file {'/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  content => $content,
}