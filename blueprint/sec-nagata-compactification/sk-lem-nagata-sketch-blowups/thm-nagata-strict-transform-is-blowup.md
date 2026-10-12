+++
id = "thm-nagata-strict-transform-is-blowup"
kind = "theorem"
title = "[stacks-project]"
order = 169
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comap_iso_strictTransform"]
uses = ["def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-scheme-theoretic-closure", "def-nagata-strict-transform", "lemma-nagata-strict-transform-closure-characterization", "prop-nagata-global-blowup-cover-independent"]
+++
Let $f\colon Y\to X$ be a morphism, let $\mathcal I$ be a quasi-coherent
ideal on $X$, put $X'=\operatorname{Bl}_{\mathcal I}(X)$, and let
$Y^{\mathrm{st}}\subseteq Y\times_XX'$ be the strict transform of $Y$
relative to $X\setminus V(\mathcal I)$. Then there is an isomorphism
$\operatorname{Bl}_{\mathcal I\mathcal O_Y}(Y)\cong Y^{\mathrm{st}}$
compatible with the projections to $Y$ and with the morphisms to $X$.
