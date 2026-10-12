+++
kind = "proof"
of = "lem-weil-pbc-flat-under-regular"
+++
Lift R to ULift.{v} R and S to ULift.{u} S, both in universe max u v. Transport the local and Noetherian instances on R and regularity on S across ULift.ringEquiv. The lifted map RingHom.ulift phi is local by composition of local maps and is flat by RingHom.Flat.ulift_iff. Equip the lifted target with the algebra structure induced by this map and apply the already proved source-library theorem IsRegularLocalRing.of_flat (WeilConjectures.Mathlib.RingTheory.Regular.ProjectiveDimension, Stacks 00OF). Finally transport regularity of the lifted source back to R by IsRegularLocalRing.of_ringEquiv. This uses the existing proof of 00OF, not any of the planned finite-resolution Sheaf statements.
