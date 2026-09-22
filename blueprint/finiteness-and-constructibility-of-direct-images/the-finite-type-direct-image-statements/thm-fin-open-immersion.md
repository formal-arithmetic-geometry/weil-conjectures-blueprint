+++
id = "thm-fin-open-immersion"
kind = "theorem"
title = "Open-immersion direct images"
order = 5817
lean = ["AlgebraicGeometry.Etale.isConstructible_higherDirectImage_of_isOpenImmersion'"]
uses = ["cor-fin-deligne-open-finite-coefficients"]
+++
Let $j:U\hookrightarrow X$ be an open immersion of finite-type schemes over
a field $k$, and let $F$ be a finite constructible $\Lambda$-sheaf with the
prime-to-characteristic finite coefficients of this blueprint. Every higher
direct image $R^qj_*F$ is constructible, and they vanish for all
sufficiently large $q$. For $q>0$ their restrictions to $U$ vanish.

## Proof

The bounded constructibility assertion is
[cor-fin-deligne-open-finite-coefficients], applied to the sheaf $F$ in
degree zero.

To check the support assertion, choose an injective resolution
$F\to I^\bullet$ on $U_{\Et}$. The section definition of the direct image
gives $j^*j_*I^\bullet=I^\bullet$. Exactness of the inverse image gives
$j^*\mathcal H^q(Rj_*F)=\mathcal H^q(F)=0$ for $q>0$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, sbc-def-coefficient-conventions, def:weil-pbc-inverse-image
