#!/usr/bin/env ruby

log_entry = ARGV[0]

sender = log_entry.match(/\[from:(?<sender>[^\]]+)\]/)&.[:sender] || ""
receiver = log_entry.match(/\[to:(?<receiver>[^\]]+)\]/)&.[:receiver] || ""
flags = log_entry.match(/\[flags:(?<flags>[^\]]+)\]/)&.[:flags] || ""

puts "#{sender},#{receiver},#{flags}"
