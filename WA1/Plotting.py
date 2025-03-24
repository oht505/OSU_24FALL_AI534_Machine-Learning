import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Define theta values (0 to 1)
theta = np.linspace(0, 1, 1000)
#print(theta)
# theta = [0.4 for i in range(1000)]

# Define the parameters for the prior and posteriors
alpha_prior, beta_prior = 2, 2
alpha_post_1, beta_post_1 = 4, 5   # After 5 coin tosses (2 heads)
alpha_post_2, beta_post_2 = 22, 32  # After 50 coin tosses (20 heads)
alpha_post_3, beta_post_3 = 402, 602 # After 1000 coin tosses (400 heads)

# Compute the PDF for the prior and posterior distributions
prior_pdf = beta.pdf(theta, alpha_prior, beta_prior)
posterior_1_pdf = beta.pdf(theta, alpha_post_1, beta_post_1)
posterior_2_pdf = beta.pdf(theta, alpha_post_2, beta_post_2)
posterior_3_pdf = beta.pdf(theta, alpha_post_3, beta_post_3)

# Plot the distributions
plt.plot(theta, prior_pdf, label='Prior (Beta(2, 2))', color='blue')
plt.plot(theta, posterior_1_pdf, label='Posterior after 5 tosses (Beta(4, 5))', color='green')
plt.plot(theta, posterior_2_pdf, label='Posterior after 50 tosses (Beta(22, 32))', color='red')
plt.plot(theta, posterior_3_pdf, label='Posterior after 1000 tosses (Beta(402, 602))', color='black')

# Add labels and legend
plt.xlabel(r'$\theta$')
plt.ylabel('Density')
plt.title('Prior and Posterior Distributions')
plt.legend()
plt.grid(True)
plt.show()
