+++
id = "def-sc-divisor"
kind = "definition"
title = "Divisors, principal divisors, class group"
lean = ["AlgebraicGeometry.Scheme.Divisor.toPic", "AlgebraicGeometry.Scheme.Divisor", "AlgebraicGeometry.Scheme.Divisor.degree", "AlgebraicGeometry.Scheme.div", "AlgebraicGeometry.Scheme.principalDivisors", "AlgebraicGeometry.Scheme.DivisorClassGroup"]
order = 454
uses = ["def-sc-curves", "def-sc-function-field"]
+++
Let $C$ be a connected curve over $k$. A
*divisor* on $C$ is a finite formal sum
$D=\sum_Pn_P[P]$ of closed points $P$ of $C$ with integer
coefficients; $\operatorname{Div}(C)$ is the free abelian group on
the closed points of $C$. For $f\in k(C)^*$
([def-sc-function-field]), its *divisor* is

$$
\operatorname{div}(f)=\sum_P v_P(f)\,[P],
$$

where $v_P$ is the normalized valuation of the local ring
$\mathcal O_{C,P}$ (a discrete valuation ring when $C$ is
smooth); such divisors are *principal*.
The *divisor class group* is

$$
\operatorname{Cl}(C):=\operatorname{Div}(C)/\{\operatorname{div}(f):f\in k(C)^*\}.
$$

For $D=\sum n_P[P]$ the associated sub-$\mathcal O_C$-module of
the constant sheaf $k(C)$ is

$$
\mathcal O_C(D)(U):=\{f\in k(C):\operatorname{div}(f)|_U+D|_U\geq0\}.
$$

The *degree* of $D$ is

$$
\deg D:=\sum_Pn_P.
$$

(For reducible $C$ all objects above are defined componentwise.)

For $C$ smooth, $\mathcal O_C(D)$ is an invertible $\mathcal O_C$-module,
and $D\mapsto[\mathcal O_C(D)]$ identifies $\operatorname{Cl}(C)$ with
$\operatorname{Pic}(C)$.
