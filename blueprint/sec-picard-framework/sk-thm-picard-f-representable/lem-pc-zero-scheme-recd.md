+++
id = "lem-pc-zero-scheme-recd"
kind = "lemma"
title = "The zero scheme of the adjoint section"
order = 834
lean = ["AlgebraicGeometry.isInvertible_zeroLocus_directImageCounit", "AlgebraicGeometry.exists_isEffectiveCartierCenter_hilbertPresheaf_zeroLocus_adjointSection", "AlgebraicGeometry.Scheme.Modules.Hom.zeroLocus_adjointSection_comp_whiskerLeft"]
uses = ["cor-picard-degree-g", "def-pc-curve", "def-pc-degree-line-bundle", "def-pc-euler-characteristic", "def-pc-f-subfunctor", "def-pc-finite-locally-free", "def-pc-genus", "def-pc-rational-point", "def-pc-relative-effective-cartier", "def-pc-smooth-projective-curve", "def-pc-zero-scheme", "def-nagata-invertible-ideal", "def-sc-invertible-module", "lem-pc-cartier-criterion", "lem-pc-cech-resolution", "lem-pc-coherent-hi", "lem-pc-degree-base-change", "lem-pc-dim-base-change", "lem-pc-f-open-subfunctor", "lem-pc-flat-base-change-cohom", "lem-pc-proper-base-change", "lem-pc-rational-hyp", "lem-pc-recd-locally-principal", "lem-pc-rf-base-change-flat-module", "lem-pc-smooth-flat", "lem-pc-vanishing-above-dim", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be a field and let $X$ be a $k$-scheme which is proper, smooth of
relative dimension $1$ and geometrically integral over $k$, of genus
$g=\dim_kH^1(X,\mathcal O_X)$, with a $k$-rational point $\sigma$. Let $T$ be
a scheme over $k$ and let
$\mathcal{L}\in F(T)\subseteq\operatorname{Pic}_{X/k,\sigma}(T)$ (with $F$ as in
[lem-pc-f-open-subfunctor]). Let $\mathcal{N}$ be an invertible
$\mathcal{O}_T$-module with $Rf_{T,*}\mathcal{L}\cong\mathcal{N}[0]$ (for instance
$\mathcal N=f_{T,*}\mathcal L$), and let $s$ be the section
of $\mathcal{L}\otimes_{\mathcal{O}_{X_T}}f_T^*\mathcal{N}^{-1}$ corresponding to the adjunction
map $f_T^*\mathcal{N}\to\mathcal{L}$ (via
$\operatorname{Hom}(f_T^*\mathcal{N},\mathcal{L})\cong H^0(X_T,\mathcal{L}\otimes f_T^*\mathcal{N}^{-1})$,
the tensor-Hom adjunction, $\mathcal{N}$ invertible). Then the
zero scheme $D:=Z(s)$, which is also the zero scheme of the adjunction
map, is a relative effective Cartier divisor on $X_T/T$ (its ideal sheaf
is invertible and $D\to T$ is flat) which is finite locally free of
degree $g$ over $T$.
