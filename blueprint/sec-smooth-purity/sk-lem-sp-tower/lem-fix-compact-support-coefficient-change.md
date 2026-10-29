+++
id = "lem-fix-compact-support-coefficient-change"
kind = "lemma"
title = "Change of finite coefficients for compact support"
lean = ["AlgebraicGeometry.Etale.exists_isCoefficientChange_compactlySupportedGlobalSections", "AlgebraicGeometry.Etale.isCoefficientChange_compactlySupportedGlobalSectionsRestrictScalarsIso"]
order = 2977
uses = ["def-compact-support-direct-image-detailed", "def-exchange-projection", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-scheme-morphism-properties", "lemma-weil-pbc-geometric-stalk-conservative", "thm-cbc-finite-level-proetale", "thm-cbc-finite-torsion", "thm-sc-finite-type-torsion-cd"]
+++
Let $f:X\to Y$ be a
separated finite-type
morphism in the finite-field datum.
Put $A=A_{E,n}$, $B=A_{E,m}$, where $1\leq m\leq n$.
For a bounded constructible complex $K$ of
finite Tor amplitude, the
canonical coefficient comparison is an isomorphism

$$
(Rf_!K)\otimes_A^L B\ \xrightarrow{\sim}\
Rf_!(K\otimes_A^L B).
$$

Here the right side uses $B$-coefficients and
compact support; the map
comes from the tensor
comparison. It is compatible with successive reductions, pullback,
and the counits defining the projection transformation.
