+++
kind = "proof"
of = "sk-def-sfb-finite-pushforward-pullback"
+++
Identity covers, composites of covers, and base changes of covers satisfy
the axioms by [sk-lem-pe-weakly-etale-stability] and the fpqc covering
axioms. Representable presheaves satisfy descent for these covers by
fpqc descent for morphisms of schemes, so they are sheaves
([det-pe-topos-functoriality-site]). Finally,
$V\mapsto V\times_YX$ preserves finite limits and covering families,
so it defines the displayed geometric morphism, and the inverse
image is left exact by the construction of the site. Exactness on abelian
sheaves and compatibility with composition follow. This is the small-site
version of the constructions in Stacks, Tag 0988. For Grothendieck abelian coefficients, the
form proved in Lean, see [prop-pe-topos-functoriality-abelian].
