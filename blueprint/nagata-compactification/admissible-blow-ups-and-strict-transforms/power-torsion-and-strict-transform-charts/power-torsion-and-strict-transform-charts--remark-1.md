+++
id = "power-torsion-and-strict-transform-charts--remark-1"
kind = "remark"
title = "Formalization route: the flattening chain is *not* the route to Tag 081S"
order = 361
+++
The module-flattening route below
([lemma-nagata-finite-data-flattening-package],
[thm-nagata-module-flattening-by-blowup],
[lemma-nagata-flattening-after-cartier-boundary],
[lemma-nagata-flattening-ideal-exists],
[lemma-nagata-dense-open-dimension-package]; Stacks Tags
0815/081R/081P/081L) is the Stacks Project's proof of
[lemma-nagata-elimination-indeterminacy] (Tag 081S), but it is
*not* the formalized route. The reason is that the chain bottoms out
in the dévissage sections of Stacks §§38.4–38.10, which exist neither
in Mathlib nor in this blueprint.

Tag 081S is instead formalized along Conrad's Theorem 2.4 and Zariski's Main
Theorem: see the chapter ``Elimination of indeterminacy after Deligne and
Conrad'', whose main results are
[thm-nagata-conrad-elimination] and
[cor-nagata-conrad-proper-target-extension], and the route remark that
closes it. Both external inputs are available: Zariski's Main Theorem is in
Mathlib (`Mathlib/AlgebraicGeometry/ZariskisMainTheorem.lean`), and
Stacks Tag 04II is already formalized here as
`AlgebraicGeometry.exists_immersion_affineSpace_of_quasiAffine`
([lemma-nagata-quasi-affine-immersion-affine-space-exists]). The
affine algebraic layer of
[lemma-nagata-module-strict-transform-exact] is nonetheless formalized
(`Submodule.powTorsion` and `Submodule.torsion'QuotientMap` in
`WeilConjectures/Mathlib/Algebra/Module/Torsion.lean`); the rest of
the flattening chain is not.

What is unchanged is the route to the two-open compactification theorem
([thm-nagata-two-open]): it does not go through flattening either way,
but uses the separation blow-up of
[lemma-nagata-separate-closed-subschemes]
(Tag 0F3V), common modifications, and the dense-source valuative criterion
([lemma-nagata-dense-source-valuative]).
