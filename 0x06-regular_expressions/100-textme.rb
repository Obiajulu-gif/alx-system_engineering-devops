#!/usr/bin/env ruby
puts "#{ARGV[0].match(/\[from:(?<sender>[^\]]+)\]/)&.[:sender] || ""},#{ARGV[0].match(/\[to:(?<receiver>[^\]]+)\]/)&.[:receiver] || ""},#{ARGV[0].match(/\[flags:(?<flags>[^\]]+)\]/)&.[:flags] || ""}"