+++
kind = "proof"
of = "lemma-frobenius-fixed-scheme"
order = 960
uses = ["lemma-frobenius-fixed-scheme--1", "lemma-frobenius-fixed-scheme--2", "lemma-frobenius-fixed-scheme--3", "lemma-frobenius-fixed-scheme--4"]
+++
We reduce to a closed subscheme of affine space, where the equations
$t^{q^m}=t$ have simple roots.

For every open $U_0\subset X_0$ the restriction to
$U=U_0\times_{k_0}k$ of the fixed scheme of $\Phi_X^m$ is the fixed scheme of
$\Phi_U^m$, because $\Phi_X$ is the base change of a morphism of $X_0$ and so
maps $U$ into itself. As $X_0$ is quasi-compact, we may therefore assume that $X_0$
is a closed subscheme of $\mathbf A^r_{\mathbf F_q}$, with coordinates
$t_1,\ldots,t_r$.

In this case the fixed scheme is the pullback of the diagonal along the graph.
Since the equations of $X_0$ have coefficients in $\mathbf F_q$, we have
$(\Phi_X^m)^\#t_i=t_i^{q^m}$, and the fixed scheme is cut out by the defining
equations of $X_0$ together with $t_i^{q^m}-t_i=0$. Each polynomial
$t^{q^m}-t$ is separable, so the algebra $k[t_1,\ldots,t_r]/(t_i^{q^m}-t_i)_i$
is a product of copies of $k$ indexed by $\mathbf F_{q^m}^r$. Its quotient by
the defining equations of $X_0$ retains exactly the factors at the rational
solutions of those equations, as asserted. In particular the fixed scheme is
a closed subscheme of a finite étale $k$-scheme, hence étale. The argument
uses only the equations of $X_0$, so $X_0$ need not be reduced.
