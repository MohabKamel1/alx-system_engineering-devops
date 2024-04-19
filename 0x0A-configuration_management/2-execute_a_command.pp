# Creating a manifest that kills a process 'killmenow' using puppet

exec { 'pkill killmenow':
command => '/usr/bin/pkill -f killmenow',
}
