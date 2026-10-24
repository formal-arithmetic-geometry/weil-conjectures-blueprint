+++
kind  = "proof"
of    = "thm-weil-final-betti"
+++
The definition of the common Betti numbers is
[def-weil-betti-numbers]. The comparison in
[prop-weil-betti-comparison] gives
$b_i=\dim_{\Ql}H^i(X,\Ql)$, independently of $\ell$. The perfect pairing
has its canonical exceptional-inverse-image orientation supplied by
[thm-weil-six-operations] for the smooth proper structure morphism;
the duality interface [thm-weil-poincare-duality] and the pairing assembled in
[prop-poincare-pairing] together give $b_i=b_{2d-i}$. The endpoint
calculation [prop-endpoints] gives $b_0=b_{2d}=1$ and the two endpoint
factors, identified with $P_0,P_{2d}$ by [prop-integral-recovery].

For the poles, use the factorization
$Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}$ of
[thm-weil-final-integrality]. Over $\overline{\mathbf Q}$ write
$P_i(T)=\prod_{r=1}^{b_i}(1-\alpha_{i,r}T)$, the $\alpha_{i,r}$ being the
reciprocal roots. For $c\in\overline{\mathbf Q}^\times$, the order of
vanishing of $P_i$ at $T=c^{-1}$ is the number of $r$ with
$\alpha_{i,r}=c$. By [thm-weil-final-rh], every $\alpha_{i,r}$ satisfies
$|\tau(\alpha_{i,r})|=q^{i/2}$ for every complex embedding $\tau$.

Take $c=1$. Since $q>1$, $q^{i/2}=1$ only for $i=0$, so
$P_i(1)\neq0$ for $1\leq i\leq2d$, while $P_0(T)=1-T$ vanishes to
order exactly $1$ at $T=1$. As $P_0$ occurs with exponent $(-1)^{0+1}=-1$,
$Z(X_0,T)$ has a pole of order exactly $1$ at $T=1$.

Take $c=q^d$ with $d\geq1$. Since $|\tau(q^d)|=q^d=q^{i/2}$ only for
$i=2d$, one has $P_i(q^{-d})\neq0$ for $0\leq i<2d$ (for $i=0$ this is
also visible from $P_0(q^{-d})=1-q^{-d}\neq0$), while
$P_{2d}(T)=1-q^dT$ vanishes to order exactly $1$ at $T=q^{-d}$. As
$2d$ is even, $P_{2d}$ occurs with exponent $-1$, so $Z(X_0,T)$ has a
pole of order exactly $1$ at $T=q^{-d}$. (For $d=0$ the two points
coincide and $Z(X_0,T)=(1-T)^{-1}$.)
