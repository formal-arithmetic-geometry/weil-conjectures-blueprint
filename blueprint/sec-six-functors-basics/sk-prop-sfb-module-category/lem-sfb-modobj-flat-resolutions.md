+++
id = "lem-sfb-modobj-flat-resolutions"
kind = "lemma"
title = "Functorial flat resolutions of module objects"
order = 1579
uses = ["def-sfb-modobj-symmetric-tensor", "lem-sfb-modobj-abelian", "lem-sfb-modobj-forget-faithful", "lem-sfb-modobj-forget-left-exact", "lem-sfb-modobj-forget-right-exact"]
lean = ["CategoryTheory.Mod.hasFunctorialFlatResolution"]
+++
Let $\mathcal C$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive in each variable, and let $\mathcal R$ be a commutative monoid object.
In a monoidal abelian category, call an object $F$ *flat* if $F\otimes-$ and $-\otimes F$
are exact. A *functorial flat resolution* is a functor $P$ with flat values together with a
natural epimorphism $\pi_M\colon P(M)\to M$. Suppose $\mathcal C$ has a functorial flat
resolution. Then so does $\Mod_{\mathcal R}(\mathcal C)$, with the relative tensor product
of [def-sfb-modobj-symmetric-tensor]. It is given by the free modules
$\mathcal R\otimes P(M)$ and the maps
$$
\mathcal R\otimes P(M)\xrightarrow{\mathcal R\otimes\pi_M}\mathcal R\otimes M
\xrightarrow{\gamma_M}M .
$$
