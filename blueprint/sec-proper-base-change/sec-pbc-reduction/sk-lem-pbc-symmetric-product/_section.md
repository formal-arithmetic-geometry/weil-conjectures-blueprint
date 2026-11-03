+++
id = "sk-lem-pbc-symmetric-product"
kind = "lemma"
title = "A finite cover of projective space"
order = 216
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_isFinite_surjective_projectiveLinePow", "AlgebraicGeometry.ProjectiveSpace.symmetricProduct", "AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveSpace"]
uses = ["sk-def-pbc", "sk-thm-p1", "sk-lem-pbc-finite", "sk-lem-pbc-composition-cancellation", "sk-prop-av-isogeny", "sec-picard-framework"]
tags = ["sketch"]
+++
For every scheme $S$ and every $n\geq1$ there is a finite surjective
$S$-morphism

$$
\sigma_n:(\mathbf P^1_S)^n\longrightarrow\mathbf P^n_S.
$$

Consequently, if $\mathrm{PBC}_\Lambda(\mathbf P^1_S\to S)$ holds for every
scheme $S$, then $\mathrm{PBC}_\Lambda(\mathbf P^n_S\to S)$ holds for every
scheme $S$ and every $n\geq0$.
