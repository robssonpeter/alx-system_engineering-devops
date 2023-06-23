# install flask package
exec { 'pip3 install flask==2.1.0':
  path  => '/usr/bin'
}
