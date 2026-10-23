+++
id = "lem-sc-h1-gm-pic"
kind = "lemma"
title = "The Picard group as first cohomology of units"
lean = ["AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroup", "AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroup_mul", "AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroupAddEquiv", "AlgebraicGeometry.Scheme.nonempty_equiv_cohomologicalPicardGroup", "AlgebraicGeometry.Scheme.nonempty_addEquiv_cohomologicalPicardGroup", "AlgebraicGeometry.Scheme.CohomologicalPicardGroup"]
order = 1353
uses = ["def-sc-curves", "def-sc-gm-torsor", "def-sc-invertible-module", "def-sc-picard-group", "thm-sc-hilbert-90"]
+++
Let $X$ be a scheme (for instance a curve $C$ as in [def-sc-curves]).
The map

$$
\operatorname{Pic}(X)\xrightarrow{\ \sim\ }H^1(X_{\Et},\mathbf G_m),
\qquad
[\mathcal L]\longmapsto\big[\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})\big],
$$

from the Picard group of [def-sc-picard-group] (isomorphism classes of
invertible modules, [def-sc-invertible-module]) to the first etale
cohomology of $\mathbf G_m$, sending $\mathcal L$ to the class of the
$\mathbf G_m$-torsor of its local trivializations
([def-sc-gm-torsor]), is an isomorphism of abelian groups. In
particular $H^1(C_{\Et},\mathbf G_m)\cong\operatorname{Pic}(C)$ for a
curve $C$.
