+++
id = "def-kun-rel-cup"
kind = "definition"
title = "Relative cup product"
order = 6130
lean = ["AlgebraicGeometry.Etale.relativeCup"]
uses = ["def-kun-derived-tensor", "lem-kun-inverse-image-monoidal"]
+++
Let $f:X\to Y$ be a morphism of schemes and $\Lambda$ a commutative ring.
For $K,L\in D(X_{\Et},\Lambda)$ the *relative cup product* is the morphism
$$
 \mathrm{cup}_{f,K,L}:\quad
 Rf_*K\otimes^{\mathbf L}_{\Lambda}Rf_*L\longrightarrow
 Rf_*(K\otimes^{\mathbf L}_{\Lambda}L)
$$
in $D(Y_{\Et},\Lambda)$ which is adjoint to the composite
$$
 f^{-1}(Rf_*K\otimes^{\mathbf L}_{\Lambda}Rf_*L)
 \xrightarrow{\ \sim\ }
 f^{-1}Rf_*K\otimes^{\mathbf L}_{\Lambda}f^{-1}Rf_*L
 \xrightarrow{\ \varepsilon_f\otimes\varepsilon_f\ }
 K\otimes^{\mathbf L}_{\Lambda}L,
$$
where the first map is the monoidality isomorphism of
[lem-kun-inverse-image-monoidal] for the inverse image $f^{-1}$ and the second
uses the derived counits (*Source:* Stacks Project,
[Tag `0B6C`](https://stacks.math.columbia.edu/tag/0B6C)).

Unresolved dependencies: def:weil-pbc-inverse-image
