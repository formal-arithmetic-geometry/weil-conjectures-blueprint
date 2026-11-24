+++
id = "example-zeta-projective-space-elliptic-curve"
kind = "example"
title = "Projective space and elliptic curves"
name_showing = false
order = 1394
+++
We have $\#\mathbf P^d(\mathbf F_{q^m})=1+q^m+\cdots+q^{dm}$, so
that $\href{@corollary-point-counting-zeta-function}{Z(\mathbf P^d_{\mathbf F_q},T)}=\prod_{i=0}^d(1-q^iT)^{-1}$.
Grouping the [reciprocal roots](@definition-reciprocal-root) by absolute value as in (2), we find
$\href{@theorem-weil-conjectures-smooth-proper-schemes}{P_{2i}}=1-q^iT$ for $0\le i\le d$ and $\href{@theorem-weil-conjectures-smooth-proper-schemes}{P_i}=1$ for odd $i$. For an
elliptic curve $C_0$, we have $\href{@theorem-weil-conjectures-smooth-proper-schemes}{P_0}=1-T$ and $\href{@theorem-weil-conjectures-smooth-proper-schemes}{P_2}=1-qT$ by (3).
Since $\href{@theorem-weil-conjectures-smooth-proper-schemes}{b_1}=2$ (Appendix [chap-Cohomology-of-torsion-sheaves-on-curves]), the polynomial [$P_1$](@theorem-weil-conjectures-smooth-proper-schemes) has two
[reciprocal roots](@definition-reciprocal-root) $\alpha,\beta$. [Poincaré duality](@theorem-poincare-duality-frobenius) matches them as
$\beta=q/\alpha$, so $\href{@theorem-weil-conjectures-smooth-proper-schemes}{P_1}=1-aT+qT^2$ with $a=\alpha+\beta$. The
[point-counting formula](@corollary-point-counting-zeta-function) for $m=1$ gives $\#C_0(\mathbf F_q)=1-a+q$, that
is, $a=1+q-\#C_0(\mathbf F_q)\in\mathbf Z$. By (2) both $\alpha$ and
$\beta$ have absolute value $q^{1/2}$, and we get Hasse's theorem
$|a|\le2q^{1/2}$.
