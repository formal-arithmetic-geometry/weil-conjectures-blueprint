+++
kind = "proof"
of = "theorem-classical-sheaves-essential-image--1"
order = 115002
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "proposition-pro-etale-affines-form-basis", "definition-classical-pro-etale-sheaves", "proposition-comparison-morphism-inverse-image"]
+++
Construct $\nu_X^*$ by left Kan extension followed by sheafification, as
in [proposition-comparison-morphism-inverse-image]. Maps from a cofiltered
limit of affine schemes to an étale $X$-scheme form the filtered colimit
of the maps from its stages, by local finite presentation. Thus the Kan
extension carries affine étale presentations to colimits. Finite covering
families on the affine pro-étale site descend to étale stages, and filtered
colimits in $A$ commute with finite limits. The Kan extension of an étale
sheaf is therefore already a sheaf on this affine subsite.

By [proposition-pro-etale-affines-form-basis], sheafification does not
change these affine sections. On affine étale objects the Kan-extension
unit is invertible, since the inclusion of sites is fully faithful.
The comparison unit is its composite with the sheafification map, hence
is invertible there. Restriction to the affine étale subsite reflects
isomorphisms, so the unit is an isomorphism of sheaves. The adjunction
then gives full faithfulness. For sets the same argument applies because
filtered colimits of sets commute with finite limits.

For the essential image, the set-valued inverse image carries cofiltered
limits of affine pro-étale objects to colimits. This gives the restriction
colimit for every affine étale presentation in
[definition-classical-pro-etale-sheaves], including larger indexing
categories: choose a small étale presentation of the same affine vertex,
and use finite presentation to factor maps through stages and to detect
equality at a stage. The resulting comparison of section colimits shows
that every $\nu_X^*F$ is classical. Naturality of the continuity map shows
that classicality is invariant under isomorphism.

Conversely, if $G$ is classical, both $G$ and
$\nu_X^*\nu_{X,*}G$ carry each affine étale presentation to its section
colimit. On the étale stages the counit is invertible by the unit and the
adjunction identities. Its map on the two colimits is therefore an
isomorphism. The affine pro-étale basis detects isomorphisms, so the
counit is invertible on $G$. Its inverse exhibits $G$ as an inverse image,
which proves the three equivalent conditions.

For modules, identify modules over the constant ring sheaf with sheaves
of $\Lambda$-modules by restriction to constant scalars, and transport
along the equivalences with the small sites used for the coefficient
universe. These identifications commute with comparison inverse image
by uniqueness of left adjoints. Apply the same counit argument to the
resulting sheaf of $\Lambda$-modules: the affine section formula gives
the source colimit, and the assumed continuity maps give the target
colimit. On each étale stage the counit is inverse to the unit.
It is consequently invertible on the affine basis, and hence everywhere.
Transporting the direct-image antecedent and this isomorphism back to
modules over the constant ring sheaf gives the required $F$.
