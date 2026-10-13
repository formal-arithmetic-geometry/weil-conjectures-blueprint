+++
kind  = "proof"
of    = "lem-exc-closed-localization"
+++
By the slice identification in
[lem-weil-pbc-proetale-restriction-injectives], restriction is evaluation on
objects over $W$. Both closed direct images evaluate a sheaf $G$ on such an
object $W'$ as $G(W'\times_XZ)$, so they agree with their restriction maps.
For inverse images, both composites carry a representable sheaf to the sheaf
of its base change by the same cartesian square of
[def-weil-pbc-cartesian-square]. All sheaves are colimits of
representables; for modules use free module sheaves on representables and a
cokernel presentation. Inverse images preserve these colimits, so the
identifications extend to all sheaves. In the sectionwise adjunction of the
pro-etale operations, the unit restricts a section to the base change and
the counit evaluates that restriction. The identifications just constructed
preserve these maps, which proves the claimed compatibility.
