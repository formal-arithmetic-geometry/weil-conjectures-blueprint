+++
id = "def-nagata-extended-admissible-blowup"
kind = "definition"
title = "Extension construction for an admissible blow-up"
order = 441
lean = ["AlgebraicGeometry.IsAdmissible.exists_extend"]
uses = ["def-nagata-admissible-blowup", "def-nagata-blowup-universal-graded-map", "def-nagata-blowup-universal-lift", "def-nagata-finite-type-ideal-extension", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "lemma-nagata-blowup-universal-exists", "lemma-nagata-blowup-universal-unique", "lemma-nagata-extend-finite-type-ideal", "lemma-nagata-glue-finite-type-ideals", "lemma-nagata-qc-open-complement-ideal-exists", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property"]
+++
Let $X$ be quasi-compact and quasi-separated and let $U,W\subseteq X$ be
quasi-compact opens. Write a given $(U\cap W)$-admissible blow-up of $W$
as $\operatorname{Bl}_{\mathcal J}(W)\to W$. Its center ideal restricts
to the unit ideal on $U\cap W$, so glue $\mathcal J$ on $W$ with the unit
ideal on $U$ to an ideal $\mathcal J^+$ on $U\cup W$ using
[lemma-nagata-glue-finite-type-ideals], and set

$$
\mathcal I_{X}(\mathcal J)
=\operatorname{Ext}_{X,U\cup W}(\mathcal J^+),
$$

and define

$$
\mathsf{ExtBl}_{X,W,U}(\mathcal J)
=\operatorname{Bl}_{\mathcal I_X(\mathcal J)}(X)\longrightarrow X.
$$
