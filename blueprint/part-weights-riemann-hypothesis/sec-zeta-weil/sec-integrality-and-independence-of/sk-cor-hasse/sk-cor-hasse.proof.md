+++
kind = "proof"
of = "sk-cor-hasse"
+++
In the point-counting formula of Corollary [sk-cor-tf-point-counting],
the terms in degrees $0$ and $2d$ are $1$ and $q^{dm}$ by
Theorem [sk-thm-weil-final](3). In degree $i$, the trace is a
sum of $b_i$ eigenvalues of $F^m$, each of complex modulus $q^{mi/2}$,
and the triangle inequality proves the first bound. For a curve, $b_1=2g$ by the cohomology calculation of
Appendix [sec-curve-estimates].

For the complement, write $P_i(T)=\prod_{j=1}^{b_i}(1-\alpha_{ij}T)$ over
$\mathbf C$; by hypothesis $|\alpha_{ij}|=q^{i/2}$. Take the logarithmic
derivative $T\frac{d}{dT}\log$ of
$Z(X_0,T)=\prod_iP_i(T)^{(-1)^{i+1}}$ in $\mathbf Q[[T]]$. By the
definition $Z(X_0,T)=\exp\bigl(\sum_{m\geq1}\#X_0(\mathbf F_{q^m})T^m/m\bigr)$
of Corollary [sk-cor-tf-point-counting], the left side is
$\sum_{m\geq1}\#X_0(\mathbf F_{q^m})T^m$, and
$T\frac{d}{dT}\log(1-\alpha T)=-\sum_{m\geq1}\alpha^mT^m$, so

$$
\#X_0(\mathbf F_{q^m})=\sum_{i=0}^{2d}(-1)^i\sum_{j=1}^{b_i}\alpha_{ij}^m
\qquad(m\geq1).
$$

Since $P_0=1-T$ and $P_{2d}=1-q^dT$, the terms $i=0$ and $i=2d$ are $1$
and $q^{dm}$, and the triangle inequality bounds the remaining terms by
$\sum_{i=1}^{2d-1}b_iq^{mi/2}$.
