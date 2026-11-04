+++
id = "example-zeta-projective-space-elliptic-curve"
kind = "example"
title = "Projective space and elliptic curves"
name_showing = false
order = 1391
+++
We have $\#\mathbf P^d(\mathbf F_{q^m})=1+q^m+\cdots+q^{dm}$, so
that $Z(\mathbf P^d_{\mathbf F_q},T)=\prod_{i=0}^d(1-q^iT)^{-1}$.
Grouping the reciprocal roots by absolute value as in (2), we find
$P_{2i}=1-q^iT$ for $0\le i\le d$ and $P_i=1$ for odd $i$. For an
elliptic curve $C_0$, we have $P_0=1-T$ and $P_2=1-qT$ by (3).
Since $b_1=2$ (Appendix [chap-Cohomology-of-torsion-sheaves-on-curves]), the polynomial $P_1$ has two
reciprocal roots $\alpha,\beta$. Poincaré duality matches them as
$\beta=q/\alpha$, so $P_1=1-aT+qT^2$ with $a=\alpha+\beta$. The
point-counting formula for $m=1$ gives $\#C_0(\mathbf F_q)=1-a+q$, that
is, $a=1+q-\#C_0(\mathbf F_q)\in\mathbf Z$. By (2) both $\alpha$ and
$\beta$ have absolute value $q^{1/2}$, and we get Hasse's theorem
$|a|\le2q^{1/2}$.
