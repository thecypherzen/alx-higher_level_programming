#!/usr/bin/env ruby
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

puts ARGV[0].scan(/([A-Z]++)/).join
<<<<<<< HEAD
=======
puts ARGV[0].scan(/[A-Z]+/).join
>>>>>>> 93ed88b... build(a_devops:0x06): add task7 solution file
=======

<<<<<<< HEAD
=======

>>>>>>> 3d3c7fd... build(a_devops:0x06): add task7 solution file
str = ARGV[0]
regex = /(?>from:(?<sndr>\+?\w+))|(?>to:(?<rcvr>\+?\w+))|(flags:(?<flgs>(:?\-?[0-9])+))/
matches = str.scan(regex)
res = ""

# if matches are found, then iterate over them to construct result
if matches
  matches.each do |match|
    len = match.length - 1
    for i in 0..len
      if match[i]
        res += match[i] if match[i]
        res += ',' if i < (match.length - 1)
      end
    end
  end
end
puts res
<<<<<<< HEAD
>>>>>>> 3d3c7fd... build(a_devops:0x06): add task7 solution file
=======
puts ARGV[0].scan(/([A-Z]++)/).join
>>>>>>> fb0560f... fix(a_devops:0x06): revert task7 file to original
=======
puts ARGV[0].scan(/[A-Z]+/).join
>>>>>>> 93ed88b... build(a_devops:0x06): add task7 solution file
=======
>>>>>>> 3d3c7fd... build(a_devops:0x06): add task7 solution file
=======
>>>>>>> fb0560f... fix(a_devops:0x06): revert task7 file to original
=======

puts ARGV[0].scan(/([A-Z]++)/).join
>>>>>>> ae08487284ffd0509af205190b88888858c22b12
