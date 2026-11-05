+++
id = "lemma-perverse-sheaves-curve--2"
kind = "lemma"
title = "Basic curve perverse Weil complexes"
name_showing = false
order = 1249002
aliases = ["bp-r386-2"]
lean = ["AlgebraicGeometry.WeilComplex.isCurvePerverse_toComplex_obj", "AlgebraicGeometry.WeilComplex.isCurvePerverse_shift_one_toComplex", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isCurvePerverse_middleExtension"]
uses = ["definition-weil-structure", "definition-perverse-sheaves-curve", "definition-punctual-sheaf", "definition-lisse-sheaves", "proposition-topos-functoriality"]
+++
Let $k_0$ be a finite field, let $\ell$ be a prime different from
$\operatorname{char}(k_0)$, and let $X_0$ be a $k_0$-scheme. Apply the
cohomological conditions of Definition [definition-perverse-sheaves-curve]
to Weil $\overline{\mathbf Q}_\ell$-complexes on $X_0$, without assuming
that $X_0$ is a curve. Here finite support means that only finitely many
points with finite residue field have a nonzero geometric stalk.

A Weil sheaf $G$ with finite support, placed in degree zero, is curve
perverse. If a Weil sheaf $G$ has no nonzero Weil subsheaf with finite
support, then $G[1]$ is curve perverse.

For a dense quasi-compact open immersion
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and a lisse Weil
$\overline{\mathbf Q}_\ell$-sheaf $M$ on $U_0$, the complex $(j_*M)[1]$
is curve perverse.
