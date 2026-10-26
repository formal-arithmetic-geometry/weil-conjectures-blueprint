+++
id = "def-pc-derived-pullback"
kind = "definition"
title = "Derived pullback of modules on schemes"
lean = ["AlgebraicGeometry.Scheme.Modules.derivedPullback"]
order = 725
uses = ["def-pc-derived-category", "def-pc-scheme"]
+++
For a morphism $g:T\to S$ of schemes,
let $Lg^*:D(\mathcal O_S)\to D(\mathcal O_T)$ be the (total) left derived
functor of the pullback functor $g^*:\mathrm{Mod}(\mathcal O_S)\to\mathrm{Mod}(\mathcal O_T)$,
$g^*\mathcal E=\mathcal O_T\otimes_{g^{-1}\mathcal O_S}g^{-1}\mathcal E$, applied
termwise to complexes; it comes with a natural transformation
$Lg^*E\to g^*E$ for complexes $E$ of $\mathcal O_S$-modules.
