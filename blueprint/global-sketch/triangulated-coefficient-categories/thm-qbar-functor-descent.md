+++
id = "thm-qbar-functor-descent"
kind = "theorem"
title = "Descent of compatible exact functors"
order = 24
uses = ["def-qbar-ambient-derived-category", "def-qbar-ambient-finext-diagram", "def-qbar-coefficient-category", "def-qbar-finext-diagram", "def-weil-finite-coefficient-datum", "thm-qbar-two-colimit-model"]
+++
Fix schemes $X,Y$, a prime $\ell\neq p$, and an algebraic closure
$\Qlb/\Ql$. For each of $X,Y$, choose either its ambient diagram
$\mathcal A_E$ or its constructible diagram $\mathcal C_E$, and denote
the chosen diagrams by $\mathcal B_E^X,\mathcal B_E^Y$. Suppose exact
functors $\Phi_E:\mathcal B_E^X\to\mathcal B_E^Y$ are
equipped, for every $E\subset L$, with exact natural isomorphisms

$$
T^Y_{L/E}\Phi_E\xrightarrow{\sim}\Phi_LT^X_{L/E}
$$

satisfying the unit, tower, and shift equations. Then they induce an exact
functor on the corresponding common-stage categories. The same statement
holds for exact functors of finitely many variables. Compatible natural transformations,
adjunction units and counits, base-change maps, projection maps, purity maps,
and duality maps descend by the same common-stage construction. If ambient
functors carry the constructible subdiagrams into the
constructible subdiagrams, the descended functor restricts to
$D^b_c(-,\Qlb)$. For $Rf^!$, the coefficient comparison is the mate of the comparison for
$Rf_!$, and its tower coherence is part of the hypotheses.
Lecture 42, Definition 8.1 and Theorem 8.2.
