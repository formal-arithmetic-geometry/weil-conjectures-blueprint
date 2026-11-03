+++
id = "def-sc-divisor"
kind = "definition"
title = "Divisors, principal divisors, class group"
lean = ["AlgebraicGeometry.Scheme.Divisor.toPic", "AlgebraicGeometry.Scheme.Divisor", "AlgebraicGeometry.Scheme.Divisor.degree", "AlgebraicGeometry.Scheme.div", "AlgebraicGeometry.Scheme.principalDivisors", "AlgebraicGeometry.Scheme.DivisorClassGroup", "AlgebraicGeometry.Scheme.ord", "AlgebraicGeometry.Scheme.finite_setOf_ord_ne_zero", "AlgebraicGeometry.Scheme.Divisor.associatedModule", "AlgebraicGeometry.Scheme.Pic.ofClosedPoint", "AlgebraicGeometry.Scheme.exists_divisorClassGroup_addEquiv_pic"]
order = 581
uses = ["def-sc-curves", "def-sc-function-field", "def-sc-invertible-module", "def-sc-picard-group"]
+++
Let $C$ be a scheme, for instance a curve over $k$. A
*divisor* on $C$ is a finite formal sum
$D=\sum_Pn_P[P]$ of closed points $P$ of $C$ with integer
coefficients; $\operatorname{Div}(C)$ is the free abelian group on
the closed points of $C$. The *degree* of $D$ is

$$
\deg D:=\sum_Pn_P.
$$

Now let $C$ be a Noetherian integral scheme (for instance a connected
smooth curve over $k$), with function field $k(C)$
([def-sc-function-field]). For $f\in k(C)^*$ its *divisor* is

$$
\operatorname{div}(f)=\sum_P v_P(f)\,[P],
$$

where $v_P$ is the order of vanishing at $P$ (the normalized valuation of
the local ring $\mathcal O_{C,P}$ when this is a discrete valuation ring,
for instance when $C$ is a smooth curve); only finitely many $v_P(f)$ are
nonzero. Such divisors are *principal*, and $f\mapsto\operatorname{div}(f)$
is a homomorphism $k(C)^*\to\operatorname{Div}(C)$.
The *divisor class group* is

$$
\operatorname{Cl}(C):=\operatorname{Div}(C)/\{\operatorname{div}(f):f\in k(C)^*\}.
$$

If moreover $C$ is regular (for instance a connected smooth curve), the
associated sub-$\mathcal O_C$-module of the constant sheaf $k(C)$ of
$D=\sum n_P[P]$ is

$$
\mathcal O_C(D)(U):=\{0\}\cup\{f\in k(C)^*:v_P(f)+n_P\geq0\text{ for every closed point }P\in U\}.
$$

Let $C$ be a smooth curve over $k$. The ideal sheaf $\mathcal I_P$ of a
closed point $P$ is an invertible $\mathcal O_C$-module
([def-sc-invertible-module]); put $\mathcal O_C(P):=\mathcal I_P^{\vee}$
and

$$
[\mathcal O_C(D)]:=\prod_P[\mathcal O_C(P)]^{n_P}\in\operatorname{Pic}(C)
$$

([def-sc-picard-group]). This is a homomorphism
$\operatorname{Div}(C)\to\operatorname{Pic}(C)$, and when $C$ is moreover
integral it induces an isomorphism
$\operatorname{Cl}(C)\xrightarrow{\sim}\operatorname{Pic}(C)$,
$D\mapsto[\mathcal O_C(D)]$.
