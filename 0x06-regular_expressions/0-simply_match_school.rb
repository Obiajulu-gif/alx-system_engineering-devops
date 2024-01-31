#!/usr/bin/env ruby

arg = ARGV[0]
pattern = /School/

if arg && arg.match?(pattern)
    puts arg.gsub(pattern, "School") + "$"
else
    puts "$"
end