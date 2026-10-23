+++
kind  = "proof"
of    = "sk-cor-hasse"
+++
In the point-counting formula of [sk-cor-tf-point-counting],
the terms in degrees $0$ and $2d$ are $1$ and $q^{dm}$ ([sk-thm-weil-final]
(3)). In degree $i$, the trace is a sum of $b_i$ eigenvalues of $F^m$, each
of complex modulus $q^{mi/2}$ ([sk-input-weights]), and the triangle
inequality proves the first bound. For a curve, $b_1=2g$ by the cohomology
calculation of [sk-thm-curveestimate]: $H^1(C,\mu_{\ell^r})=J[\ell^r](k)$,
and the Tate module of the Jacobian has rank $2g$ ([sk-prop-av-tate-rank]).

For the complement: over $\mathbf C$ write
$P_i(T)=\prod_{j=1}^{b_i}(1-\alpha_{i,j}T)$, so $|\alpha_{i,j}|=q^{i/2}$.
Comparing logarithmic derivatives of
$Z(X_0,T)\prod_{i\ \text{even}}P_i=\prod_{i\ \text{odd}}P_i$, using
$T\,Z'/Z=\sum_{m\ge1}\#X_0(\mathbf F_{q^m})T^m$ and
$T\,P_i'/P_i=-\sum_{m\ge1}\bigl(\sum_j\alpha_{i,j}^{m}\bigr)T^m$, gives
$\#X_0(\mathbf F_{q^m})=\sum_{i=0}^{2d}(-1)^{i}\sum_{j}\alpha_{i,j}^{m}$. The
terms $i=0$ and $i=2d$ are $1$ and $q^{dm}$, distinct since $d\ge1$, and the
triangle inequality bounds the rest. Both endpoint terms must be subtracted:
for $X_0=\mathbf P^1$ one has $b_1=0$ and $\#X_0(\mathbf F_q)=q+1$.
