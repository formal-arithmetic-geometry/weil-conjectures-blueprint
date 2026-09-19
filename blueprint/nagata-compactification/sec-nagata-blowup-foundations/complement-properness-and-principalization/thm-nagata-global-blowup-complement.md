+++
id = "thm-nagata-global-blowup-complement"
kind = "theorem"
title = "Complement of the center"
order = 240
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isIso_blowupMap_restrict_support_compl"]
uses = ["lemma-nagata-affine-blowup-complement", "prop-nagata-global-blowup-affine-restrict"]
+++
Let $U=X\setminus V(\mathcal I)$. The restriction

$$
b_{X,\mathcal I}^{-1}(U)\longrightarrow U
$$

is an isomorphism.

## Proof

Cover $X$ by affine opens. Under
[prop-nagata-global-blowup-affine-restrict], the restriction over each
affine is the affine complement isomorphism of
[lemma-nagata-affine-blowup-complement]. These local isomorphisms glue,
and isomorphisms are local on source and target.
