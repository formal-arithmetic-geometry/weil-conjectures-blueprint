+++
id = "lem-weil-pbc-limit-affine-transition-affine-comparison"
kind = "lemma"
title = "Affine comparison for affine transition limit"
lean = ["AlgebraicGeometry.limit_affine_transition_affine_comparison"]
order = 1878
+++
Let $I$ be a nonempty directed set and $(D_i)_{i\in I}$ an inverse system of schemes indexed by $I$ whose transition morphisms $D_j\to D_i$ ($i\le j$) are affine, and suppose every $D_i$ is affine. Let $c$ be a limit cone of the system, with vertex $D$ and projections $\pi_i:D\to D_i$. Then there is an isomorphism $e:D\xrightarrow{\sim}\operatorname{Spec}\bigl(\varinjlim_i\Gamma(D_i,\mathcal O_{D_i})\bigr)$ such that for every $i$ the composite of $e$ with $\operatorname{Spec}$ of the colimit coprojection $\Gamma(D_i,\mathcal O_{D_i})\to\varinjlim_j\Gamma(D_j,\mathcal O_{D_j})$ equals $\pi_i$ followed by the canonical morphism $D_i\to\operatorname{Spec}\Gamma(D_i,\mathcal O_{D_i})$.
