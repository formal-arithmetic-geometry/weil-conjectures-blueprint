+++
id = "lem-sfb-open-projection-formula"
kind = "lemma"
title = "Projection formula for extension by zero"
order = 1312
uses = ["lem-weil-pbc-sheaf-tensor-closed", "sk-def-sfb-finite-pushforward-pullback", "det-def-sfb-finite-lower-shriek"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.hasProjectionFormula_openImmersion"]
+++
Let $j\colon U\to X$ be an open immersion, and $j^{\Ab}_!\dashv j^*_{\Ab}$ the
extension by zero and the pullback of abelian pro-étale sheaves
([det-def-sfb-finite-lower-shriek], [sk-def-sfb-finite-pushforward-pullback]). For
$L\in\Sh(X_{\mathrm{proét}},\Ab)$ and $M\in\Sh(U_{\mathrm{proét}},\Ab)$ the canonical
map

$$
j^{\Ab}_!(j^*_{\Ab}L\otimes M)\longrightarrow L\otimes j^{\Ab}_!M,
$$

adjoint to $j^*_{\Ab}L\otimes M\to j^*_{\Ab}L\otimes j^*_{\Ab}j^{\Ab}_!M\cong
j^*_{\Ab}(L\otimes j^{\Ab}_!M)$ (unit of $j^{\Ab}_!\dashv j^*_{\Ab}$ and strong
monoidality of $j^*_{\Ab}$), is an isomorphism; here $\otimes$ is the tensor product
of [lem-weil-pbc-sheaf-tensor-closed].
