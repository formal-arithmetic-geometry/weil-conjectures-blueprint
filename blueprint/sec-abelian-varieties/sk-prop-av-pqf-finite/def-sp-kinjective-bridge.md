+++
id = "def-sp-kinjective-bridge"
kind = "definition"
title = "The K-injective bridge"
lean = ["CochainComplex.KInjectiveResolution.homologyRightDerivedFunctorPlusObjIso", "CochainComplex.KInjectiveResolution.rightDerivedFunctorObjIso", "CochainComplex.KInjectiveResolution.homologyRightDerivedFunctorObjIso", "CochainComplex.KInjectiveResolution", "CochainComplex.KInjectiveResolution.rightDerived", "CochainComplex.KInjectiveResolution.rightDerivedHomology", "CochainComplex.KInjectiveResolution.exists_of_isStrictlyGE", "CochainComplex.KInjectiveResolution.nonempty_of_isGE"]
order = 523
uses = ["def-sp-grothendieck-abelian", "def-sp-left-exact-additive"]
+++
A *K-injective resolution* of a complex $K$ is a quasi-isomorphism $K\to I$
with $I$ K-injective: for every acyclic complex $A$ the complex
$\operatorname{Hom}(A,I)$ is acyclic. In a Grothendieck abelian category
[def-sp-grothendieck-abelian] every bounded-below complex admits a
K-injective resolution.

This carries a left exact additive functor [def-sp-left-exact-additive] from
objects to complexes. For $v:\mathcal A\to\mathcal B$ left exact additive and
$K\in\operatorname{Ch}^+(\mathcal A)$, choose a K-injective resolution $K\to
I$ and set

$$
 RvK:=v(I),\qquad R^pv(K):=\mathcal H^p(RvK),
$$

a priori depending on the chosen resolution.

Up to canonical isomorphism, $RvK$ does not depend on the choice of the
K-injective resolution, and for an object $X$ placed in degree zero
$R^pv(X)$ agrees with the right derived functor defined by injective
resolutions in [def-sp-left-exact-additive]; this is proved in the lemma
that K-injective resolutions compute $Rv$.
