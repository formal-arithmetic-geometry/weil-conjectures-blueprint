+++
kind  = "proof"
of    = "det-lem-coefficient-finite-descent-hom"
+++
(1) $F_X$ and $\QbarX$ are flat over $E_X$ ([lem-sfb-subfield-flat], [lem-sfb-qlbar-flat]),
so extension of scalars is exact on complexes and is left adjoint to the exact restriction of
scalars on the derived categories (the module-level adjunction applied termwise). For
$F\subseteq F'$ the adjunction isomorphisms are compatible with the transition maps
$D_F\to D_{F'}$, since extension of scalars along $E\to F\to F'$ is the composite.

(2) Tensor products commute with colimits and $\QbarX=\varinjlim_FF_X$ as $E_X$-modules
([sk-prop-sfb-qlbar-colimit-x]); the index poset of finite $F\supseteq E$ is filtered. Each
$D^n\otimes F_X$ vanishes where $D^n$ does.

(3) By (1) the map becomes
$\varinjlim_F\Hom_{D(X,E)}(C,D^\bullet\otimes F_X[r])\to\Hom_{D(X,E)}(C,(\varinjlim_FD^\bullet\otimes F_X)[r])$,
using (2) and that $D^\bullet\otimes\QbarX$ represents $D_{\Qlb}$ by flatness. This is bijective by
[sk-lem-constructible-ext-continuity] (1), applied to $C\in\Dbc(X,E)$ and the filtered system
of (2). Unwinding the adjunctions, the bijection is the map induced by extension of scalars.
