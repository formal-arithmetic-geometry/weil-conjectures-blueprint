+++
id = "thm-pur-trace-normalization-transitivity"
kind = "theorem"
title = "Trace normalization and transitivity"
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace_comp", "AlgebraicGeometry.Etale.smoothPurityTrace_baseChange", "AlgebraicGeometry.Etale.isIso_affineLineFundamentalClass_comp_smoothPurityTrace", "AlgebraicGeometry.Etale.exists_affineLineFundamentalClass_comp_smoothPurityTrace"]
order = 3043
uses = ["cor-pur-affine-space-purity", "cor-pur-affine-space-zero-section-purity", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-smooth-trace", "def-sbc-smooth-morphisms", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-amb-cartier-kummer-map", "lem-pur-projection-purity-agreement", "thm-pur-affine-line-orientation", "thm-pur-affine-line-purity", "thm-pur-composition-coherence", "thm-pur-finite-reduction-of-purity", "thm-pur-smooth-base-change-coherence", "thm-sf-comp-composition"]
+++
Work in the purity conventions of [def-pur-conventions], let
$\Lambda=A=A_{E,n}$, let $f:X\to Y$ and $g:Y\to Z$ be smooth separated
morphisms of relative dimensions $d$ and $e$, and let
$K\in D^b_{ctf}(Z,\Lambda)$. The typed composite

$$
\begin{array}{l}
R(gf)_!L(gf)^*K(d+e)[2d+2e]
\xrightarrow{\ \alpha_{g,f}^{-1}\ }
Rg_!Rf_!Lf^*Lg^*K(d+e)[2d+2e]\\
\hphantom{R(gf)_!L(gf)^*K(d+e)[2d+2e]}
\xrightarrow{\ Rg_!(\operatorname{Tr}^{\mathrm{sm}}_{f,Lg^*K(e)[2e]})\ }
Rg_!Lg^*K(e)[2e]
\xrightarrow{\ \operatorname{Tr}^{\mathrm{sm}}_{g,K}\ }K
\end{array}
$$

where $\alpha_{g,f}$ is the composition law of
[thm-sf-comp-composition],
equals $\operatorname{Tr}^{\mathrm{sm}}_{gf,K}$, after the pullback-composition
and twist-additivity identifications; thus the $f$-trace, with the
$(e)[2e]$ twist already present, is applied before the $g$-trace.
On every geometric fiber of a structural $f=p_d:\mathbf A^d\to\Spec k$,
the smooth trace

$$
\operatorname{Tr}^{\mathrm{sm}}_{p_d,\Lambda}:
R\Gamma_c(\mathbf A^d,\Lambda(d)[2d])\longrightarrow\Lambda
$$

is the product of the normalized affine-line traces of
[thm-pur-affine-line-purity]: it sends the ordered fundamental class
of $\mathbf A^d$, the $d$-fold tensor of the affine-line classes (each
the image in $R\Gamma_c(\mathbf A^1,\Lambda(1)[2])$ of the orientation
$\operatorname{pur}_s=\partial\kappa(t)$ of
[thm-pur-affine-line-orientation]), to $(-1)^d\in\Lambda$, and the
$d$-fold tensor of the Cartier classes of the zero section
([lem-amb-cartier-kummer-map]) to $1$.
The sign is that of [cor-pur-affine-space-zero-section-purity]: the
affine-line traces are normalized by the projective-line trace,
$t_q(c_1(\mathcal O(1)))=1$, and $\partial\kappa(t)$ is minus the Cartier
class. The smooth traces are compatible with arbitrary base
change of $Z$ and with the finite reductions
$A_{E,n}\to A_{E,m}$ of [thm-pur-finite-reduction-of-purity].

For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ the transitivity is
[sk-prop-sp-trace-composition] and the base-change compatibility is
[sk-prop-sp-purity-bc]. By [det-sp-purity-coefficient-change] the smooth
traces with these coefficients are obtained from the finite ones by reduction
(for $\mathcal O_E$), inversion of $\ell$ and extension of scalars, so the
normalization on $\mathbf A^d$ holds for them as well.
