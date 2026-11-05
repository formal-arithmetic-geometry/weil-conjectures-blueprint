+++
id = "lemma-kunneth-finite-direct-image--1"
kind = "lemma"
title = "Finite direct images of constant sheaves (1)"
name_showing = false
order = 711001
aliases = ["bp-r214-1"]
lean = ["AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_rightDerivedLowerStar_unit", "AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_lowerStar_unit"]
uses = ["definition-derived-base-change-map", "definition-kunneth-map"]
+++
The finite direct image calculation has the following form in Lean. Let $A$
be a finite commutative ring, and let
$h:Y\to X'$, $e:Y\to T$, $f':X'\to S'$ and $g:T\to S'$ be morphisms of
schemes with $f'h=ge$. For $Q\in D(X'_{\acute{e}t},A)$ and
$F\in D(T_{\acute{e}t},A)$, write

$$
\beta_{Q,F}:Q\otimes^{\mathbf L}f'^*Rg_*F
\longrightarrow Rh_*(h^*Q\otimes^{\mathbf L}e^*F)
$$

for the adjoint transpose of the tensor comparison for $h^*$ followed by
the pullback of the counit $g^*Rg_*F\to F$. Pullbacks here are exact, and
the derived categories are unbounded.

Let $\pi':X'_i\to X'$ be finite, and let $h_i:Y_i\to X'_i$ and
$\rho:Y_i\to Y$ form its cartesian base change along $h$, so that
$\pi'h_i=h\rho$. Suppose that both base change maps

$$
f'^*Rg_*F\longrightarrow Rh_*e^*F,
\qquad
\pi'^*Rh_*e^*F\longrightarrow Rh_{i*}\rho^*e^*F
$$

are isomorphisms. Then $\beta_{R\pi'_*A_{X'_i},F}$ is an isomorphism.
No boundedness, constructibility or finite Tor amplitude assumption on $F$
is needed for this assertion.

In the geometric application, let $k$ be a field in which the exponent of
$A$ is invertible. Let $a:X\to\operatorname{Spec}(k)$ be of finite type,
let $b:S'\to\operatorname{Spec}(k)$ be any morphism, and suppose that
$X'=X\times_k S'$ with projections $p:X'\to X$ and $f':X'\to S'$.
Let $g:T\to S'$ be quasi-compact and quasi-separated, and suppose that
$Y=X'\times_{S'}T$ with projections $h$ and $e$. For every finite morphism
$\pi:X_i\to X$ and every sheaf $\mathcal F$ of $A$-modules on
$T_{\acute{e}t}$, placed in degree $0$, the map

$$
\beta_{p^*(\pi_*A_{X_i}),\mathcal F}:
p^*(\pi_*A_{X_i})\otimes^{\mathbf L}f'^*Rg_*\mathcal F
\longrightarrow
Rh_*(h^*p^*(\pi_*A_{X_i})\otimes^{\mathbf L}e^*\mathcal F)
$$

is an isomorphism. This is the single-sheaf case used in Lean's dévissage;
finite sums are handled by additivity. The external Künneth map (8.4)
is obtained from this tensor comparison by taking the product square and
interchanging the two tensor factors.
