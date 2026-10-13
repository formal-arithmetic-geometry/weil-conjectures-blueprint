+++
id = "thm-sfb-extend-scalars-localization"
kind = "theorem"
title = "Extension of scalars to $E$ is a localization on bounded constructible complexes"
order = 1650
uses = ["def-sfb-bounded-constructible-extend-scalars", "sk-def-sfb-rationalization", "sk-def-sfb-bounded-constructible"]
lean = ["AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars"]
+++
Let $X$ be a scheme whose underlying topological space is Noetherian. Then the functor
$E\otimes^{\mathrm L}_{\cO_E}-\colon D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)\to
D_{\mathrm{cons}}(X_{\mathrm{proét}},E)$ of [def-sfb-bounded-constructible-extend-scalars]
is a localization functor with respect to the class $W_{\ell^{\mathbf N}}$
[sk-def-sfb-rationalization]. This is the class of morphisms of the triangulated
$\mathbf Z$-linear category $D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)$
[sk-def-sfb-bounded-constructible] whose mapping cone is killed by some power $\ell^n$.
