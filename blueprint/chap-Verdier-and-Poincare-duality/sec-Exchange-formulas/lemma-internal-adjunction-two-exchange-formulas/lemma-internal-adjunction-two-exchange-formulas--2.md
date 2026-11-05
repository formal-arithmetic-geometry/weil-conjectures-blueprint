+++
id = "lemma-internal-adjunction-two-exchange-formulas--2"
kind = "lemma"
title = "Verdier duality and direct image with compact support"
name_showing = false
order = 829002
aliases = ["bp-r248-2"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_rightDerivedLowerShriek", "AlgebraicGeometry.WeilComplex.nonempty_verdierDual_derivedLowerShriek_iso"]
uses = ["definition-compactification-refinement", "definition-verdier-dual-evaluation", "definition-weil-structure", "theorem-exceptional-inverse-image"]
+++
Let $\Lambda$ be a finite commutative ring, let $f:X\to Y$ and
$a_Y:Y\to S$, and put $a_X=a_Y\circ f$. Suppose that $f$, $a_Y$ and
$a_X$ each admit a compactification. Define
$\omega_X=a_X^!\Lambda_S$, $\omega_Y=a_Y^!\Lambda_S$, and
$\mathbb D=\cHom(-,\omega)$ as in
[definition-verdier-dual-evaluation]. For every
$K\in D(X_{\acute{e}t},\Lambda)$ there is an isomorphism

$$
\mathbb D_YRf_!K\simeq Rf_*\mathbb D_XK.
$$

There is also the following version for Weil complexes. Let $k_0$ be a
finite field and $\ell$ a prime different from its characteristic, and
let $f:X\to Y$ be a separated morphism of finite type between separated
schemes of finite type over $k_0$. Suppose the compactly supported direct
images of the structure maps $a_X$ and $a_Y$ have right adjoints. For
every Weil complex $K$ with coefficients in $\overline{\mathbf Q}_\ell$
there is an isomorphism

$$
\mathbb D_YRf_!K\simeq Rf_*\mathbb D_XK
$$

in the category of Weil complexes. This statement does not assume a
right adjoint to $Rf_!$ itself.
