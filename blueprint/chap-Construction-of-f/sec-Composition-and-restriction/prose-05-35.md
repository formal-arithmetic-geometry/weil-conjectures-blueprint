+++
id = "prose-05-35"
kind = "hidden"
title = "Composition and restriction (1)"
order = 529
+++
Brown representability gives [$f^!$](@theorem-existence-exceptional-inverse-image) one morphism at a time. To compute it in Chapter [chap-Constructibility-of-f], however, we factor $f$ locally. The two are linked by uniqueness of adjoints: an isomorphism between composites of left adjoints, such as $\href{@proposition-construction-independence-rf-shriek}{Rg_!}\circ \href{@proposition-construction-independence-rf-shriek}{Rf_!}\simeq \href{@proposition-construction-independence-rf-shriek}{R(gf)_!}$ or
$\href{@proposition-construction-independence-rf-shriek}{Rf_!}=Rp_*\circ j_!$, gives an isomorphism between the right
adjoints, composed in the opposite order. Since $\href{@theorem-existence-exceptional-inverse-image}{j^!}=j^*$ for an open
immersion $j$, it follows that [$f^!$](@theorem-existence-exceptional-inverse-image) is local on $X$ and on $Y$. For example, a smooth $f$ is
locally the composite of an étale map and a projection
$\mathbf A^n_Y\to Y$. By composition and locality, [$f^!$](@theorem-existence-exceptional-inverse-image) is then
determined by its values on these two kinds of maps.

Base change for [$f^!$](@theorem-existence-exceptional-inverse-image) does not follow in this way. Passing to right
adjoints in the base change isomorphism $v^*\href{@proposition-construction-independence-rf-shriek}{Rf_!}\simeq \href{@proposition-construction-independence-rf-shriek}{Rf'_!}u^*$ relates
$\href{@theorem-existence-exceptional-inverse-image}{f^!}Rv_*$ and $Ru_*\href{@theorem-existence-exceptional-inverse-image}{f'^!}$. These involve direct images, not the
inverse images $u^*\href{@theorem-existence-exceptional-inverse-image}{f^!}$ and $\href{@theorem-existence-exceptional-inverse-image}{f'^!}v^*$ that one wants to compare. We prove
base change for smooth morphisms in
Proposition [proposition-exceptional-inverse-image-smooth-morphism]. That
[$f^!$](@theorem-existence-exceptional-inverse-image) preserves [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves) is proved in
Theorems [theorem-f-shriek-finite-coefficients] and [theorem-f-shriek-ell-adic-coefficients].
