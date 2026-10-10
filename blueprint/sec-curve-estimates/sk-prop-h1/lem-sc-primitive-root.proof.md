+++
kind  = "proof"
of    = "lem-sc-primitive-root"
+++
Since $n$ is prime to $\operatorname{char}k$, the polynomial
$x^n-1$ is separable (its derivative $nx^{n-1}$ is nonzero, and
$x^n-1$ and $nx^{n-1}$ are coprime); as $k$ is algebraically
closed it splits into $n$ distinct linear factors, giving a
primitive root $\zeta$ and $\mu_n(k)\cong\mathbf Z/n\mathbf Z$
via $\theta_\zeta$ ([def-sc-mu-trivialization]). The image of
a primitive root in a field extension is primitive (it has order
exactly $n$), which gives the compatibility with pullback.
