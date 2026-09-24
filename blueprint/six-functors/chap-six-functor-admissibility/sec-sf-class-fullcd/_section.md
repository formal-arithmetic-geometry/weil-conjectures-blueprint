+++
id = "sec-sf-class-fullcd"
kind = "section"
title = "The class-restricted datum, and the existence half of the ambient adjoint"
order = 3495
uses = ["def-amb-etale-compact-support", "def-compact-support-direct-image-detailed", "def-sf-fullcd-used-class", "def-trf-admissibility", "def-weil-ambient-exceptional-adjoint", "def-weil-compactifications-refinements", "def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-full-cohomological-dimension", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-etale-sheaves", "def-weil-pbc-extension-by-zero", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-amb-etale-compact-comparisons", "lem-cbc-proetale-extension-zero-comparison", "lem-sf-proetale-constructible-origin", "lem-weil-pbc-comparison-pullback", "prop-sf-comparison-bound-zero", "prop-weil-pbc-comparison-direct-image", "thm-amb-etale-exceptional-adjoint", "thm-sf-fullcd-etale-origin", "thm-sf-fullcd-used-class", "thm-sp-grothendieck", "thm-weil-pbc-site-comparison"]
+++
The full cohomological-dimension condition
def:weil-full-cohomological-dimension quantifies over *all*
sheaves of $A$-modules, and in that form it is *false*
([prop-sf-fullcd-general-form-false],
[rem-sf-fullcd-counterexample]). The condition the blueprint actually
consumes is the same two vanishing clauses with the quantifier restricted to
the coefficient class [def-sf-fullcd-used-class], and the existence
half of the ambient exceptional right adjoint is the residue that
[open-sf-ambient-adjoint-input] records for
prop:ambient-exceptional-adjoint. The six items below introduce the
restricted datum, record that [thm-sf-fullcd-used-class] supplies it
with the bound $2\dim\overline X$, and discharge the existence half on
that class. They are collected in a final section so that no statement,
proof, label or number of the preceding sections is moved, and the
unrestricted definition def:weil-full-cohomological-dimension keeps
its quantifiers verbatim: it is *not* restated, weakened or replaced
here, and the restricted datum is a separate definition beside it.
