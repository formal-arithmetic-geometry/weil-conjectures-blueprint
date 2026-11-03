+++
id = "sk-prop-input-torsors"
kind = "proposition"
title = "Torsors and étale $H^1$"
order = 2197
uses = ["sk-def-smooth"]
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor", "AlgebraicGeometry.Scheme.EtaleTorsor.exists_quotientEquivSheafH"]
+++
Let $Y$ be a scheme and $M$ a finite abelian group. Then there is a
canonical bijection, natural in $(Y,M)$,

$$
\mathrm{Tor}^1(Y,M)\xrightarrow{\ \sim\ }H^1(Y_{\Et},\underline M)
$$

between the isomorphism classes of $M$-torsors on $Y_{\Et}$ and
$H^1(Y_{\Et},\underline M)$, and an $M$-torsor is the same thing as a
finite étale surjective $Y$-scheme with a simply transitive
$M$-action. Under this bijection the class of a torsor vanishes exactly
when its structure morphism admits a section. For
$M=\Z/d\Z$ and $Y$ connected with geometric point $\bar y$, the
torsor attached to a class is connected — that is, a Galois cover
with group $\Z/d\Z$ — exactly when the corresponding continuous homomorphism
$\pi_1(Y,\bar y)\to\Z/d\Z$ is surjective.
