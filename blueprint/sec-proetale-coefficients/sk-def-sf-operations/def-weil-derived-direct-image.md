+++
id = "def-weil-derived-direct-image"
kind = "definition"
title = "Derived direct image"
order = 1827
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "sk-def-sfb-module-pushforward-pullback", "sk-def-sfb-derived-categories"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$ with uniformizer $\pi_E$, an
integer $n\in\mathbf Z_{\geq1}$, and put $A_{E,n}=\mathcal O_E/\pi_E^n$. Let
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring, with
coefficient sheaves $\Lambda_W=p_W^*\Lambda$. Let $X,Y$ be schemes on which
$\ell$ is invertible, and let $f:X\to Y$ be a morphism
[def-weil-scheme-morphism-properties]. On the small pro-étale sites
[def-weil-pbc-proetale-site], with derived pullback and internal Hom
notation [def-weil-derived-pullback-tensor-hom] and derived tensor notation
[def-weil-derived-tensor], the pushforward of module objects
$f_*:\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y}$
([sk-def-sfb-module-pushforward-pullback]) is left exact. Its total right
derived functor, computed by K-injective resolutions
([sk-def-sfb-derived-categories]), is

$$
 Rf_*:D(X_{\mathrm{proét}},\Lambda)\longrightarrow D(Y_{\mathrm{proét}},\Lambda).
$$

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
