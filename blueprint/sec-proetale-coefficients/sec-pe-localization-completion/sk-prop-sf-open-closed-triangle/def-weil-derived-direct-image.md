+++
id = "def-weil-derived-direct-image"
kind = "definition"
title = "Derived direct image"
order = 1214
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.lowerStar", "CategoryTheory.Functor.rightDerivedFunctor", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerStarIso", "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunction"]
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "det-def-sfb-module-pushforward-pullback", "det-def-sfb-derived-categories"]
+++
Let $\Lambda$ be a commutative condensed ring, with coefficient sheaves
$\Lambda_W=p_W^*\Lambda$; the cases of interest are $\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$
for a prime $\ell$, a finite extension $E/\Ql$ with uniformizer $\pi_E$, an integer
$n\in\mathbf Z_{\geq1}$ and $A_{E,n}=\mathcal O_E/\pi_E^n$. Let $X,Y$ be schemes and let
$f:X\to Y$ be a morphism [def-weil-scheme-morphism-properties]. On the small pro-étale sites
[def-weil-pbc-proetale-site], with derived pullback and internal Hom
notation [def-weil-derived-pullback-tensor-hom] and derived tensor notation
[def-weil-derived-tensor], the pushforward of module objects
$f_*:\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y}$
([det-def-sfb-module-pushforward-pullback]) is left exact. Its total right
derived functor, computed by K-injective resolutions
([det-def-sfb-derived-categories]), is

$$
 Rf_*:D(X_{\mathrm{proét}},\Lambda)\longrightarrow D(Y_{\mathrm{proét}},\Lambda);
$$

it is right adjoint to the derived pullback $Lf^*$ of [def-weil-derived-pullback-tensor-hom], and,
restriction of scalars along $\eta_f$ being exact, it is the right derived functor of the
transport $\operatorname{mapMod}(f^{\Ab}_*)$ followed by termwise restriction of scalars along
$\eta_f$.

The definition is the same for every $\Lambda$; for
$\Lambda=A_{E,n}$, where $(A_{E,n})_W$ is the classical constant sheaf, write
$f_n$ for $f$ with these coefficients and $Rf_{*,n}=R(f_n)_*$. Here $A_{E,n}$
and finite-level constructibility are the finite-torsion coefficient data
[def-weil-finite-torsion-constructibility], and $\mathcal H^r$ is the
cohomology-sheaf functor [def-weil-derived-cohomology-sheaves].

For $\Lambda=\mathcal O_E$ the projection-formula map

$$
 (Rf_*K)\otimes^L_{\mathcal O_{E,Y}}(A_{E,n})_Y
 \longrightarrow
 Rf_{*,n}\bigl(K\otimes^L_{\mathcal O_{E,X}}(A_{E,n})_X\bigr)
$$

is an isomorphism, and for derived $\pi_E$-complete $K$ one has
$Rf_*K\simeq R\varprojlim_nRf_{*,n}(K\otimes^L_{\mathcal O_{E,X}}(A_{E,n})_X)$.
These are consequences of the definition, proved in
[prop-weil-pbc-direct-image-limits]; they are not used to define $Rf_*$.
