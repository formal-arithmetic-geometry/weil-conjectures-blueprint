+++
kind = "proof"
of = "det-sf-mate-open-restriction"
uses = ["lem-sf-mate", "det-sf-existence-brown", "sk-prop-proper-image-localizing"]
+++
*(1)* On sheaves $j_!\dashv j^*$ with both functors exact, so the adjunction
passes to unbounded derived categories termwise. Both functors preserve the
localizing subcategories: $j^*$ and $j_!$ are exact, preserve direct sums and
carry $\Dctf$ into $\Dctf$ (restriction of a constructible complex of finite
Tor amplitude is again one; for $j_!$ see [sk-prop-proper-image-localizing]),
and the usual closure argument extends this to $\Loc(\Dctf)$. Using the
compactification $j=\mathrm{id}_X\circ j$, $Rj_!=R\mathrm{id}_*\circ j_!=j_!$; so $j^*$
is a right adjoint of $Rj_!$ on the localizing categories, and by the
uniqueness clause of [det-sf-existence-brown] there is a unique isomorphism
$j^!\simeq j^*$ compatible with the two adjunctions.

*(2)* By the composition isomorphism for exceptional inverse images
([lem-sf-mate], i.e. (1) of [sk-lem-sf-mate]) and (1):
$u^*f^!\simeq u^!f^!\simeq(fu)^!=(vf_V)^!\simeq f_V^!v^!\simeq f_V^!v^*$, using
$fu=vf_V$. Likewise $j^*f^!\simeq j^!f^!\simeq(fj)^!$.

*(3)* The restrictions $j_a^*$ along an open covering are jointly
conservative on $D(X_{\mathrm{proét}},\Lambda)$: if a cone $C$ of a morphism $\phi$ has
$j_a^*C=0$ for all $a$, its cohomology sheaves vanish on each $U_a$, hence
vanish, so $C=0$. By (2), $j_a^*f^!\simeq(fj_a)^!$ and similarly over opens of
$Y$, so $f^!$ and maps between its values can be computed locally on $X$ and
on $Y$.
