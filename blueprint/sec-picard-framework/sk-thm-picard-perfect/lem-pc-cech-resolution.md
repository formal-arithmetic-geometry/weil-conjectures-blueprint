+++
id = "lem-pc-cech-resolution"
kind = "lemma"
title = "The Cech resolution and derived direct image"
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_homology_cechModuleComplex_linearEquiv", "AlgebraicGeometry.Scheme.Modules.quasiIso_cechResolution\u03b9", "AlgebraicGeometry.Scheme.Modules.rightAcyclic_cechResolution_X", "AlgebraicGeometry.Scheme.Modules.higherDirectImageIsoCechResolution"]
order = 754
uses = ["def-pc-derived-direct-image", "def-pc-morphism-conventions", "def-pc-scheme", "lem-pc-affine-morphism-hi", "pqf-lem-affine-vanishing"]
+++
Let $S=\operatorname{Spec}(A)$, let $f:X\to S$ be a separated morphism,
and let $X=\bigcup_{i\in I}U_i$ be a finite cover by affine opens. For an
$\mathcal O_X$-module $\mathcal F$ and a tuple $y=(i_0,\dots,i_p)\in I^{p+1}$
write $U_y=U_{i_0}\cap\dots\cap U_{i_p}$ and $j_y:U_y\to X$. The augmented
(ordered) Cech complex of sheaves

$$
0\longrightarrow\mathcal F\longrightarrow
\prod_{i\in I} j_{i,*}(\mathcal F|_{U_i})\longrightarrow
\prod_{(i_0,i_1)\in I^2}j_{(i_0,i_1),*}(\mathcal F|_{U_{i_0i_1}})\longrightarrow\cdots,
$$

with the alternating sum of the restriction maps as differential, is exact.
If $\mathcal F$ is quasi-coherent, its non-augmented terms are
$f_*$-acyclic, so applying $f_*$ to it computes the higher direct images:
$R^qf_*\mathcal F\cong H^q\bigl(f_*\check{\mathcal C}^\bullet(\mathcal U,\mathcal F)\bigr)$
for all $q\ge0$. On global sections this says that the Cech complex
$\check C^\bullet(\mathcal U,\mathcal F)$ of $A$-modules has
$H^q(\check C^\bullet(\mathcal U,\mathcal F))\cong\Gamma(S,R^qf_*\mathcal F)$.
