+++
id = "definition-projection-formula-map--1"
kind = "definition"
title = "Projection formula map (1)"
name_showing = false
order = 416001
aliases = ["bp-r126-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.projectionMap"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1"]
+++
Let $p:X\to Y$ be a morphism, $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ and
$M\in D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$. The *projection formula map*

$$
Rp_*K\otimes^{\mathbf L}M\longrightarrow Rp_*(K\otimes^{\mathbf L}p^*M)
\tag{4.14}
$$

is the adjoint, under $p^*\dashv Rp_*$, of the composite
$p^*(Rp_*K\otimes^{\mathbf L}M)\simeq p^*Rp_*K\otimes^{\mathbf L}p^*M
\to K\otimes^{\mathbf L}p^*M$ of the monoidal isomorphism of $p^*$ and the
counit $p^*Rp_*K\to K$ tensored with $p^*M$.
