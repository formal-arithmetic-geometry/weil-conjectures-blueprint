+++
id = "thm-pur-regular-immersion-purity"
kind = "theorem"
title = "Purity for regular closed immersions"
order = 3408
uses = ["cor-pur-affine-space-purity", "cor-pur-affine-space-zero-section-purity", "lem-pur-projection-purity-agreement", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-frame-class", "def-pur-regular-immersion", "def-weil-derived-tensor", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-frame-independence", "lem-pur-immersion-twist", "lem-pur-kunneth-supported", "lem-pur-regular-immersion-linearization", "lem-pur-regular-immersion-smooth-structure", "thm-pur-composition-coherence", "thm-pur-diagonal-dualizing-object"]
+++
In the purity conventions of [def-pur-conventions],
let $i:Z\hookrightarrow X$ be a
regular closed immersion of pure
codimension $c$, with $X$ smooth over the perfect field $k$ and
$Z$ regular. Then $Ri^!\Lambda_X(c)[2c]$ is concentrated in degree
$0$, with $\mathcal H^0$ free of rank one, so that
$H^0(Z,Ri^!\Lambda_X(c)[2c])=H^{2c}_Z(X,\Lambda(c))$. The
*fundamental class*
$[Z\subset X]\in H^{2c}_Z(X,\Lambda(c))$ is the global class whose
restriction to every frame $(U,f)$ of [def-pur-frame-class] is
$\operatorname{cl}(f)$ (it exists and is unique by
[lem-pur-frame-independence] and the sheaf property of
$\mathcal H^0$). There is a canonical isomorphism

$$
\operatorname{cl}_i:\Lambda_Z\xrightarrow{\ \sim\ }Ri^!\Lambda_X(c)[2c],
\qquad 1\longmapsto[Z\subset X],
$$

equivalently (cancelling the invertible twist) a canonical
isomorphism $Ri^!\Lambda_X\xrightarrow{\sim}\Lambda_Z(-c)[-2c]$,
the inverse of $\operatorname{cl}_i(-c)[-2c]$. It is compatible with
etale base change and with exterior products.
