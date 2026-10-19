+++
id = "lemma-nagata-dense-source-valuative"
kind = "lemma"
title = "Dense-source valuative criterion"
order = 289
lean = ["AlgebraicGeometry.IsProper.of_valuativeCriterion_of_isDominant", "AlgebraicGeometry.IsSeparated.of_valuativeCriterion_of_isDominant", "AlgebraicGeometry.UniversallyClosed.of_valuativeCriterion_of_isDominant"]
+++
Let $f\colon X\to S$ be a morphism of schemes, let
$h\colon U\to X$ be quasi-compact, and assume $h(U)$ is dense in $X$. Suppose that for every valuation
ring $A$ with fraction field $K$, every commutative diagram

$$
\operatorname{Spec}(K)\longrightarrow U\longrightarrow X,
\qquad
\operatorname{Spec}(A)\longrightarrow S
$$

has a unique lift $\operatorname{Spec}(A)\to X$. If $f$ is
quasi-compact, then $f$ is universally closed. If $f$ is quasi-separated,
then $f$ is separated. In particular, if $f$ is moreover of finite type and
quasi-separated, then $f$ is proper.
