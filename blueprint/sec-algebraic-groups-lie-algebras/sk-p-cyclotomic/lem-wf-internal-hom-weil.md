+++
id = "lem-wf-internal-hom-weil"
kind = "lemma"
title = "Internal Hom of Weil complexes"
lean = ["AlgebraicGeometry.Etale.WeilComplex.internalHom"]
order = 2915
uses = ["def-wf-internal-hom", "def-weil-weil-sheaf-complex", "lem-wf-tensor-weil"]
+++
Let $\Lambda\in\{E,\Qlb\}$. The construction of [def-wf-internal-hom] defines a
bifunctor on Weil complexes with underlying complexes in $\Dbc(X,\Lambda)$,

$$
R\mathcal Hom_{\Lambda_X}(-,-):\ (K,\varphi_K),(L,\varphi_L)\longmapsto
\bigl(R\mathcal Hom_{\Lambda_X}(K,L),\varphi_{\mathcal Hom}\bigr),
$$

contravariant in the first and covariant in the second variable, lying over the exact
bifunctor $R\mathcal Hom$ on $\Dbc(X,\Lambda)$; the displayed composite
$\varphi_{\mathcal Hom}$ is an isomorphism for every pair of Weil complexes.
