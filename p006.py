def compute():
  n = 100
  # Prove this using the differences technique
  # very interesting => https://trans4mind.com/personal_development/mathematics/series/polynomialEquationDifferences.htm
  square_of_sums = (n * (n + 1) / 2) ** 2
  sum_of_squares = n/6 * (2*n + 1) * (n + 1)
  
  return square_of_sums - sum_of_squares

if __name__ == '__main__':
  print(compute())
