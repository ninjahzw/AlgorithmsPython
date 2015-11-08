###
# How would you print just the 10th line of a file?
# 
# For example, assume that file.txt has the following content:
# 
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Your script should output the tenth line, which is:
# Line 10
###

# NOTE that if we use the following commend, if the file does not have 10 lines, 
# it will return the last line which is not correct.
head -10 file.txt | tail -1

# This commend can always give correct answer:
# (if does not have 10 lines, this will return nothing.)
cat file.txt | awk 'NR==10'

# We can also use sed:
sed -n '10p' file.txt

# or, if you have to use head and tail:
# because in the help of tail it says:
#   -n, --lines=K            output the last K lines, instead of the last 10;
#                            or use -n +K to output lines starting with the Kth
tail -n +10 file.txt | head -n 1
