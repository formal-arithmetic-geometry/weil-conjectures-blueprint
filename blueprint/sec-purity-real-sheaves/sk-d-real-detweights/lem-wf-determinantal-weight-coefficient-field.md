+++
id = "lem-wf-determinantal-weight-coefficient-field"
kind = "lemma"
title = "The determinant weight does not depend on the coefficient field"
lean = ["AlgebraicGeometry.WeilGroup.isPunctuallyPure_det_baseChange_iff"]
order = 3842
uses = ["def-mg-determinant-line", "def-real-weil-representation-operations", "def-weil-punctual-weights"]
+++
Let $X_0$ be a normal geometrically connected curve over $k_0$, fix
a field embedding $\iota:\Qlb\hookrightarrow\mathbf C$, and let $\mathcal V$ be an
irreducible lisse Weil sheaf of rank $r$ on $X_0$ whose
representation is defined over finite extensions
$E\subseteq E'$ of $\mathbf Q_\ell$. If
$\hyperref[def-real-weil-representation-operations]{\det(\mathcal V)}$, read with
coefficients in $E$, is
punctually $\iota$-pure of weight
$a$, then it is punctually $\iota$-pure of the same weight $a$ when
read with coefficients in $E'$.
