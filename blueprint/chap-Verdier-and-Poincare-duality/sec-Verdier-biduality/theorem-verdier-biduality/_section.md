+++
id = "theorem-verdier-biduality"
kind = "theorem"
title = "Verdier biduality"
order = 845
lean = ["AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app", "AlgebraicGeometry.Etale.verdierDualEquivalence", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_of_field"]
uses = ["definition-relative-dualizing-complex", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For every admissible coefficient ring $\Lambda$ and every scheme $X$,

$$
\delta_K:K\xrightarrow{\sim}\mathbb D_X\mathbb D_XK
\qquad(K\in D^b_{\mathrm{ctf}}(X,\Lambda)).
$$

Thus $\mathbb D_X$ is an exact anti-equivalence of
$D^b_{\mathrm{ctf}}(X,\Lambda)$ with itself.
