+++
id = "det-prop-sfb-module-pullback-exact-lifted"
kind = "lemma"
title = "Transport of module objects along an exact functor is exact"
lean = ["CategoryTheory.Functor.preservesFiniteLimits_mapMod", "CategoryTheory.Functor.preservesFiniteColimits_mapMod"]
order = 1201
uses = ["lem-sfb-modobj-abelian", "def-sfb-modobj-transport"]
+++
Let $\mathcal C$ and $\mathcal D$ be abelian monoidal categories whose tensor products are additive in
each variable, let $F\colon\mathcal C\to\mathcal D$ be a lax monoidal functor and let $\mathcal R$ be a
monoid object of $\mathcal C$ such that $\mathcal R\otimes-$ and $F(\mathcal R)\otimes-$ are right
exact, so that $\Mod_{\mathcal R}(\mathcal C)$ and $\Mod_{F(\mathcal R)}(\mathcal D)$ are abelian
([lem-sfb-modobj-abelian]). Let
$\operatorname{mapMod}(F)\colon\Mod_{\mathcal R}(\mathcal C)\to\Mod_{F(\mathcal R)}(\mathcal D)$ be the
transport of module objects along $F$ ([def-sfb-modobj-transport]). If $F$ preserves finite limits,
then so does $\operatorname{mapMod}(F)$; if $F$ preserves finite colimits, then so does
$\operatorname{mapMod}(F)$.
