def find_missing(input):

  # sortedList = sorted(input)
  # #print(sortedList )
  # first = sortedList[1]
  # last = sortedList[-1]
  # num_list = range(first, last + 1) 
  # #print(first , last , list(num_list) ,sum(input), sum(list(num_list)))
  # return (sum(list(num_list)) - sum(input) ) + 1
  sum_of_elements = sum(input)
  
  # There is exactly 1 number missing 
  n = len(input) + 1
  actual_sum = (n * ( n + 1 ) ) / 2
  print(actual_sum)
  return actual_sum - sum_of_elements

if True:
  result = find_missing([3,7,1,2,8,4,5])
  print(result)