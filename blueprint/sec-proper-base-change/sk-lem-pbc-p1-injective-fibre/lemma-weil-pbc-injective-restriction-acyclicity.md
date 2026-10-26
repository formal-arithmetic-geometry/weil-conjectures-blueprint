+++
id = "lemma-weil-pbc-injective-restriction-acyclicity"
kind = "lemma"
title = "Injective restriction acyclicity bound"
lean = ["AlgebraicGeometry.Etale.subsingleton_H_upperStar_of_injective_of_iSup_eq_top"]
order = 1561
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-gabber-affine-comparison", "def-weil-pbc-torsion-etale-sheaf"]
+++
Let $(A,J)$ be a henselian pair [def-weil-pbc-henselian-terminology], let
$Y\to\operatorname{Spec}A$ be separated and locally of finite type, and let
$Y_0=Y\times_{\operatorname{Spec}A}\operatorname{Spec}(A/J)$. Suppose that $Y$ is
covered by $n+1$ affine opens. Let $\Lambda$ be a commutative ring and let $I$ be
an injective object of the category of sheaves of $\Lambda$-modules on $Y_{\Et}$
which is torsion [def-weil-pbc-torsion-etale-sheaf] (for instance an injective
sheaf of $\mathbf F_r$-modules). Then

$$
 H^q(Y_0,I|_{Y_0})=0\qquad(q>n).
$$
