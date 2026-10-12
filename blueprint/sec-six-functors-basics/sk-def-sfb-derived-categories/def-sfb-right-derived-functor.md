+++
id = "def-sfb-right-derived-functor"
kind = "definition"
title = "Right derived functor on the unbounded derived category"
order = 1554
uses = ["def-weil-abstract-derived-category"]
lean = ["CategoryTheory.Functor.rightDerivedFunctor"]
+++
Let $\mathcal C,\mathcal D$ be abelian categories, where $\mathcal C$ has K-injective
resolutions, and let $F\colon\mathcal C\to\mathcal D$ be an additive functor. The *right
derived functor* $RF\colon D(\mathcal C)\to D(\mathcal D)$ is the total right derived
functor of
$$
K(\mathcal C)\xrightarrow{\ F\ }K(\mathcal D)\xrightarrow{\ Q\ }D(\mathcal D)
$$
with respect to the quasi-isomorphisms. It comes with a unit
$Q\circ F\Rightarrow RF\circ Q$, which is an isomorphism on K-injective complexes. So
$RF(K)=F(I)$ for a K-injective resolution $K\to I$.
