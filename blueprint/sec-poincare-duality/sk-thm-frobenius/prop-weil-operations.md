+++
id = "prop-weil-operations"
kind = "theorem"
title = "Six operations on Weil complexes"
lean = ["AlgebraicGeometry.WeilComplex.upperStarCompForgetIso", "AlgebraicGeometry.WeilComplex.nonempty_derivedLowerStar_comp_forget_iso", "AlgebraicGeometry.WeilComplex.nonempty_iso_derivedLowerShriek_comp", "AlgebraicGeometry.WeilComplex.nonempty_iso_derivedLowerShriek_upperStar", "AlgebraicGeometry.WeilComplex.nonempty_iso_derivedLowerShriek_tensorLisse"]
order = 3437
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image-detailed", "def-exchange-projection", "def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-frobenius-detailed", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "det-def-sfb-bounded-constructible", "sk-thm-sf-ctf-stability", "fix-cor-verdier-exchange", "lem-fix-weil-operations", "prop-constructible-truncations", "prop-pur-weil-equivariance-compatibilities", "thm-pod-equivariance-of-the-twisted-pairing", "thm-pur-weil-equivariance-of-purity-and-trace"]
+++
Fix the finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and fix a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$, and
let $E/\Ql$ be finite and contained in $\Qlb$, and let
$\Lambda\in\{E,\Qlb\}$, regarded as a condensed ring. On a scheme $W$ use
the condensed categories
$\Dctf(W,\Lambda)=\Dbc(W,\Lambda)\subseteq D(W_{\mathrm{pro\acute et}},\Lambda)$ of
[det-def-sfb-bounded-constructible], the
separated finite-type
morphism conditions, and the
exceptional inverse image in its constructible form (the exceptional inverse
image of [def-weil-exceptional-inverse-image], defined for every separated
finite-type morphism; the ambient clause (1) of
[def-weil-exceptional-adjoint-admissibility] is not assumed, as it fails in
general). Use the
derived pullback, tensor, and
internal-Hom operations, the
derived direct-image and
compact-support direct image, the
exceptional inverse image, the
exchange/projection transformations, and
the standard truncation functors $\tau^{\leq m},\tau^{\geq m}$.
Let $X_0,Y_0$ be
finite-type $k_0$-schemes
and let $f_0:X_0\to Y_0$ be a
separated finite-type
$k_0$-morphism, and let
$X=X_0\times_{k_0}k$, $Y=Y_0\times_{k_0}k$, and let $f:X\to Y$ be
the geometric fiber of
$f_0$. Put

$$
g_X=\operatorname{id}_{X_0}\times\operatorname{Spec}(\operatorname{Frob}_q),
\qquad
g_Y=\operatorname{id}_{Y_0}\times\operatorname{Spec}(\operatorname{Frob}_q),
$$

using the geometric-Frobenius convention. A Weil complex on $W\in\{X,Y\}$ is
a pair $(K,\theta_K)$ with $K\in\Dbc(W,\Lambda)$ and
$\theta_K:Lg_W^*K\xrightarrow{\sim}K$, as in [def-weil-weil-sheaf-complex]
and [sk-def-sf-weil-complexes]; an object of
$D^b_{c,\mathrm W}(W,\Lambda)$ gives the pair
$(\operatorname{For}(K),\theta_K)$.

For a Weil complex $(K,\theta_K)$ on $X$, and, whenever a tensor or internal
Hom is used on $W$, for Weil complexes $M,N$ on $W$, the operations

$$
Lf^*,\quad Rf_*,\quad Rf_!,\quad Rf^!,\quad -\otimes^L-,\quad R\mathcal Hom
$$

applied to the underlying objects carry induced Weil structures, built from
the exchange and adjunction maps. For example, the Weil structure on
$Rf_*K$ is

$$
Lg_Y^*Rf_*K
\xrightarrow{\operatorname{Ex}_*}
Rf_*Lg_X^*K
\xrightarrow{Rf_*(\theta_K)}Rf_*K,
$$

and the compact-support construction uses $\operatorname{Ex}_!$. The
underlying object of each induced Weil complex is the operation applied to
the underlying object, and morphisms of Weil complexes go to morphisms of
Weil complexes. All these operations preserve $\Dbc(-,\Lambda)=\Dctf(-,\Lambda)$ for
$\Lambda\in\{E,\Qlb\}$ ([sk-thm-sf-ctf-stability]), so equivariance needs no
further preservation theorem.
For every $W\in\{X,Y\}$ and $m\in\mathbf Z$, let
$\tau^{\leq m},\tau^{\geq m}:\Dbc(W,\Lambda)\to\Dbc(W,\Lambda)$
be the truncation functors of [prop-constructible-truncations],
characterized by vanishing of the
cohomology sheaves
$\mathcal H^r(\tau^{\leq m}K)=0$ for $r>m$ and
$\mathcal H^r(\tau^{\geq m}K)=0$ for $r<m$, together with their
standard truncation triangles; they also carry induced Weil structures.
Composition,
base change, projection, purity, and duality isomorphisms are morphisms of
Weil complexes and induce Frobenius-equivariant maps on
cohomology.
