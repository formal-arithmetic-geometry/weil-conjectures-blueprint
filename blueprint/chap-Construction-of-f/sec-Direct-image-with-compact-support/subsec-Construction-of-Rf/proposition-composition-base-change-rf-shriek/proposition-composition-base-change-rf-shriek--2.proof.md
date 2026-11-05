+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--2"
order = 516003
uses = ["proposition-construction-independence-rf-shriek", "theorem-nagata-s-compactification-theorem"]
+++
Choose compactifications of $f$, $g$ and $h$, then compactify the two
adjacent proper-open composites and the middle proper-open composite. These
form the two compatible diagrams of compactifications for the bracketings
$(hg)f$ and $h(gf)$. Rewrite each $C$ using its expression through a triangle
of compactifications. The identity
`CategoryTheory.ExchangeFormalism.compIso_assoc` equates the two composites
of exchange maps on these diagrams. The compactification comparisons and
their cocycle condition in [proposition-construction-independence-rf-shriek]
transport this equality to the chosen functors. This is the argument of
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_assoc'`.
