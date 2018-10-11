name = str(input("What is the batter's full name? "))
print (name)
plate_appearances = int(input("How many plate appearances did he/she have? "))
print (plate_appearances)
at_bats = int(input("How many at bats did he/she have? "))
print (at_bats)
walks = int(input("How many walks did he/she have? "))
print (walks)
singles = int(input("How many singles did he/she have? "))
print (singles)
doubles = int(input("How many doubles did he/she have? "))
print (doubles)
triples = int(input("How many triples did he/she have? "))
print (triples)
home_runs = int(input("How many home runs did he/she have? "))
print (home_runs)
#Above is just the user input and variable creation
hits = (home_runs + triples + doubles + singles)
batting_average = ("{0:.3f}".format(hits/at_bats))
total_bases = (singles + (doubles * 2) + (triples * 3) + (home_runs*4))
slugging_percentage = float(("{0:.3f}".format(total_bases/at_bats)))
on_base_percentage = float(("{0:.3f}".format((walks + singles + doubles + triples + home_runs)/plate_appearances)))
ops = ("{0:.3f}".format(on_base_percentage + slugging_percentage))

#Above are all the variables
print (name, "had", hits, "hits!")
print (name, "had his/her batting average to be", batting_average,)
print (name, "had his/her slugging average to be", slugging_percentage,)
print (name, "had his/her on-base plus slugging rate to be", ops,)
#Above just prints out the necessary variables to the user
print ("Did you know that Mike Trout is currently the highest OPS holder that is also an active player at 1.061? ")
#http://www.espn.com/mlb/stats/batting/_/sort/OPS/order/true
print ("Did you know that Babe Ruth is the record holder for the highest OPS of all time at 1.1636?")
#https://www.baseball-reference.com/leaders/onbase_plus_slugging_career.shtml
