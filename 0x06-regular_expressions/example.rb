#!/usr/bin/env ruby
#puts ARGV[0].scan(/(\w+).*\1/).join
#mystr = "I code with java mostly, and javascript always. I know Typescript" +\
#        "Other times, I use C++, C or Python"
#reg_scan = mystr.scan(/(?>java(?:script)?|Python|c\b(?:\+\+)?)/i)
mystr = "abcc"
reg_scan = mystr.match(/a(bc|b)c/)


puts "====== reg_scan ======"
if reg_scan
  puts reg_scan.to_a
else
  puts "no match"
end
