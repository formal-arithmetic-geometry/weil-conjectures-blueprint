+++
id = "prose-13-04"
kind = "hidden"
title = "Frobenius fixed points and the local term on a curve"
order = 575
+++
The local terms of the trace formula live on the fixed point scheme
$\Fix(\Phi_X^m)=\Fix(c_m)$ of the graph $c_m$. A local term is defined on each open and
closed part of this scheme that is proper over $k$. The next lemma shows
that the fixed scheme is a finite reduced set of points, one for each
$\mathbf F_{q^m}$-rational point of $X_0$, so that every such point has
its own local term.

That the fixed scheme is reduced is the algebraic form of the
transversality computed after the question at the start of
Section [sec-trace-formula], where $u^{q^m}-u$ has a simple zero at
$u=0$. On
$\mathbf A^1$ the fixed scheme of $\Phi^m$ is
$\operatorname{Spec}k[t]/(t^{q^m}-t)$, and since $t^{q^m}-t$ has
derivative $-1$, its $q^m$ roots are simple. Reducedness alone does
not let us read off the local term from the stalk: the local term is
computed from $\cHom(c_2^*K,c_1^!K)$ near the fixed point, and for
$K=j_!A$ on $\mathbf A^1$ this complex is not determined by the stalk
at the origin (Remark [sk-rem-tf-locality-warning]). The main result of the
subsection, Proposition [sk-p-frob], says that for
Frobenius on a smooth curve the local term at a rational point is
nevertheless the trace on the stalk, for every $K$ and every $\psi$.
It is the only computation of local terms in the proof of
Theorem [sk-thm-tf-coefficient-morphism-formula], where it is applied on
$\mathbf P^1$, at the points of $\mathbf A^1$ and at the point at
infinity. Remark [sk-rem-tf-curve-local-proof] below describes the route.
