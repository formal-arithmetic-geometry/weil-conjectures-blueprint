+++
kind = "proof"
of = "proposition-topos-functoriality--2"
order = 39002
uses = ["lemma-stability", "proposition-topos-functoriality--1"]
+++
By [lemma-stability], base change preserves weakly étale objects.
The universal properties of the final object and fibre products show
that $b_f$ preserves finite limits. The image of a covering family is
its base change, so it is again a covering family. This makes $b_f$
continuous, and restriction along it carries sheaves to sheaves.

Compose the left Kan extension adjunction with the sheafification
adjunction of [proposition-topos-functoriality--1]. This gives
$f^{-1}\dashv f_*$, and hence preservation of all colimits by $f^{-1}$.
Since $b_f$ preserves finite limits, the comma categories computing
the left Kan extension along $b_f^{\mathrm{op}}$ are filtered.
Filtered colimits of sets commute with finite limits. The inclusion
of sheaves into presheaves preserves limits, and sheafification is
left exact, so their composite $f^{-1}$ preserves finite limits.

For abelian sheaves, the same filtered-colimit argument gives left
exactness, and the adjunction gives right exactness. To compare
underlying sets, identify abelian sheaves with commutative group
objects in sheaves of sets and lift the set-valued adjunction to
these group objects. Its right adjoint is abelian direct image.
Uniqueness of left adjoints identifies the lifted inverse image
with the abelian Kan-extension construction, giving the asserted
isomorphism on underlying sheaves of sets.
