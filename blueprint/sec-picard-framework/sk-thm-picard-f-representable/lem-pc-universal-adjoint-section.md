+++
id = "lem-pc-universal-adjoint-section"
kind = "lemma"
title = "The adjoint section of the normalized universal module"
lean = ["AlgebraicGeometry.zeroLocus_directImageCounit_eq_of_iso", "AlgebraicGeometry.Scheme.Modules.nonempty_tensorObj_dual_pullback_pushforward_iso", "AlgebraicGeometry.isQuasicoherent_pushforward_dual_toModules", "AlgebraicGeometry.zeroLocus_adjointSection_eq_of_iso"]
order = 837
uses = ["def-pc-f-subfunctor", "def-pc-finite-locally-free", "def-pc-genus", "def-pc-hilb-functor", "def-pc-rational-point", "def-pc-zero-scheme", "def-nagata-invertible-ideal", "lem-pc-projection-formula", "lem-pc-universal-divisor", "lem-pc-zero-scheme-recd"]
+++
Let $k$ be a field and let $X$ be a $k$-scheme which is proper, smooth of
relative dimension $1$ and geometrically integral over $k$, of genus $g$, with
a $k$-rational point $\sigma$. Let $T$ be a scheme over $k$, write
$f_T:X_T\to T$, and let $D\subset X_T$ be an effective Cartier divisor.

1. $f_{T,*}\mathcal{O}_{X_T}(D)$ is a quasi-coherent $\mathcal{O}_T$-module.
1. (*The $\sigma$-terms cancel.*) If $\mathcal{L}\cong\mathcal{O}_{X_T}(D)\otimes f_T^*\mathcal{M}$
for an invertible $\mathcal{O}_T$-module $\mathcal{M}$ and $f_{T,*}\mathcal{O}_{X_T}(D)$ is
invertible, then $f_{T,*}\mathcal{L}$ is invertible and
$$
\mathcal{L}\otimes f_T^*(f_{T,*}\mathcal{L})^{-1}\;\cong\;
\mathcal{O}_{X_T}(D)\otimes f_T^*\bigl(f_{T,*}\mathcal{O}_{X_T}(D)\bigr)^{-1}.
$$
1. (*The adjoint section has zero scheme $D$.*) Let
$\mathcal{L}\in F(T)\subseteq\operatorname{Pic}_{X/k,\sigma}(T)$ ([def-pc-f-subfunctor]),
assume $D\in\operatorname{Hilb}^g_{X/k}(T)$ ([def-pc-hilb-functor]) and
$\mathcal{L}\cong\mathcal{O}_{X_T}(D)\otimes f_T^*\mathcal{N}'$ for some invertible
$\mathcal{O}_T$-module $\mathcal{N}'$, and let $\mathcal{N}$ be an invertible
$\mathcal{O}_T$-module with $\mathcal{N}\cong f_{T,*}\mathcal{L}$. Then the section $s$ of
$\mathcal{L}\otimes f_T^*\mathcal{N}^{-1}$ adjoint to the adjunction map
$f_T^*\mathcal{N}\to\mathcal{L}$ ([lem-pc-zero-scheme-recd]) has zero scheme
$Z(s)=D$.

In particular, for $H=\underline{\operatorname{Hilb}}^g_{X/k}$ with universal divisor
$D_{\mathrm{univ}}\subset H\times X$ ([lem-pc-universal-divisor]), the normalized
universal module
$\mathcal{L}_H=\mathcal{O}(D_{\mathrm{univ}})\otimes\mathrm{pr}_H^*\sigma_H^*\mathcal{O}(D_{\mathrm{univ}})^{-1}$
and the open $W\subseteq H$ over which $\mathcal{L}_H$ lies in $F$, the adjoint
section of $\mathcal{L}_H|_{W\times X}$ has zero scheme $D_{\mathrm{univ}}\cap(W\times X)$.
