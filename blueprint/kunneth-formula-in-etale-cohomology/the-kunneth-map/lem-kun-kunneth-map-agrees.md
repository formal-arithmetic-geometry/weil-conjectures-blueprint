+++
id = "lem-kun-kunneth-map-agrees"
kind = "lemma"
title = "Compatibility of the Kunneth map with Leray, proper base change and the projection formula"
order = 6136
lean = ["AlgebraicGeometry.Etale.kunnethMap_isIso_of_isProper"]
uses = ["def-kun-kunneth-map", "lem-kun-0F0C", "lem-kun-0F0E", "lem-kun-0F0F", "lem-kun-0F0G", "lem-kun-0F10", "lem-kun-0F12", "lem-kun-leray-bdd", "lem-kun-leray-unbdd", "lem-kun-tensor-sym", "def-kun-derived-tensor", "def-kun-unbounded-exchange", "lem-kun-inverse-image-monoidal", "lem-kun-tensor-unit", "lem-kun-pullback-constant", "lem-kun-unbounded-exchange-natural"]
+++
Let $k$ be a separably closed field, $X$ a proper scheme over $k$ and $Y$
a scheme over $k$. Denote $f:X\to\Spec(k)$, $g:Y\to\Spec(k)$ and
$c=f\circ\operatorname{pr}_1=g\circ\operatorname{pr}_2$ on $X\times_kY$.

(a) Let $E\in\Dplus(X_{\Et})$ have torsion cohomology and
$K\in\Dplus(Y_{\Et})$. Let $\theta$ be the composite
$$
 \begin{aligned}
 &\RGamma\bigl((X\times_kY)_{\Et},
   \operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z}\operatorname{pr}_2^{-1}K\bigr)\\
 &\quad\xrightarrow{\ \sim\ }
   \RGamma\bigl(Y_{\Et},R\operatorname{pr}_{2,*}
   (\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z}\operatorname{pr}_2^{-1}K)\bigr)\\
 &\quad\xrightarrow{\ \sim\ }
   \RGamma\bigl(Y_{\Et},R\operatorname{pr}_{2,*}\operatorname{pr}_1^{-1}E
   \otimes^{\mathbf L}_{\mathbf Z}K\bigr)\\
 &\quad\xrightarrow{\ \sim\ }
   \RGamma\bigl(Y_{\Et},\underline{\RGamma(X_{\Et},E)}
   \otimes^{\mathbf L}_{\mathbf Z}K\bigr)\\
 &\quad\xrightarrow{\ \sim\ }
   \RGamma(Y_{\Et},K)\otimes^{\mathbf L}_{\mathbf Z}\RGamma(X_{\Et},E)\\
 &\quad\xrightarrow{\ \sim\ }
   \RGamma(X_{\Et},E)\otimes^{\mathbf L}_{\mathbf Z}\RGamma(Y_{\Et},K),
 \end{aligned}
$$
whose five arrows are [lem-kun-leray-bdd], [lem-kun-0F0F], the bounded-below
proper base change theorem, [lem-kun-0F0E] and [lem-kun-tensor-sym]
respectively. Then $\theta\circ\kappa_{E,K}=\mathrm{id}$, where
$\kappa_{E,K}$ is the Kunneth map of [def-kun-kunneth-map]; in particular
$\kappa_{E,K}$ is an isomorphism.

(b) Let $n\ge1$ be invertible in $k$, let $Y$ be of finite type over $k$, let
$E\in D(X_{\Et},\mathbf Z/n\mathbf Z)$ and
$K\in D(Y_{\Et},\mathbf Z/n\mathbf Z)$, and let $\theta$ be the same composite
with $\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}$-products, where the first
arrow uses [lem-kun-leray-unbdd] and [lem-kun-0F10], the second
[lem-kun-0F0G], the third [lem-kun-0F0C], the fourth [lem-kun-0F12], and the
fifth [lem-kun-tensor-sym]. Then $\theta\circ\kappa_{E,K}=\mathrm{id}$ and
$\kappa_{E,K}$ is an isomorphism.

## Proof

We verify (a); the proof of (b) is identical, replacing [lem-kun-0F0F] by
[lem-kun-0F0G], the bounded-below proper base change theorem by
[lem-kun-0F0C], [lem-kun-0F0E] by [lem-kun-0F12] and [lem-kun-leray-bdd] by
[lem-kun-leray-unbdd]. It suffices to compare adjoints under
$c^{-1}\dashv Rc_*$ (writing $c:X\times_kY\to\Spec(k)$). By
[def-kun-kunneth-map] the adjoint of $\kappa_{E,K}$ is
$(\varepsilon_f\otimes\varepsilon_g)\circ\mathrm{mon}$. Each arrow in the
definition of $\theta$ is the mate of an identification built from the
adjunction data of the inverse image and of [def-kun-derived-tensor]: the
first is the comparison
$\RGamma\circ R\operatorname{pr}_{2,*}\cong\RGamma$ (an instance of the Leray
composition [lem-kun-leray-bdd]); the second is the projection formula map of
[lem-kun-0F0F], which is by definition the mate of the unit--monoidality
composite of [lem-kun-inverse-image-monoidal]; the third is the inverse of the
proper base change map, itself the mate of $\varepsilon_f$ by
[def-kun-unbounded-exchange]; the fourth is the map of [lem-kun-0F0E], whose
mate is $\mathrm{id}\otimes\eta_g$ for the unit $\eta_g$ (using
[lem-kun-tensor-unit] and [lem-kun-pullback-constant] for the constant
objects); the fifth is the symmetry [lem-kun-tensor-sym], whose mate is again
the symmetry.

Applying $c^{-1}$ to $\theta\circ\kappa_{E,K}$ therefore yields the composite
of the corresponding mates, and an elementary cancellation of each unit
against the adjacent counit -- all compatibilities being instances of the
pasting law for exchange morphisms and of the naturality of
[lem-kun-unbounded-exchange-natural] -- leaves exactly
$(\varepsilon_f\otimes\varepsilon_g)\circ\mathrm{mon}$, the adjoint of
$\mathrm{id}$. Since the adjunction bijection is injective,
$\theta\circ\kappa_{E,K}=\mathrm{id}$, and as $\theta$ is an isomorphism so is
$\kappa_{E,K}$.

Unresolved dependencies: thm:weil-pbc-bounded-below, def:weil-pbc-inverse-image, lem:weil-pbc-exchange-identity-pasting
