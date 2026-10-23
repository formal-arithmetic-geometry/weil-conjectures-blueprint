+++
id = "lem-pd-picard-base-change"
kind = "lemma"
title = "The Picard functor is compatible with base change"
lean = ["AlgebraicGeometry.picardFunctorIsoOfIsPullback", "AlgebraicGeometry.picardFunctorIsoOfIsPullback_hom_app_toPicardFunctor", "AlgebraicGeometry.nonempty_picardFunctor_iso_of_isPullback"]
order = 882
uses = ["def-pc-base-change", "def-pc-fppf-site", "def-pc-picard-functor", "def-pc-picard-presheaf"]
+++
Let $f:X\to S$ be a morphism of schemes and let $g:S'\to S$ be a morphism,
with base change $f':X_{S'}\to S'$ of $f$ along
$g$. Then the restriction of the
Picard functor
$\operatorname{Pic}_{X/S}$ to the slice site
$(\mathit{Sch}/S')_{fppf}\subseteq(\mathit{Sch}/S)_{fppf}$ of
[def-pc-fppf-site] is the Picard functor
$\operatorname{Pic}_{X_{S'}/S'}$.
