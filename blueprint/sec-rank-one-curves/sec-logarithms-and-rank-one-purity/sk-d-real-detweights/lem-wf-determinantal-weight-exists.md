+++
id = "lem-wf-determinantal-weight-exists"
kind = "lemma"
title = "Purity of the determinant line"
lean = ["AlgebraicGeometry.WeilGroup.existsUnique_isPunctuallyPure_detLine"]
order = 4030
uses = ["cor-wf-rank-one-punctual-purity-curve", "def-mg-determinant-line", "def-real-weil-representation-operations", "def-weil-local-frobenius-trace", "def-weil-punctual-weights", "def-wf-fundamental-representation", "thm-wf-rank-one-finite-geometric-image-curve"]
+++
Let $X_0$ be a normal geometrically connected curve over $k_0$, let
$\iota:\Qlb\hookrightarrow\mathbf C$ be a field embedding, and let $\mathcal V$ be an
irreducible lisse Weil sheaf of rank $r$ on $X_0$. Then there is
exactly one real number $a$ such that the
determinant line
$\det(\mathcal V)$ is
punctually $\iota$-pure of weight
$a$.
