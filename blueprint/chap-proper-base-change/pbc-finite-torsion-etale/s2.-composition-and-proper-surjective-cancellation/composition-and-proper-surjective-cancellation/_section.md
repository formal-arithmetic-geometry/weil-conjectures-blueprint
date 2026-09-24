+++
id = "composition-and-proper-surjective-cancellation"
kind = "section"
title = "Composition and proper-surjective cancellation"
order = 1663
uses = ["def-sp-composite-acyclicity", "def-sp-etale-dictionary", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-injective-acyclicity", "def-weil-pbc-inverse-image", "def-weil-pbc-property-detailed", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-geometric-stalk-conservative", "lem-weil-pbc-underived-proper-exchange", "prop-weil-pbc-property-iff-acyclicity", "thm-sp-grothendieck", "thm-sp-grothendieck-base-change"]
+++
The two closure properties that turn the projective-line case into the general
one. Both are proved through the injective acyclicity predicate
$\mathrm{IA}$ rather than through the exchange morphism directly: the
Grothendieck spectral sequence of a composite
[lem-weil-pbc-grothendieck-spectral-sequence] gives stability under
composition [prop-weil-pbc-composition-stability], and a retract supplied by a
proper surjection [lem-weil-pbc-retract-supplied] gives cancellation
[prop-weil-pbc-cancellation].
