+++
id = "lemma-nagata-proper-separated-valuation-extension"
kind = "lemma"
title = "Valuative extension to a proper separated morphism"
order = 297
lean = ["AlgebraicGeometry.IsProper.eq_valuativeCriterion"]
uses = ["lemma-nagata-proper-valuative-criterion-existence-api", "lemma-nagata-separated-valuation-lift-unique"]
+++
A morphism $f\colon Y\to S$ is proper if and only if it is
quasi-compact, quasi-separated and locally of finite type, and every
commutative square

$$
\operatorname{Spec}(K)\longrightarrow Y
\qquad\text{over}\qquad
\operatorname{Spec}(A)\longrightarrow S
$$

with $A$ a valuation ring and $K=\operatorname{Frac}(A)$ admits a unique
lift $\operatorname{Spec}(A)\to Y$.
