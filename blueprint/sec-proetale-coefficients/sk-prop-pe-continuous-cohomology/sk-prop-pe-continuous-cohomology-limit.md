+++
id = "det-pe-continuous-cohomology-limit"
kind = "lemma"
title = "Sections of a limit with epimorphic transitions"
lean = ["AlgebraicGeometry.ProEtale.isHomotopyLimit_mapCone_Q_of_epi", "CategoryTheory.Pretriangulated.IsHomotopyLimit.map"]
order = 1053
uses = ["det-pe-replete-epimorphism", "det-pe-milnor-epimorphic"]
+++
Let $X$ be a scheme and $(F_n)_{n\geq1}$ an inverse system of abelian sheaves on
$X_{\Proet}$ with epimorphic transition maps, and $F=\varprojlim_nF_n$. Then the
canonical map $F\to R\varprojlim_nF_n$ is an isomorphism in $D(X_{\Proet})$, and
for every object $W$ of $X_{\Proet}$

$$
R\Gamma(W,F)\simeq R\varprojlim_nR\Gamma(W,F_n)
$$

in $D(\mathbf Z)$; here $R\varprojlim$ of a sequence $(K_n)$ is the fibre of
$1-\text{shift}\colon\prod_nK_n\to\prod_nK_n$.
