+++
id = "lem-pc-flat-complex-derived-pullback"
kind = "lemma"
title = "Termwise derived pullback of a bounded above flat complex"
lean = ["AlgebraicGeometry.Scheme.Modules.isIso_derivedPullbackCounit_app", "AlgebraicGeometry.Scheme.Modules.derivedPullbackObjIsoOfFlat"]
order = 766
uses = ["def-pc-derived-pullback", "def-pc-scheme"]
+++
Let $g:T\to S$ be a morphism of schemes and let $E$ be a bounded above
complex of flat $\mathcal{O}_S$-modules. Then the derived pullback
$Lg^*E$ of [def-pc-derived-pullback] is represented by the complex
$g^*E$ obtained by pulling $E$ back term by term: the canonical map
$Lg^*E\to g^*E$ is an isomorphism in $D(\mathcal O_T)$.
