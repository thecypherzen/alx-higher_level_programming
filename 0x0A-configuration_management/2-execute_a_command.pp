# a manifest that kills the process named killmenow.

exec{'kill_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => 'pgrep killmenow',
}