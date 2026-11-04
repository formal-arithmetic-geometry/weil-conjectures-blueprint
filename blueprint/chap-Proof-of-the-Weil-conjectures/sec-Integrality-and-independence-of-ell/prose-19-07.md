+++
id = "prose-19-07"
kind = "hidden"
title = "Integrality and independence of $\\ell$ (1)"
order = 1377
+++
Let $X_0$ be smooth and proper over $\mathbf F_q$, of pure dimension
$d$, and let $A/B$ be the reduced fraction of $Z(X_0,T)$
(Lemma [lemma-reduced-fractions-integer-coefficients]). We now
carry out the argument sketched at the start of the section. Purity
makes the characteristic polynomials of Frobenius in different degrees
pairwise coprime. No cancellation can then occur, and the polynomials
can be read off from $A$ and $B$.
For a prime $\ell\nmid q$ put

$$
H^i_\ell=H^i(X_{\mathrm{pro}\acute{e}t},\mathbf Q_\ell),\qquad
P_{i,\ell}(T)=\det(1-TF\mid H^i_\ell),\qquad
b_{i,\ell}=\dim_{\mathbf Q_\ell}H^i_\ell.
$$

Since $X_0$ is proper, $H^i_c=H^i$, and the determinant identity of
Corollary [corollary-point-counting-zeta-function] for $\Lambda=\mathbf Q_\ell$ reads

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}.
\tag{19.1}
$$

Since Frobenius is invertible, $\deg P_{i,\ell}=b_{i,\ell}$.
