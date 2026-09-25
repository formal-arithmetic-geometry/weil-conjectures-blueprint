+++
id = "lem-sf-hom-comparison-local-morphism"
kind = "lemma"
title = "Locality of Hom comparison with a site-perfect first variable"
order = 2307
uses = ["def-weil-site-perfect-complex", "lem-sf-hom-finite-projective", "thm-sf-hom-comparison-constructible"]
+++
Let $u:X'\to X$ be a scheme morphism, compatible with the site
comparisons, and let $K$ be site-perfect and $M$ bounded constructible
on $X_{\Et}$. Pullback of the internal-Hom comparison for $(K,M)$
is the comparison for $(u^*K,u^*M)$, and both are isomorphisms.

## Proof

Use a bounded finite projective model $P$ from
[def-weil-site-perfect-complex]. The expression
$P^\vee\otimes_A^LM$ of [lem-sf-hom-finite-projective] commutes
with every monoidal pullback. The identifications arise from evaluation
and thus identify the canonical maps.
