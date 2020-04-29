import numpy as np
from scipy.stats import norm
from scipy.stats import poisson
from scipy.special import gammaln


# Log-likelihood functions and samplers =======================================

def normal_logpdf(x, mu, sigma=1):
    return norm.logpdf(x, loc=mu, scale=sigma).sum()

def normal_rvs(mu, sigma=1, random_state=None):
    return norm.rvs(loc=mu, scale=sigma, random_state=random_state)

def sqrt_normal_logpdf(x, mu, sigma=1):
    return norm.logpdf(x ** 0.5, loc=mu ** 0.5, scale=sigma).sum()

def sqrt_normal_rvs(mu, sigma=1, random_state=None):
    return norm.rvs(loc=mu ** 0.5, scale=sigma, random_state=random_state) ** 2

def poisson_logpdf(x, mu, sigma=None):
    #return poisson.logpmf(x, mu).sum()
    return (x * np.log(mu.astype(float) + 1e-10) - mu - gammaln(x.astype(float) + 1e-10)).sum()

def poisson_rvs(mu, sigma=None, random_state=None):
    return poisson.rvs(mu, random_state=random_state)