+++
kind = "proof"
of = "det-ctf-finite-comparison-localizing"
+++
By [sk-prop-pe-unbounded-classical], $\nu_X^*$ is exact, fully faithful and preserves sums on the unbounded
categories; by [sk-cor-pe-finite-tor-comparison] it maps $\Dctf(X_{\mathrm{ét}},A)$ essentially surjectively onto
$\Dctf(X,A)$.

*Image of the closure.* The objects $K\in\Loc(\Dctf(X_{\mathrm{ét}},A))$ with $\nu_X^*K\in\Loc(\Dctf(X,A))$ form a
localizing subcategory (exactness and sum preservation) containing the generators; hence all of
$\Loc(\Dctf(X_{\mathrm{ét}},A))$ maps into $\Loc(\Dctf(X,A))$.

*Essential surjectivity.* The essential image $\mathcal I$ of $\Loc(\Dctf(X_{\mathrm{ét}},A))$ under the fully faithful
exact sum-preserving $\nu_X^*$ is a triangulated subcategory closed under sums (a cone of
$\nu_X^*K\to\nu_X^*K'$ is $\nu_X^*$ of the cone of the preimage of the map), and it contains $\Dctf(X,A)$. So
$\mathcal I\supset\Loc(\Dctf(X,A))$ ([sk-def-localizing-closure]). Together with full faithfulness this is an
equivalence.

*Operations.* $\nu^*$ commutes with inverse image ($\nu_{X}^*g^*=g^*\nu_Y^*$, composition of inverse images of
morphisms of sites), with extension by zero along open immersions (stalkwise description; Stacks, Tag 09AF),
and with direct image by the direct-image comparison of [sk-prop-pe-unbounded-classical]. Composing the
last two for a compactification $f=p\circ j$ gives $\nu_Y^*Rp_*j_!\simeq Rp_*j_!\nu_X^*$.
