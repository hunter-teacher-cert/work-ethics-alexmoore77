“You’ll love the way we fly” 
(and endanger you with heartless algorithms)
Alex Moore
10-5-21
Ethics
Computer Science Advanced Certificate Program - Hunter College

According to The Independent, the algorithms that assign economy seats randomly or close to randomly is unethical:  “This is especially important when adults and their children need to be seated near to each other if an emergency situation occurs, such an evacuation, decompression or air turbulence, when the assistance and supervision of an adult is likely to be of paramount importance.”  I would agree because passengers are paying for greater safety.  If they don’t pay more, they will be more likely to be seated in an unsafe way because they may be separated from family members.
In our Hunter College Computer Science Advanced Certificate Program Ethics course with Professor Zamansky, our class experimented with a Python program that contained algorithms that were likely similar to those utilized by the airlinesI believe that this problem can be addressed in a number of ways:

Algorithmic Solution #1:  Take advantage of Python dictionaries:
def get_number_economy_sold(economy_sold):
In C/C++, arrays are indexed by number.  In Python and PHP, they can be indexed by keys, and this is an untapped opportunity.  Are the surnames of all family members the same?  Of course not; however, family members are more likely to share a surname than strangers.  This is emphasized in the Independent article.  If the Python dictionary were sorted as it were being created by key, it would increase the likelihood that family members were seated together.

Algorithmic Solution #2:  This line of code is one of the major culprits:
random.shuffle(order)
One step that could be taken would be to avoid shuffling order and leading to a semi-random assignment.  Randomizing is an unnecessary step that is scrambling the passengers.  It would be preferable to seat the economy passengers in the order of purchase as a family purchasing a number of seats could be more likely to be grouped together.

Algorithmic Solution #3:  The function below could also be updated:
def seat_economy(plane,economy_sold,name):
  Throughout this program, you see collections and lists of lists.  It is possible to simply append economy seats to the plane where seats are available in a consecutive order.  This would make it more likely that family members would sit together.

Work Cited:
Coffey, Helen.  “Airlines Face Crackdown on Use of ‘Exploitative’ Algorithm that Splits up Families of Flights.”  The Independent.  19 Nov. 2018    https://www.independent.co.uk/travel/news-and-advice/airline-flights-pay-extra-sit-together-split-family-algorithm-minister-a8640771.html
