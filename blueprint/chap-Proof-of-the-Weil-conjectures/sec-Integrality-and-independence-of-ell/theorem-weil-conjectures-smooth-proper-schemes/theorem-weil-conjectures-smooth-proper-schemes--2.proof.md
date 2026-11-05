+++
kind = "proof"
of = "theorem-weil-conjectures-smooth-proper-schemes--2"
order = 1388003
uses = []
+++
Cross-multiply the two factorizations in $\mathbf Q[[T]]$ and use the injectivity of polynomials into power series to obtain an equality of polynomial products. Extend coefficients to $\mathbf C$. In each product, filter the multiset of roots by the absolute value $q^{-i/2}$. Since $q>1$, the weights are distinct, so the filtered equality identifies the root multisets of $P_i$ and $P'_i$. Their constant coefficients are one, hence the polynomials agree. Injectivity of $\mathbf Z\hookrightarrow\mathbf C$ gives the original equality. The separation step is `Polynomial.eq_of_isPureOfWeight_of_prod_mul_eq`.
