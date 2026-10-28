+++
id = "lem-weil-pbc-constant-pullback-identity-coherence"
kind = "lemma"
title = "ConstantPullbackIdentityCoherence"
uses = ["def-constructible-constant", "def-pc-scheme", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.constantPullbackIdentityCoherence"]
order = 1953
+++
Let $Z$ be a scheme [def-pc-scheme] and $M$ an abelian group, with constant sheaf $M_Z$ [def-constructible-constant]. Let $c:M_Z\xrightarrow{\sim}\mathrm{id}_Z^{-1}M_Z$ be the inverse constant-sheaf comparison, defined by uniqueness of left adjoints to global sections using the inverse-image adjunction [def-weil-pbc-inverse-image] and the identification of sections of direct image [def-weil-pbc-direct-image]. Let $a:\mathrm{id}_Z^{-1}\xrightarrow{\sim}\mathrm{id}$ be the identity comparison of [lem-weil-pbc-inverse-image-composition]. Then
$$a_{M_Z}\circ c=\mathrm{id}_{M_Z}.$$
This is an equality of sheaf morphisms, with no cohomology degree or Ext class quantified.
