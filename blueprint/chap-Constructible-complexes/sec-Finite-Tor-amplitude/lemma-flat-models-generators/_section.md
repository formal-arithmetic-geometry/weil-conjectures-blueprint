+++
id = "lemma-flat-models-generators"
kind = "lemma"
title = "Flat models and generators"
order = 255
lean = ["AlgebraicGeometry.Etale.constructibleFiniteTor_eq_triangEnvelope_ctfGenerators_of_isNoetherian", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_iff_exists_flatModel"]
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves"]
+++
Every $C\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}$ on [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) is represented by a bounded complex of
flat [constructible](@definition-constructible-sheaves) $A$-sheaves. A flat [constructible sheaf](@definition-constructible-sheaves) has a finite
stratification on whose strata it is locally of the form $\underline M$ with
$M$ a finite projective $A$-module. Consequently, [$D^b_{\mathrm{ctf}}(X,A)$](@definition-constructible-sheaves) is generated,
using
shifts, finite extensions and direct summands, by sheaves $a_!L$, where
$a:S\hookrightarrow X$ is locally closed and $L$ is locally of the form
$\underline M$ with $M$ a finite projective $A$-module.
