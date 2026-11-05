+++
id = "lemma-integral-linear-character--1"
kind = "lemma"
title = "The zero form"
order = 1225002
aliases = ["bp-r378-1"]
lean = ["AlgebraicGeometry.WeilComplex.nonempty_iso_upperStar_comp_derivedLowerShriek_of_isPullback"]
uses = ["definition-weil-structure", "proposition-construction-independence-rf-shriek", "definition-tate-twists"]
+++
Let $\pi:Y\simeq X\times_{k_0}\mathbf A^1\to X$ be the trivial line
bundle in the relative setting above. There is an isomorphism

$$
R\pi_!\pi^*P\simeq P(-1)[-2]
$$

natural in the Weil complex $P$ on $X$.

This is the relative Thom isomorphism used for the zero form. In Lean
it is supplied as an input with proof `sorry`; the declaration asserts
the existence of a natural isomorphism and does not specify its trace
normalization. In the zero-locus calculation,
`AlgebraicGeometry.nonempty_iso_artinSchreierOf_zero` first identifies
$\mathcal L_\psi(0)$ with the constant sheaf, after which this
isomorphism applies.
