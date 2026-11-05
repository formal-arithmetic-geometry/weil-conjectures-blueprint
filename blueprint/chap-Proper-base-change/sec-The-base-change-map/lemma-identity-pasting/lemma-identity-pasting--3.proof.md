+++
kind = "proof"
of = "lemma-identity-pasting--3"
order = 319007
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map"]
+++
Direct image preserves injectives, since it is right adjoint to exact
inverse image. Thus the composition isomorphisms
$R(gf)_*\simeq Rg_*Rf_*$ and $R(g'f')_*\simeq Rg'_*Rf'_*$ are
available and are compatible with the units of the right derived
functors.

On sheaves, the square isomorphisms paste, and the composition
isomorphisms for inverse image and direct image correspond under
adjunction. Taking mates as in [definition-underived-base-change-map]
gives the underived vertical pasting formula.

By the uniqueness characterization of the derived map in
[definition-derived-base-change-map], it remains to verify its defining
factorization on each bounded below complex. Express the unit for the
composite direct image through the composition isomorphism, use
naturality to move it through the base change map for $g$, and apply the
factorization formulas for the two squares. Naturality of the remaining
units and comparison isomorphisms reduces the result to the underived
vertical pasting formula.
