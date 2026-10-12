+++
id = "lemma-nagata-strict-transform-closure-characterization"
kind = "lemma"
title = "Scheme-theoretic closure characterization"
order = 167
lean = ["AlgebraicGeometry.strictTransform"]
uses = ["lemma-nagata-power-torsion-kernel-localization", "lemma-nagata-power-torsion-quotient-torsionfree", "prop-nagata-strict-transform-closed-fiber-product"]
+++
Let $f\colon Y\to X$, let $\mathcal I$ be a quasi-coherent
ideal on $X$, put $X'=\operatorname{Bl}_{\mathcal I}(X)$, and let
$U=X\setminus V(\mathcal I)$. The strict transform is the smallest
closed subscheme of $Y\times_XX'$ through which

$$
Y\times_XU\longrightarrow Y\times_XX'
$$

factors. In particular it is the scheme-theoretic closure of this open
part.
