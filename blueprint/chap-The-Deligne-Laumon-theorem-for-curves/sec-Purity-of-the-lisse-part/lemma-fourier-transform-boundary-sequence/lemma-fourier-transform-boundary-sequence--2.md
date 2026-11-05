+++
id = "lemma-fourier-transform-boundary-sequence--2"
kind = "lemma"
title = "Lissity of the transformed boundary sheaf"
name_showing = false
order = 1273002
aliases = ["bp-r393-2"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_isLisse_iso_fourierTransform_boundarySheaf"]
uses = ["definition-weil-structure", "definition-lisse-sheaves", "prose-16-06"]
+++
The weight bound in the parent lemma is bypassed by the Lean route; the
available statement is the following lissity assertion.

Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open and let $M$
be any lisse Weil $\overline{\mathbf Q}_\ell$-sheaf on $U_0$.
Put $B=j_*M/j_!M$. For any additive character
$\psi:k_0\to\overline{\mathbf Q}_\ell^{\times}$, there is a Weil sheaf
$B'$ on the dual line, lisse on the entire line, and an isomorphism

$$
\operatorname{FT}_\psi(B)\simeq B'[1].
$$

This assertion requires neither irreducibility nor nonexceptionality,
and imposes no condition on the weights of $M$.
