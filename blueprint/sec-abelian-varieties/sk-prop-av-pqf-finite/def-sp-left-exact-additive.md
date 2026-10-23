+++
id = "def-sp-left-exact-additive"
kind = "definition"
title = "Additive left exact functors and right derived functors"
order = 523
lean = ["CategoryTheory.Functor.Additive", "CategoryTheory.Functor.rightDerived", "CategoryTheory.InjectiveResolution.isoRightDerivedObj", "CategoryTheory.Functor.rightDerivedZeroIsoSelf"]
uses = ["def-sp-abelian", "def-sp-injective-resolutions"]
+++
Let $\mathcal A,\mathcal B$ be abelian categories [def-sp-abelian]. A functor
$v:\mathcal A\to\mathcal B$ is *additive* if it preserves finite products
(equivalently finite biproducts); it is *left exact* if it is additive and
preserves kernels. Suppose that $\mathcal A$ has enough injectives. For a
left exact additive functor $v$ and an object $X\in\mathcal A$, the *right
derived functors* $R^nv$ ($n\geq0$) are defined via injective resolutions
[def-sp-injective-resolutions]: for an injective resolution $X\to I^\bullet$,

$$
 R^nv(X):=\mathcal H^n(v(I^\bullet)).
$$

Up to canonical isomorphism, $R^nv(X)$ does not depend on the choice of the
injective resolution, and $R^0v=v$; this is the well-definedness lemma for
derived functors.
