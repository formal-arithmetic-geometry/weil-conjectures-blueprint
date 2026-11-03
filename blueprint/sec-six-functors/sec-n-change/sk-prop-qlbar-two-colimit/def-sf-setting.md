+++
id = "def-sf-setting"
kind = "definition"
title = "Coefficients and sites"
order = 2854
uses = ["det-def-sfb-condensed-ring", "det-def-sfb-qlbar-condensed", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-derived-categories", "def-sfb-constructible-module", "det-def-sfb-bounded-constructible", "def-weil-finite-tor-amplitude", "def-coefficient-twists-detailed", "thm-weil-pbc-site-comparison", "lem-sf-proetale-constructible-origin", "det-pe-finite-tor-comparison-noetherian", "det-prop-sfb-qlbar-colimit-x-integral-limit", "det-prop-sfb-qlbar-colimit-x-invert-ell", "def-sfb-qlbar-x-cocone", "det-prop-integral-criterion-reductions", "thm-sfb-extend-scalars-localization", "def-sfb-rationalization-equivalence", "thm-sfb-constructible-cocone-two-colimit", "det-lem-int-integral-heart-dualizable"]
lean = ["AlgebraicGeometry.ProEtale.condensedRingObj", "AlgebraicGeometry.ProEtale.boundedConstructible", "DerivedCategory.finiteTorAmplitude", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedConstructible", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor"]
+++
Fix a base field $k$ that is finite or algebraically closed, a prime $\ell$ different from the characteristic of $k$, a finite extension $E/\Ql$ inside $\Qlb$ with valuation ring
$\mathcal O_E$ and uniformizer $\pi_E$ ([det-def-sfb-condensed-ring]), an integer $n\ge1$, and put
$A_{E,n}=\mathcal O_E/\pi_E^n$. The admissible coefficient rings are
$\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$, where $A$ is an arbitrary finite commutative
$\ell$-primary ring; the rings $A_{E,n}$ are the distinguished family of finite coefficients
used for integral reduction. They are regarded as condensed rings: $A$ with its
discrete topology, $\underline{\mathcal O}_E$ and $\underline E$ ([det-def-sfb-condensed-ring]), and
$\underline{\Qlb}$ ([det-def-sfb-qlbar-condensed]). For a scheme $X$ the coefficient sheaf is
$\Lambda_X=p_X^*\Lambda$ on $X_{\mathrm{proét}}$ ([det-def-sfb-pulled-back-coefficients]); it is the
unit of $\otimes^L_{\Lambda}$, and $D(X,\Lambda)=D(X_{\mathrm{proét}},\Lambda)$ is the derived
category of $\Lambda_X$-modules ([det-def-sfb-derived-categories]). $D^b_c(X,\Lambda)\subseteq
D(X_{\mathrm{proét}},\Lambda)$ consists of the bounded complexes with constructible cohomology
sheaves ([def-sfb-constructible-module], [det-def-sfb-bounded-constructible]), and
$D^b_{ctf}(X,\Lambda)\subseteq D^b_c(X,\Lambda)$ of those of finite Tor amplitude over
$\Lambda_X$ ([def-weil-finite-tor-amplitude]). These categories come with constructible
intervals and the Tate twists of [def-coefficient-twists-detailed]. Morphisms are separated of finite type.

*Finite-field datum.* The global finite-field datum $(p,a,q,k_0,k)$ with $k=\overline{\mathbf F}_q$ is
introduced only where Frobenius is needed; the six operations and purity are stated in the geometric
setting above. Statements over a finite field are deduced from $\bar k$ by conservative pullback only
after the canonical separable-extension comparisons for exceptional restriction, internal Hom and
evaluation, which precede any biduality theorem being descended.

*Finite coefficients.* For $\Lambda=A$ the sheaf $A_X$ is the classical constant sheaf, and
$\nu_X^*$ identifies the étale categories with the pro-étale ones: $D^b_c(X_{\mathrm{ét}},A)$,
the bounded complexes of sheaves of $A$-modules on the small étale site with constructible
cohomology sheaves, and its subcategory $D^b_{ctf}(X_{\mathrm{ét}},A)$, are carried
equivalently onto $D^b_c(X,A)$ and $D^b_{ctf}(X,A)$ ([thm-weil-pbc-site-comparison],
[lem-sf-proetale-constructible-origin], [det-pe-finite-tor-comparison-noetherian]). Finite-level
arguments may therefore be carried out on the small étale site.

*Integral and rational coefficients.* For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ the categories
$D^b_c(X,\Lambda)$ are the full subcategories of $D(X_{\mathrm{proét}},\Lambda)$ just defined,
and no other model of them is used. The pulled-back rings satisfy
$\mathcal O_{E,X}\cong\varprojlim_n(A_{E,n})_X$, $E_X\cong\mathcal O_{E,X}[1/\ell]$ and
$\overline{\mathbf Q}_{\ell,X}\cong\varinjlim_EE_X$ ([det-prop-sfb-qlbar-colimit-x-integral-limit],
[det-prop-sfb-qlbar-colimit-x-invert-ell], [def-sfb-qlbar-x-cocone]); these are
theorems about the condensed rings, not definitions. The following consequences are used in
proofs to reduce to finite levels.

1. A complex $K\in D(X_{\mathrm{proét}},\mathcal O_E)$ lies in $D^b_c(X,\mathcal O_E)$ if and
   only if it is derived $\pi_E$-complete and $K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(A_{E,1})_X$
   is in $D^b_c(X,A_{E,1})$; then every reduction
   $K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(A_{E,n})_X$ is in $D^b_c(X,A_{E,n})$, with
   cohomology in one interval independent of $n$, and $K\simeq R\varprojlim_nK_n$
   ([det-prop-integral-criterion-reductions]).
2. Extension of scalars along $\mathcal O_{E,X}\to E_X$ identifies $D^b_c(X,E)$ with the
   category obtained from $D^b_c(X,\mathcal O_E)$ by tensoring the Hom groups with $E$; in
   particular every object of $D^b_c(X,E)$ has an integral model
   ([thm-sfb-extend-scalars-localization], [def-sfb-rationalization-equivalence]).
3. Every object and every morphism of $D^b_c(X,\Qlb)$ is obtained by extension of scalars
   from some finite $E$, so that $D^b_c(X,\Qlb)\simeq2\text{-}\varinjlim_ED^b_c(X,E)$
   ([thm-sfb-constructible-cocone-two-colimit]).

For these three coefficient rings, finite Tor amplitude is automatic:
$D^b_{ctf}(X,\Lambda)=D^b_c(X,\Lambda)$; this is not part of the definition, see
[lem-integral-ctf-equals-bc]. For $\Lambda=\mathcal O_E$, an object $K$ of
$D^b_c(X,\mathcal O_E)$ is a finite extension of shifted sheaves $a_!C$, with
$a$ the inclusion of a stratum and $C$ of Tor amplitude in $[-1,0]$ on it
([det-lem-int-integral-heart-dualizable]). Hence $K$ has finite Tor amplitude, and its
reductions $K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(A_{E,j})_X$ lie in
$D^b_{ctf}(X,A_{E,j})$, with Tor amplitude in one interval independent of $j$.
