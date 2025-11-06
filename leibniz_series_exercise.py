def approximate_pi(n_terms):
  pi_value = 0
  for i in range (n_terms):
      pi_value += ((-1)**i) / (2*i+1)
  return pi_value * 4
