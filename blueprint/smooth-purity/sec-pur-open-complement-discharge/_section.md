+++
id = "sec-pur-open-complement-discharge"
kind = "section"
title = "The open-complement condition is unconditional"
order = 3654
uses = ["cor-exc-base-change-open-immersion-general", "cor-pur-general-admissibility-datum", "cor-sf-ambient-adjoint-discharge", "def-exc-direct-image-input", "def-exc-open-complement-bound", "def-pur-conventions", "def-sbc-affine-space", "def-sf-fullcd-used-class", "def-weil-constructible-intervals", "def-weil-exceptional-adjoint-admissibility", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "def-weil-scheme-morphism-properties", "lem-exc-open-complement-known", "lem-kun-cd-sep-closed-point", "lem-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-strict-henselization-stalk-formula-detailed", "thm-dg-finite-type-constructibility", "thm-exc-curve-open-constructible-general", "thm-exc-curve-open-dimension-general", "thm-exc-direct-image-input-holds", "thm-pur-general-admissibility", "thm-sc-finite-type-torsion-cd"]
+++
The single hypothesis that [thm-pur-general-admissibility] displays is the
open-complement condition of [def-exc-open-complement-bound] for the
finitely many chart complements, and that condition is a theorem of this
blueprint in complete generality:
[lem-exc-open-complement-known] derives both of its clauses — the
vanishing $R^qj_*M=0$, $q>2d$, for *every* sheaf $M$ of
$A$-modules, and the constructibility of the higher direct images of
constructible sheaves — from the two clauses of the direct-image finiteness
input [def-exc-direct-image-input], which hold over every separably
closed field by [thm-exc-direct-image-input-holds], with the constant
$2d$ depending only on the dimension of the ambient finite-type scheme.
Neither curves, nor lisse coefficients, nor constant towers, nor smooth
morphisms are needed, and no case of the condition is left open. The two
statements below record what the assembly and the admissibility definitions of
the manuscript consume: the condition holds with the *same* constant at
every finite coefficient stage, and, with it, the assembly
[thm-pur-general-admissibility] and
[cor-pur-general-admissibility-datum] are theorems without hypotheses.
