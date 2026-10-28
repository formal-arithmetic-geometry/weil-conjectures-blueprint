+++
id = "sbc-lem-strict-henselian-constant-cohomology"
kind = "lemma"
title = "Constant-sheaf cohomology of a strictly henselian local scheme"
lean = ["AlgebraicGeometry.Scheme.exists_section_of_etale_of_isStrictlyHenselianLocalRing", "AlgebraicGeometry.Scheme.subsingleton_H_of_isStrictlyHenselianLocalRing", "AlgebraicGeometry.Scheme.hZeroConstantSheafAddEquiv"]
order = 2220
uses = ["def-weil-pbc-etale-cohomology"]
+++
Let $(R,\mathfrak m)$ be a strictly henselian local ring, let
$X=\operatorname{Spec}R$, and let $A$ be a finite constant sheaf of
order invertible in $R$. Then

$$
H^q(X_{\Et},A)=\begin{cases}A,&q=0,\\0,&q>0,\end{cases}
$$

for the etale cohomology of [def-weil-pbc-etale-cohomology].
