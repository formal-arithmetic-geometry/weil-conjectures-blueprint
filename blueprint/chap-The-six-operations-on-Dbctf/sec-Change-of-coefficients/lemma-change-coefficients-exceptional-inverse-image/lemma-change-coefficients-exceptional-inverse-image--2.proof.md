+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--2"
order = 640005
uses = ["lemma-change-coefficients-compact-support", "lemma-change-coefficients-direct-image", "lemma-reduction-derived-nakayama", "proposition-comparison-etale-derived-category", "proposition-composition-open-restriction-compactifications-f", "theorem-nagata-s-compactification-theorem"]
+++
Choose a compactification $f=p\circ j$, with $j$ an open immersion and
$p$ proper. For $j$, the comparison for $j^!$ is the comparison for $j^*$;
the transpose of the chosen comparison for $j_!$ is exactly this
isomorphism.

For $p$, use the triangle for multiplication by $\ell^n$. The pullback
comparison is compatible with its unit and boundary maps. Transposing
first under $p^*\dashv Rp_*$ and then under $Rp_*\dashv p^!$ gives an
invertible comparison for reduction on bounded constructible condensed
complexes. This is
`isIso_mateEquiv_boundedConstructibleLowerStarIntegersModPowReduction`.
Compose it with the finite-coefficient comparison that reads $p^!$ on the
étale site; the mate of this composite is the composite of the mates.
Thus `isIso_mateEquiv_etaleReductionLowerShriekIso` gives the required
isomorphism for $p$.

Finally, the composition isomorphisms for $Rf_!$ identify its comparison
with the composite of those for $j$ and $p$. Transposing gives the
composite of the two invertible exceptional comparisons, by
`isIso_mateEquiv_etaleReductionLowerShriekIsoOfCompactification`.
This is the canonical isomorphism in the statement.
