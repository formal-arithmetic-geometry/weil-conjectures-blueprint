+++
id = "definition-projection-formula-map"
kind = "definition"
title = "Projection formula map"
order = 416
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves"]
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
