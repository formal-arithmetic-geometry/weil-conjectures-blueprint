+++
id = "prop-functor-package"
kind = "theorem"
title = "Coefficient and functor package on the proved domains"
lean = ["AlgebraicGeometry.WeilComplex.derivedLowerShriekObjIsoDerivedLowerStar", "AlgebraicGeometry.WeilComplex.nonempty_derivedLowerShriek_toComplex_iso_of_isOpenImmersion", "AlgebraicGeometry.WeilComplex.nonempty_derivedLowerShriek_comp_iso", "AlgebraicGeometry.WeilComplex.exists_distTriang_derivedLowerShriek_openClosed", "AlgebraicGeometry.WeilComplex.nonempty_upperStar_derivedLowerShriek_iso", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.upperStar_derivedLowerShriek_of_isPullback", "AlgebraicGeometry.WeilSheaf.higherLowerShriekZeroObjIsoLowerStar"]
order = 3563
tags = ["latex:proposition"]
uses = ["cor-cbc-proper-coincidence", "cor-weil-boundary-duality-discharge", "cor-weil-finite-constructible-hom", "def-fix-six-functor-datum", "fix-cor-verdier-exchange", "fix-lem-exchanges", "fix-prop-coherence", "fix-prop-projection-formula", "lem-cbc-open-closed-recollement", "lem-coef-finite-direct-image", "lem-coef-finite-exceptional", "lem-compact-support-direct-image-triangulated", "lem-fix-compact-support-coefficient-change", "lem-fix-operation-reduction", "lem-weil-coefficient-frobenius", "prop-compactification-coherence-detailed", "sbc-thm-bounded-below-derived-smooth-base-change", "def-sf-setting", "sk-def-sf-categories", "det-def-sfb-coefficient-change", "det-prop-sfb-finite-extension-compatibility", "sk-thm-sfb-qlbar-two-colimit", "sk-prop-scalar-six", "sk-thm-existence", "sk-thm-sf-ctf-stability", "sk-thm-pd-verdier-duality", "sk-thm-sfb-proper-base-change", "sk-thm-sbc-coefficients", "det-prop-sf-cbc", "sk-thm-purity-transport", "thm-cbc-finite-torsion", "thm-coef-finite-hom", "thm-coef-integral-verdier", "thm-fix-general-biduality", "thm-pur-finite-coefficient-smooth-purity", "thm-sf-comp-composition", "thm-sf-dual-perfect", "thm-weil-pbc-bounded-below"]
+++
Use the admissible coefficient rings $A_{E,n},\mathcal O_E,E,\Qlb$ of
[def-sf-setting], regarded as condensed rings, finite-type
separated schemes over the fixed algebraic closure of a finite field, and separated
finite-type morphisms of [def-fix-six-functor-datum]. For each $\Lambda$ the
categories are the full subcategories
$\Dctf(X,\Lambda)\subseteq D(X_{\mathrm{pro\acute et}},\Lambda)$ of
[sk-def-sf-categories]; for $\Lambda=\mathcal O_E,E,\Qlb$ they equal
$\Dbc(X,\Lambda)$.
Pullback, tensor and the two direct images have their proved constructible
domains. At finite stages, internal Hom preserves bounded constructible
finite-Tor complexes in both variables by
[cor-weil-finite-constructible-hom].
General internal-Hom coefficient change is [thm-coef-finite-hom].
For every admissible $\Lambda$, the six operations preserve $\Dctf$
([sk-thm-sf-ctf-stability]), and the
exceptional inverse image is the right adjoint of $Rf_!$ on $\Dctf$ given by
[sk-thm-existence]; their comparisons under reduction and extension of
scalars are [sk-prop-scalar-six].
The sharper dimension-free Hom bound and tensor-dual formulas still
require a site-perfect first
argument. Exceptional adjunction here is on these constructible
categories, without asserting an unrestricted unbounded ambient adjoint.
The following seven clauses collect the preceding results.

1. Extension of scalars along $E_X\to F_X\to\Qlb_X$, for finite extensions
$F/E$, is exact, because these rings are flat over $E_X$, and commutes with
the operations ([det-prop-sfb-finite-extension-compatibility]). Every object
and morphism of $\Dbc(X,\Qlb)$ descends to some finite $E$
([sk-thm-sfb-qlbar-two-colimit]); this is a consequence about the condensed
category, not its definition.
1. Compactification comparisons for $Rf_!=R\bar f_*j_!$ are independent
of refinement and satisfy the cocycle condition. For
$K\in\Dbc(X,\mathcal O_E)$, put
$K_n=K\otimes^L_{\mathcal O_{E,X}}A_{E,n}$. Then
$$
(Rf_*K)\otimes^L_{\mathcal O_E}A_{E,n}\simeq Rf_*K_n,
\qquad
(Rf_!K)\otimes^L_{\mathcal O_E}A_{E,n}\simeq Rf_!K_n
$$
([sk-prop-scalar-six]). Between finite quotient rings, both direct-image
coefficient comparisons hold on the bounded finite-Tor domains.
1. Compact-support composition satisfies
$R(gf)_!\simeq Rg_!Rf_!$, with the identity and associativity equations.
For proper $f$, $Rf_!\simeq Rf_*$. For a closed immersion $i$
with open complement $j$, applying $Rf_!$ to the localization triangle gives
$$
R(fj)_!j^*K\longrightarrow Rf_!K\longrightarrow R(fi)_!i^*K\longrightarrow .
$$
1. In a Cartesian square, $g^*Rf_*\to Rf'_*g'^*$ is an isomorphism
if $f$ is proper or $g$ is smooth, and
$g^*Rf_!\simeq Rf'_!g'^*$ for arbitrary base change, on the stated
bounded coefficient domains: at the finite stages for $g^*Rf_*$ on
bounded-below complexes with torsion cohomology, and for every admissible
$\Lambda$ on $\Dctf(X,\Lambda)$ ([sk-thm-sfb-proper-base-change],
[sk-thm-sbc-coefficients], [det-prop-sf-cbc]); no claim is made for discrete
non-torsion coefficients on the small étale site.
1. For $K\in D^b_c(X,\Lambda)$ and $L\in D^b_{ctf}(Y,\Lambda)$,
the compact-support projection map is an isomorphism:
$$
Rf_!K\otimes^L L\simeq Rf_!(K\otimes^L f^*L).
$$
1. Smooth purity for relative dimension $r$ identifies
$Rf^!L\simeq f^*L(r)[2r]$, with its normalized trace, for every admissible
$\Lambda$ ([sk-thm-purity-transport]).
1. For separated finite-type $f:X\to Y$ and structure morphisms set
$\omega_X=Ra_X^!\Lambda$ and
$D_X=R\mathcal Hom(-,\omega_X)$. For
$M\in D^b_{ctf}(X,\Lambda)$, the formal Verdier exchange map of
[fix-cor-verdier-exchange] is a natural isomorphism
$$
D_YRf_!M\xrightarrow{\ \sim\ }Rf_*D_XM.
$$
Point biduality and smooth site-perfect biduality are proved independently.
At every finite stage $A=A_{E,n}$, the general anti-equivalence
$D_Y:D^b_{ctf}(Y,A)^{\mathrm{op}}\simeq D^b_{ctf}(Y,A)$, with
$D_Y^2\simeq\operatorname{id}$, is
[thm-fix-general-biduality]. Its geometric proof also supplies the
finite-stage boundary comparison in
[cor-weil-boundary-duality-discharge].
For every admissible $\Lambda$ the same anti-equivalence and
evaluation-defined biduality hold on $\Dctf(Y,\Lambda)$
([sk-thm-pd-verdier-duality]; integrally [thm-coef-integral-verdier]).
On these domains $Rf^!=D_Xf^*D_Y$, with its exceptional adjunction
([sk-thm-existence], [lem-coef-finite-exceptional] at finite levels), and the
coefficient comparisons are [sk-prop-scalar-six].

All comparisons have the coherence and equivariance proved for their
individual clauses. No clause enlarges the domain of another clause.
