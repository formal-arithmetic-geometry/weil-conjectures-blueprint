+++
kind = "proof"
of = "proposition-forgetting-supports-composition--3"
order = 519006
uses = ["proposition-forgetting-supports-composition--2", "proposition-composition-base-change-rf-shriek", "definition-derived-base-change-map"]
+++
For any compactification of proper $f$, the open immersion $j$ is also
closed. The functors $j_!$ and $j_*$ are then two left adjoints of $j^*$,
so they are isomorphic. The exactness of $j_*$ identifies $Rj_*$ with its
induced functor on derived categories, and its full faithfulness makes
the counit of $j^*\dashv Rj_*$ invertible. The triangle identity shows
that the unit is invertible on $j_!K\simeq Rj_*K$. Hence $\alpha_j$ is
an isomorphism. Applying $Rp_*$ proves the first assertion; composing
with the ordinary direct-image isomorphism gives $\eta_f$.

For the composition identity, substitute $h=gf$. Let $d$ be the chosen
compactification of $g$ and let $e$ be the compactification of
$j_d f$ obtained from the chosen compactification of $gf$.
The specified composition map is built from the comparisons with
$e$ restricted over $Y$ and with $d\circ e$, and the composition map
on these compatible compactifications.

Expand this last map into the interchange of extension by zero with
proper direct image, composition of extensions by zero, and composition
of ordinary direct images. The interchange commutes with forgetting
supports by the base change identity for $\alpha_j$, transposed under
the derived pullback/direct-image adjunctions. The two open-immersion
comparisons compose to the comparison for the composite open immersion:
their transposes agree by the composite counit formula. Naturality and
associativity of ordinary direct-image composition now give
`AlgebraicGeometry.Etale.properShriekComp_compactificationForgetSupports`.

Move the forget-supports maps through the compactification comparisons
using [proposition-forgetting-supports-composition--2] and cancel the
inverse comparisons. This is the calculation
`AlgebraicGeometry.Etale.properShriekComp_comp_forgetSupports_raw`.
Identifying the specified composition map for $h=gf$ with this map and
transporting back along the specified equality gives the asserted
identity. Naturality of $\eta_g$ gives the other order of the two
forget-supports maps in the square.
