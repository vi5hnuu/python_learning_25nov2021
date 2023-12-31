# The find() method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
# Syntax :
#
# str.find(sub,start,end)
#
# Parameters :
#
# sub : It’s the substring which needs to be searched in the given string.
# start : Starting position where sub is needs to be checked within the string.
# end : Ending position where suffix is needs to be checked within the string.
#
# NOTE : If start and end indexes are not provided then by default it takes 0 and length-1 as starting and ending indexes where ending indxes is not included in our search.
#
#
#
#
# Returns:
#
# returns the lowest index of the substring if it is found in given string. If it’s not found then it returns -1.
#
# The find() method is similar to index(). The only difference is find() returns -1 if searched string is not found and index() throws an exception in this case.

s="vivishvishnu kuvikumarr"
z=s.find('v',0)
print(s[z],"at ",z)
z=s.find('v',z+1)
print(s[z],"at ",z)
z=s.find('v',z+1)
print(s[z],"at ",z)