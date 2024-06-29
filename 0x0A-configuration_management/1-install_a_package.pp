#!/usr/bin/puppet

# Install required packages
package { ['ruby', 'ruby-augeas', 'ruby-shadow']:
  ensure => 'installed',
}
