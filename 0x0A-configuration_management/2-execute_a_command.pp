# script to kill a process by name
exec { 'pkill killmenow':
  path  => '/usr/bin'
}
