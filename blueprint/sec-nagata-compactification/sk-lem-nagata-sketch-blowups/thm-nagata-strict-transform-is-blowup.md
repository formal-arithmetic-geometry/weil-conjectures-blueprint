+++
id = "thm-nagata-strict-transform-is-blowup"
kind = "theorem"
title = "[stacks-project]"
order = 161
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comap_iso_strictTransform"]
uses = ["def-nagata-dense-compactification", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "def-nagata-scheme-image-comparison", "def-nagata-scheme-theoretic-closure", "def-nagata-strict-transform", "def-nagata-strict-transform-blowup-comparison", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-strict-transform-over-complement", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property", "thm-nagata-global-blowup-complement"]
+++
Let $f\colon Y\to X$ be a morphism, let $\mathcal I$ be a quasi-coherent
ideal on $X$, put $X'=\operatorname{Bl}_{\mathcal I}(X)$, and let
$Y^{\mathrm{st}}\subseteq Y\times_XX'$ be the strict transform of $Y$
relative to $X\setminus V(\mathcal I)$. Then there is an isomorphism
$\operatorname{Bl}_{\mathcal I\mathcal O_Y}(Y)\cong Y^{\mathrm{st}}$
compatible with the projections to $Y$ and with the morphisms to $X$.
