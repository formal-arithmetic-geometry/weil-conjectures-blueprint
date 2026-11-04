+++
kind = "proof"
of = "lemma-change-coefficients-compact-support"
order = 632
uses = ["definition-change-of-coefficients-maps", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
The map is the composite of the isomorphism of
Lemma [lemma-change-coefficients-direct-image] for $p$, applied to
$j_!K\in D^b_{\mathrm{ctf}}$ (Proposition [proposition-proper-direct-image-extension-zero]),
and of $Rp_*$ of the isomorphism of
Definition [definition-change-of-coefficients-maps](2). For independence,
let $h:Z'\to Z$ be a refinement of compactifications. Both comparison
maps (4) and (2) commute with the refinement map
(5.7). Indeed, they are formed from
identifications of pullbacks and adjunction maps. A map out of an
extension by zero is determined by its restriction to the open subscheme,
and there all maps involved are identities. We also use that (4) is
compatible with composition of morphisms. Under $R(ph)_*\simeq Rp_*Rh_*$,
the map (4) for $ph$ is $Rp_*$ of (4) for $h$ followed by (4) for $p$,
since transposes of composites are composites. As in the proof of
Proposition [proposition-construction-independence-rf-shriek], this
gives independence for any two compactifications.
