+++
id = "proposition-local-structure-integral-constructible-complexes"
kind = "proposition"
title = "Local structure of integral constructible complexes"
order = 243
lean = ["AlgebraicGeometry.ProEtale.integral_local_structure"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves"]
+++
Let $X$ be Noetherian and let $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ be
derived complete with $K_1\in\Dbc(X,\mathbf F_E)$. Then there is a
finite stratification of $X$ such that on each stratum $S$,
pro-étale locally,

$$
K|_S\simeq \mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet
$$

for a bounded complex $P^\bullet$ of finite free $\mathcal O_E$-modules.
