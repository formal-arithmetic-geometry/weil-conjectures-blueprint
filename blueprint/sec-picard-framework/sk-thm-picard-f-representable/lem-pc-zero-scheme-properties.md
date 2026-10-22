+++
id = "lem-pc-zero-scheme-properties"
kind = "lemma"
title = "Properties of the zero scheme"
order = 832
uses = ["def-pc-base-change", "def-pc-scheme", "def-sc-invertible-module", "lem-pc-divisor-line-bundle-properties", "lem-pc-tensor-dual-invertible"]
lean = ["AlgebraicGeometry.Scheme.Modules.Hom.ideal_zeroLocus", "AlgebraicGeometry.Scheme.Modules.Hom.isLocallyPrincipal_zeroLocus", "AlgebraicGeometry.Scheme.Modules.Hom.comap_zeroLocus", "AlgebraicGeometry.Scheme.Modules.Hom.zeroLocus_eq_bot_iff", "AlgebraicGeometry.Scheme.Modules.Hom.zeroLocus", "AlgebraicGeometry.Scheme.Modules.Hom.imageSubobject_dualMap_comp_dualUnitIso"]
+++
Let $X$ be a scheme, $\mathcal{M},\mathcal{N}$ invertible
$\mathcal{O}_X$-modules and $\varphi\colon\mathcal{M}\to\mathcal{N}$ a morphism.
On an open $U$ on which $\mathcal M$ and $\mathcal N$ are free on generators
$e_{\mathcal M}$ and $e_{\mathcal N}$, write
$\varphi(e_{\mathcal M})=b\cdot e_{\mathcal N}$ with $b\in\Gamma(U,\mathcal O_X)$.

1. There is a unique closed subscheme $Z(\varphi)\subseteq X$, the *zero
scheme* of $\varphi$, such that for every affine open
$U=\operatorname{Spec}(A)$ as above $Z(\varphi)\cap U=\operatorname{Spec}(A/(b))$.
In particular $Z(\varphi)$ is a locally principal closed subscheme.
1. For every morphism $g\colon Y\to X$, the zero scheme of the pullback
$g^*\varphi\colon g^*\mathcal M\to g^*\mathcal N$ is
$Z(g^*\varphi)=Z(\varphi)\times_XY$.
1. $Z(\varphi)=X$ if and only if $\varphi=0$.

For a global section $s\in H^0(X,\mathcal{M})$, viewed as the morphism
$s\colon\mathcal O_X\to\mathcal M$, this is the zero scheme
$Z(s)=Z(\varphi)$, whose ideal sheaf is
$\operatorname{im}(s^\vee\colon\mathcal M^\vee\to\mathcal O_X)$.
