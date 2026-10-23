+++
id = "det-prop-picard-degree-decomposition"
kind = "proposition"
title = "Degree decomposition of the Picard scheme"
order = 857
uses = ["thm-pc-pic-split", "thm-pc-picard-representable", "lem-sc-riemann-roch", "det-thm-picard-semicon"]
lean = ["AlgebraicGeometry.picardFunctorDegree", "AlgebraicGeometry.exists_decomposition_picardFunctor", "AlgebraicGeometry.exists_decomposition_picardFunctor_representableBy", "AlgebraicGeometry.exists_decomposition_picardFunctor_isMonHom", "AlgebraicGeometry.exists_decomposition_picardTranslation"]
+++
Let $k$ be separably closed, $C$ a $k$-scheme which is proper, smooth of
relative dimension $1$ and geometrically integral over $k$, $P\in C(k)$,
and $\underline{\Pic}_{C/k}$ a $k$-scheme representing $\Pic_{C/k}$, with
universal class $\cL$. The function $t\mapsto\deg\cL_t$ is locally constant on
$\underline{\Pic}_{C/k}$. Hence

$$
\underline{\Pic}_{C/k}=\coprod_{d\in\Z}\underline{\Pic}^d_{C/k},
\qquad
\underline{\Pic}^d_{C/k}:=\{t:\deg\cL_t=d\},
$$

each $\underline{\Pic}^d_{C/k}$ is open and closed and represents the
subfunctor of classes of fibrewise degree $d$, $\underline{\Pic}^0_{C/k}$
is an open and closed subgroup scheme, and tensoring with
$\cO_C(dP)$ is an isomorphism of schemes
$\underline{\Pic}^0_{C/k}\xrightarrow{\sim}\underline{\Pic}^d_{C/k}$.
