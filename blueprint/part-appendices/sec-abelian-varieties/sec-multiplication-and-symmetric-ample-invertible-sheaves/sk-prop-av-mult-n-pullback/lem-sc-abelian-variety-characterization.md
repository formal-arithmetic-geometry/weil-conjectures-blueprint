+++
id = "lem-sc-abelian-variety-characterization"
kind = "lemma"
title = "Abelian varieties are the complete group varieties"
lean = ["AlgebraicGeometry.IsAbelianVariety.geometricallyIntegral", "AlgebraicGeometry.IsAbelianVariety.irreducibleSpace"]
order = 489
uses = ["def-sc-abelian-variety", "def-sc-group-scheme"]
+++
Let $k$ be a field and $A$ a
group scheme over $k$ which is
proper, connected and smooth over $k$ (a *complete group
variety*). Then $A$ is irreducible and geometrically integral.
Consequently an *abelian variety* in the sense of
[def-sc-abelian-variety] is exactly a complete group variety.

The smoothness hypothesis cannot be dropped: for
$\operatorname{char}k=p>0$ the finite group schemes

$$
\alpha_p=\Spec k[x]/(x^p),\qquad
\mu_p=\Spec k[x]/(x^p-1)
$$

are proper and connected but not reduced, hence not smooth, over $k$.
