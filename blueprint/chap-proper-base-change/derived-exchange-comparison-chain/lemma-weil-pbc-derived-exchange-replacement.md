+++
id = "lemma-weil-pbc-derived-exchange-replacement"
kind = "lemma"
title = "Derived exchange replacement independence"
order = 1431
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_ext", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_fac_app"]
uses = ["def-weil-pbc-derived-exchange", "lemma-weil-pbc-derived-exchange-source-comparison-v5", "lemma-weil-pbc-derived-exchange-target-comparison-exists-v5", "lemma-weil-pbc-derived-exchange-target-comparison-unique-v5", "lemma-weil-pbc-underived-exchange-naturality"]
+++
The K-injective replacement used in Definition
[def-weil-pbc-derived-exchange] gives a well-defined derived exchange
map, independent of all replacement choices.

## Proof

Given two K-injective replacements $J^\bullet$ and $J'^\bullet$, the identity
of $g'^{-1}I^\bullet$ lifts to maps $J^\bullet\to J'^\bullet$ and
$J'^\bullet\to J^\bullet$ because K-injective complexes are homotopically
injective. Their composites are homotopic to the identities by lifting the
homotopies of the replacement quasi-isomorphisms. Applying $f'_*$ preserves
chain homotopies. The two resulting maps from
$g^{-1}f_*I^\bullet$ therefore define the same morphism in the derived
category. A comparison of two injective resolutions of $K$ is handled by
the same lifting argument, and naturality of the underived exchange map
commutes with the comparison maps. Thus the class is canonical.
