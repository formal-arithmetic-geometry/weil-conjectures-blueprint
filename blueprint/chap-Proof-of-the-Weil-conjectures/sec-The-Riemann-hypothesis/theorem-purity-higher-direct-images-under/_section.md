+++
id = "theorem-purity-higher-direct-images-under"
kind = "theorem"
title = "Purity of higher direct images under a smooth proper morphism"
order = 1369
lean = ["AlgebraicGeometry.WeilSheaf.smooth_proper_relative_purity", "AlgebraicGeometry.WeilComplex.derivedLowerShriekObjIsoDerivedLowerStarOfIsProper"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $f_0:X_0\to Y_0$ be smooth proper of pure relative dimension $d$,
and let $F$ be a lisse Weil sheaf, punctually $\iota$-pure of weight
$w$. For every $i$, the canonical identification

$$
R^if_{0!}F=R^if_{0*}F
$$

is Weil-equivariant, and this constructible sheaf is punctually
$\iota$-pure of weight $w+i$. In particular, it is mixed of the
single weight $w+i$.
