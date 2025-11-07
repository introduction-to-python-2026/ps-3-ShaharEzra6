def approximate_pi(n_terms):
  pi_value = 0
  for i in range (n_terms):
      pi_value += ((-1)**i) / (2*i+1)
  return pi_value * 4


n_terms = 10
list_of_numbers = []
sign = -1
for i in range(n_terms):
    sign *= -1
    list_of_numbers.append(sign)
print (list_of_numbers)



n_terms = 10
list_of_numbers = []
numerator = -1
denominator = -1
for i in range(n_terms):
    numerator *= -1
    denominator += 2
    leibniz = (numerator) / (denominator)
    list_of_numbers.append(leibniz)
print (list_of_numbers)



n_terms = 10
list_of_numbers = []
numerator = -1
denominator = -1
pi_sum = 0
for i in range(n_terms):
    numerator *= -1
    denominator += 2
    leibniz = numerator / denominator
    list_of_numbers.append(leibniz)
    pi_sum += leibniz
    
print (pi_sum *4)





def approximate_pi(n_terms):
    n_terms = 10
    list_of_numbers = []
    numerator = -1
    denominator = -1
    pi_sum = 0
    for i in range(n_terms):
      numerator *= -1
      denominator += 2
      leibniz = numerator / denominator
      list_of_numbers.append(leibniz)
      pi_sum += leibniz
    return (pi_sum *4)
