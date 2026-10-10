+++
id = "thm-weil-final"
kind = "theorem"
title = "Weil conjectures for a smooth proper variety"
order = 2939
lean = ["AlgebraicGeometry.Scheme.weil_conjectures"]
uses = ["def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "prop-euler-product", "thm-weil-final-betti", "thm-weil-final-functional-equation", "thm-weil-final-integrality", "thm-weil-final-rationality", "thm-weil-final-rh"]
+++
Let $k_0$ be a finite field with $q$ elements, let $X_0$ be a scheme over
$k_0$ whose structure morphism $X_0\to\Spec k_0$ is smooth of relative
dimension $d$, proper and geometrically integral, and let $Z(X_0,T)\in\mathbf Q[[T]]$
be its point-count zeta series. Then there are polynomials
$P_0,\dots,P_{2d}\in\mathbf Z[T]$ such that:

1. (*Factorization.*) $P_i(0)=1$ for every $i$, $P_0(T)=1-T$,
$P_{2d}(T)=1-q^dT$, and
$$
Z(X_0,T)\prod_{\substack{0\leq i\leq2d\\ i\text{ even}}}P_i(T)
=\prod_{\substack{0\leq i\leq2d\\ i\text{ odd}}}P_i(T)
\quad\text{in }\mathbf Q[[T]].
$$
1. (*Functional equation.*) For every $0\leq i\leq2d$, the multiset of
complex roots of $P_{2d-i}$ is the image of the multiset of complex roots
of $P_i$ under $z\mapsto(q^dz)^{-1}$; equivalently, $\alpha\mapsto q^d/\alpha$
maps the reciprocal roots of $P_i$ bijectively, with multiplicity, onto
those of $P_{2d-i}$.
1. (*Riemann hypothesis.*) For every $0\leq i\leq2d$, every complex root
$z$ of $P_i$ satisfies $|z|=q^{-i/2}$; equivalently, every reciprocal root
of $P_i$ has absolute value $q^{i/2}$.

## Proof

The hypotheses make $\mathscr X=(X_0,d,X)$ a smooth-proper datum, so all
degreewise factors and Frobenius operators in Definitions
`[def-weil-smooth-proper-cohomological-family]` and
*Frobenius characteristic factors* are available.

*Clause (i).*
Definition [def-weil-point-counts-zeta] is the exponential point-counting
description. Proposition [prop-euler-product] gives the closed-point
Euler product and membership in $1+T\mathbf Z[[T]]$. Proposition
`prop-integral-recovery` gives the factorization by integral
polynomials and hence $Z(X_0,T)\in\mathbf Q(T)$.
This proves exactly the two displayed descriptions and both coefficient
claims in (i).

*Clause (ii).*
Proposition `prop-integral-recovery` applies to the fixed datum and says
that the canonical $P_i\in\mathbf Z[T]$ have constant term one, satisfy

$$
\bigl((\mathbf Z[T]\longrightarrow\Ql[T])(P_i)\bigr)(T)=P_{i,\ell}(T)
=\det(1-TF\mid H^i(X,\Ql))
$$

for every prime $\ell\neq p$, are the unique integral family with those
realizations, and obey

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}
\quad\text{in }\mathbf Q(T).
$$

These are precisely all assertions of (ii).

*Clause (iii).*
Fix $0\leq i\leq2d$. Proposition
`prop-arithmetic-roots` applies to the polynomial $P_i$ in the fixed
algebraic closure. It states that every reciprocal root is an algebraic
integer and a $q$-Weil number of weight $i$, with the displayed equality
for every complex embedding. The same proposition identifies an ordinary
root $\beta$ with the inverse of a reciprocal root of this same
polynomial $P_i$, and gives $|\tau(\beta)|=q^{-i/2}$. This proves
(iii) without changing the root terminology.

*Clause (iv).*
Fix an integer $0\leq i\leq2d$. For every prime $\ell\neq p$,
Proposition `prop-integral-recovery` gives

$$
b_i=\deg P_i=\dim_{\Ql}H^i(X,\Ql),
$$

so the left-hand side is independent of $\ell$. Proposition
`prop-duality-reciprocity` gives $b_i=b_{2d-i}$, and Proposition
`prop-endpoints` gives

$$
b_0=b_{2d}=1,\qquad P_0(T)=1-T,\qquad P_{2d}(T)=1-q^dT.
$$

Theorem [thm-weil-final-betti] states all of these equalities for the
same datum and, in addition, that $Z(X_0,T)$ has a pole of order exactly
$1$ at $T=1$ and, when $d\geq1$, at $T=q^{-d}$. This is exactly (iv).

*Clause (v).*
The definitions of $D_i,\chi,\varepsilon$ are respectively
Definitions `def-weil-determinant-constants`,
*Euler characteristic*,
and `def-weil-functional-equation-sign`. Proposition
`prop-duality-reciprocity` supplies, for every $i$, the asserted
degreewise Laurent reciprocity. Proposition
*Parity of the functional-equation exponent* verifies that $d\chi/2$ is an
integer. Finally Proposition `prop-functional-equation` proves

$$
\varepsilon\in\{1,-1\},\qquad
Z(X_0,q^{-d}T^{-1})
=\varepsilon q^{d\chi/2}T^\chi Z(X_0,T)
$$

in $\mathbf Q(T)$. Hence all assertions of (v) follow.

The five independently verified clauses are exactly the conjunction stated
in the theorem.
