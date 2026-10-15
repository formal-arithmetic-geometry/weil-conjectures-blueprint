+++
id = "sk-prop-cohsm"
kind = "proposition"
title = "The exceptional inverse image of a smooth morphism"
order = 1818
uses = ["sk-prop-a1", "sk-prop-an", "sk-prop-sf-cbc"]
lean = ["AlgebraicGeometry.Etale.isInvertible_dualizingComplex", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_obj_derivedTensor", "AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_comp_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Let $\Lambda$ be a finite $\ell$-primary coefficient ring and work with
schemes of finite type over the standing field $k$. Let $f:X\to S$ be
separated, smooth and of finite type, of pure relative dimension $d$, and let
$\omega_f=f^!\Lambda_S\in D_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)$ be its dualizing
complex. Then $\omega_f$ is pro-étale locally isomorphic to $\Lambda_X(d)[2d]$,
and the canonical map

$$
f^*N\otimes^{\mathbf L}_\Lambda\omega_f\longrightarrow f^!N
\quad\text{in }D_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)\qquad\text{(G11)}
$$

is an isomorphism for every $N\in D_{\mathrm{class}}(S_{\mathrm{proét}},\Lambda)$.
Moreover, let $g:S'\to S$ be a morphism, $X'=X\times_SS'$, and $f':X'\to S'$,
$g':X'\to X$ the projections. Then the canonical base-change map

$$
g'^*f^!N\longrightarrow f'^!g^*N
\quad\text{in }D_{\mathrm{class}}(X'_{\mathrm{proét}},\Lambda)\qquad\text{(G12)}
$$

is an isomorphism. It identifies $g'^*\omega_f$ with $\omega_{f'}$ and is
compatible with (G11).
