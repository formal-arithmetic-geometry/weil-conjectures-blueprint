+++
id = "lemma-flat-models-generators"
kind = "lemma"
title = "Flat models and generators"
order = 255
lean = ["AlgebraicGeometry.Etale.constructibleFiniteTor_eq_triangEnvelope_ctfGenerators_of_isNoetherian", "AlgebraicGeometry.Etale.hasTorAmplitudeIn_iff_exists_flatModel", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_iff_exists_flatModel"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image"]
+++
Every $C\in D^b_{\mathrm{ctf}}(X,A)$ on $X_{\mathrm{pro}\acute{e}t}$ is represented by a bounded complex of
flat constructible $A$-sheaves. A flat constructible sheaf has a finite
stratification on whose strata it is locally of the form $\underline M$ with
$M$ a finite projective $A$-module. Consequently, $D^b_{\mathrm{ctf}}(X,A)$ is generated,
using
shifts, finite extensions and direct summands, by sheaves $a_!L$, where
$a:S\hookrightarrow X$ is locally closed and $L$ is locally of the form
$\underline M$ with $M$ a finite projective $A$-module.
