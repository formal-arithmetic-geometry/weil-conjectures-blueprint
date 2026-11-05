+++
id = "lemma-integral-models--4"
kind = "lemma"
title = "Integral tensor product"
order = 294005
aliases = ["bp-r087-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_tensorObj"]
uses = ["lemma-integral-models--3", "definition-constructible-sheaves"]
+++
Use the notation $D^b_{\mathrm{fp}}$ of [lemma-integral-models--3]. Let
$\Lambda$ be a commutative condensed ring with the following properties
on every scheme $Z$ with Noetherian underlying space:

1. $D^b_{\mathrm{fp}}(Z,\Lambda)$ is a triangulated subcategory.
2. The derived tensor product of two bounded complexes with pro-étale
   locally finitely presented cohomology sheaves belongs to
   $D^b_{\mathrm{fp}}(Z,\Lambda)$.

Then, for every scheme $X$ with Noetherian underlying space, derived tensor
product preserves $D^b_{\mathrm{fp}}(X,\Lambda)$. These hypotheses hold
for $\Lambda=\mathcal O_E$, with $E\subset\overline{\mathbf Q}_\ell$ finite
over $\mathbf Q_\ell$. In particular, for Noetherian $X$,
$$
K,M\in\Dbc(X,\mathcal O_E)\quad\Longrightarrow\quad
K\otimes^{\mathbf L}_{\mathcal O_{E,X}}M\in\Dbc(X,\mathcal O_E).
$$
