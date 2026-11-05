+++
kind = "proof"
of = "lemma-kunneth-formula-compact-supports--3"
order = 1222003
uses = ["proposition-construction-independence-rf-shriek", "proposition-proper-direct-image-extension-zero", "proposition-proper-direct-image-constructible-complexes", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Write $a=r\circ j$ using the chosen compactification. Extension by
zero preserves bounded constructible complexes, so the proper
projection formula applies to $j_!A$ and $B$. The exceptional
projection map is the composite of this proper projection map with
the inverse of the extension-by-zero comparison

$$
j_!(A\otimes j^*N)\longrightarrow j_!A\otimes N,
$$

at $N=r^*B$, followed by $j^*r^*\simeq a^*$.
The two comparison maps are isomorphisms by
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_properProjectionMorphism_padicAlgCl`
and
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_openImmersionProjectionComparison`.
The fully faithful inclusion of bounded constructible complexes into
the derived category reflects isomorphisms, which proves the claim.
