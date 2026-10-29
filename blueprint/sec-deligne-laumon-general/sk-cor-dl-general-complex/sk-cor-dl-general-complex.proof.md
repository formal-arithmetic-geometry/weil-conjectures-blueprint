+++
kind  = "proof"
of    = "sk-cor-dl-general-complex"
+++
Apply $Rf_!$ to the ordinary truncation tower of the underlying
geometric complex $K$. Since this tower is bounded and functorial, we
obtain the spectral sequence

$$
 E_2^{a,b}=R^af_!\mathcal H^b(K)
   \ \Longrightarrow\ \mathcal H^{a+b}(Rf_!K).
$$

By naturality in $K$ and the Frobenius compatibility of $Rf_!$, its exact couple, its differentials and
its finite abutment filtration carry compatible Frobenius actions. By
[sk-thm-dl-general-sheaf], $E_2^{a,b}$ is mixed of weights at most
$w+a+b$, and every $E_\infty^{a,b}$ is a subquotient of this term.
Therefore the finite filtration of $\mathcal H^n(Rf_!K)$ has mixed
quotients of weights at most $w+n$, and so
$\mathcal H^n(Rf_!K)$ is mixed of weights at most $w+n$.
For the structure map, the geometric fibre of the direct image is
the compactly supported cohomology with its Frobenius operator
([det-prop-sf-cbc]), which gives the last assertion.
