+++
id = "lem-fd-stalk-at-origin"
kind = "lemma"
title = "Stalk of the transform at the origin of the dual line"
lean = ["AlgebraicGeometry.nonempty_equiv_stalk_homologySheaf_fourierTransform_origin", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_equiv_stalk_fourierTransform_middleExtension_origin"]
order = 4017
uses = ["def-fd-kernel", "def-fd-transform", "def-weil-ordinary-compact-cohomology", "lem-fd-stalk-formula"]
+++
Let $K_0$ be a Weil complex on $\mathbf A^1_{k_0}$ (in the
conventions of [def-fd-transform]) and let $0'$ be the origin of
the dual line $V^\vee$. In the compact-support convention of
[def-weil-ordinary-compact-cohomology] there is a canonical
isomorphism

$$
\bigl(\operatorname{FT}_\psi(K)\bigr)_{0'}\;\cong\;R\Gamma_c\bigl(\mathbf A^1_{k_0},K\bigr)[1].
$$

In particular, for the middle extension
$K=j_{!*}\mathcal M[1]=j_*\mathcal M[1]$ of a lisse sheaf
$\mathcal M$ on $U_0\subset\mathbf A^1_{k_0}$, the stalk at
$0'$ has exactly two possibly nonzero cohomology groups, in degrees
$-1$ and $0$:

$$
\mathcal H^{-1}\bigl(\operatorname{FT}_\psi(j_*\mathcal M[1])_{0'}\bigr)
\cong H_c^1(\mathbf A^1_{k_0},j_*\mathcal M),
\qquad
\mathcal H^0\bigl(\operatorname{FT}_\psi(j_*\mathcal M[1])_{0'}\bigr)
\cong H_c^2(\mathbf A^1_{k_0},j_*\mathcal M).
$$
