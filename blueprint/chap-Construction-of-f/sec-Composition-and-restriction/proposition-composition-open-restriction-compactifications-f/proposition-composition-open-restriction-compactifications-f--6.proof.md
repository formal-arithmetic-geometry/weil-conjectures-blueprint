+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f--6"
order = 530015
uses = ["theorem-existence-exceptional-inverse-image", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Take the chosen right adjoint $P_p$ of the proper direct image $Rp_*$ and
follow it by the exact restriction $j^*$. The composite adjunction of
$j_!\dashv j^*$ and $Rp_*\dashv P_p$ gives
$$
Rp_*j_!\dashv j^*P_p.
$$
This is `AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactificationAdjunction`
for finite coefficients, and the corresponding
`boundedConstructibleUpperShriekOfCompactificationAdjunction` in the
three condensed coefficient settings. Choosing the compactification
then defines $f^!$ and its adjunction.
