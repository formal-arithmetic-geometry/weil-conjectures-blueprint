+++
kind  = "proof"
of    = "prop-weil-pbc-composition-stability"
uses = ["def-weil-pbc-derived-exchange", "lem-weil-pbc-direct-image-preserves-injectives", "lemma-weil-pbc-property-iff-acyclicity"]
+++
(1) Since $\Lambda$ is torsion, every complex of sheaves of $\Lambda$-modules has
torsion cohomology sheaves, so torsion base change over $\Lambda$ says that the
derived exchange morphism [def-weil-pbc-derived-exchange] is an isomorphism on
all of $\Dplus$. Given a cartesian square for $hf$ along $c:Z'\to Z$, form the
base changes $Y'=Y\times_ZZ'$ and $X'=X\times_YY'$; the square for $hf$ is the
vertical pasting of the square for $f$ along $b:Y'\to Y$ and the square for $h$
along $c$. The exchange morphism of the pasted square is the composite of
$c^{-1}$-whiskered and $Rh'_*$-whiskered exchange morphisms of the two squares,
up to the composition isomorphisms of inverse images and of derived direct
images (the latter exist because direct images preserve injectives,
[lem-weil-pbc-direct-image-preserves-injectives]); both are isomorphisms, hence
so is their composite.

(2) For proper morphisms, injective acyclicity over $\Lambda$ is equivalent to
torsion base change over $\Lambda$
([lemma-weil-pbc-property-iff-acyclicity]); $hf$ is proper, so (2) follows from
(1). This is Stacks Project, Tag 0A4D.
