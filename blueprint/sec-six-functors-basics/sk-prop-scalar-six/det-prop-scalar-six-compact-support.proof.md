+++
kind  = "proof"
of    = "det-prop-scalar-six-compact-support"
uses = ["det-prop-scalar-six-direct-image", "det-prop-scalar-six-pullback", "det-prop-scalar-six-ctf", "sk-thm-existence", "sk-thm-sf-ctf-stability"]
+++
*Isomorphism.* $j_!K\in\Dctf(\overline X,\Lambda)$ ([sk-thm-sf-ctf-stability]), so the first
arrow, the direct-image comparison of [det-prop-scalar-six-direct-image] for $p$, is an
isomorphism; the second is the extension-by-zero identification of
[det-prop-scalar-six-pullback] (2). Both sides lie in $\Dctf(Y,\Lambda')$ by
[sk-thm-existence] (2) and [det-prop-scalar-six-ctf].

*Independence.* Two compactifications are dominated by a third, so it suffices
to compare $\overline X$ with a refinement $h\colon\overline X'\to\overline X$ (proper, with
$h\circ j'=j$ and $p'=p\circ h$). The identification of $Rp_*j_!$ with $Rp'_*j'_!$ comes
from the refinement map $e\colon j_!K\to Rh_*j'_!K$, which is the unique map restricting
to the identity of $K$ on $X$ (by the adjunction $j_!\dashv j^*$ and
$j^*Rh_*j'_!K=K$, as $h$ is an isomorphism over the dense open $X$). The two composites
$(j_!K)_{\Lambda'}\to Rh_*j'_!(K_{\Lambda'})$, "refine then compare"
$\gamma_{h,j'_!K}\circ(e)_{\Lambda'}$ (after the $j'_!$-identification) and "compare then
refine" $e_{K_{\Lambda'}}$ (after the $j_!$-identification), are both formed from the
same pullback identifications and adjunction maps and restrict to the identity of
$K_{\Lambda'}$ on $X$; by the adjunction $j_!\dashv j^*$ they are equal. Applying $Rp_*$ and
the compatibility of $\gamma$ with composition $R(ph)_*=Rp_*Rh_*$
([det-prop-scalar-six-direct-image] (2)) shows that the comparisons defined with
$\overline X$ and $\overline X'$ agree.

*Composition.* The isomorphism $R(gf)_!\simeq Rg_!Rf_!$ is built from proper direct
images, extensions by zero, and the base-change isomorphism
$j_!Rq_*\simeq Rq'_*j'_!$ in a compactification of a composite, which is again
characterized by restricting to the identity on an open subscheme. The
comparison maps commute with each of these: with proper direct images by
[det-prop-scalar-six-direct-image] (2), with extensions by zero by
[det-prop-scalar-six-pullback] (2), and with the interchange maps by the
restriction argument of the previous paragraph. Hence $\gamma^!$ respects
composition.
