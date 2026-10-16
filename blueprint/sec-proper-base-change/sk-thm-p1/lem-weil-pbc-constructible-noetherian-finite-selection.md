+++
id = "lem-weil-pbc-constructible-noetherian-finite-selection"
kind = "lemma"
title = "Noetherian finite selection of stalk tests"
lean = ["AlgebraicGeometry.Etale.exists_finset_mono_pi_lift"]
order = 1185
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "lem-weil-pbc-irreducible-lisse-strata", "lem-weil-pbc-lisse-generic-kernel", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $X$ be Noetherian, let $F$ be a constructible abelian etale sheaf, and let
$(\phi_\lambda:F\to G_\lambda)_{\lambda\in L}$ be a family of maps to
arbitrary abelian etale sheaves. Assume that for every geometric point $\bar
x$ and every $0\neq v\in F_{\bar x}$, some $\lambda$ satisfies
$(\phi_\lambda)_{\bar x}(v)\neq0$. Then a finite subset $L_0\subset L$ makes

$$
 (\phi_\lambda)_{\lambda\in L_0}:
 F\longrightarrow\bigoplus_{\lambda\in L_0}G_\lambda
$$

a monomorphism. In particular, the conclusion holds if at each geometric point
some single $\phi_\lambda$ is injective.
