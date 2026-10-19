+++
id = "def-sf-setting"
kind = "definition"
title = "Coefficients and sites"
order = 1811
uses = ["sk-def-sfb-condensed-ring", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-derived-categories", "sk-def-sfb-constructible", "sk-def-sfb-bounded-constructible", "sk-def-sp-tate-twist", "sk-prop-sf-comparison", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-sfb-rationalization-comparison"]
lean = ["AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible", "AlgebraicGeometry.Etale.DerivedCategory.boundedConstructibleFiniteTor", "AlgebraicGeometry.Etale.constantComplex"]
+++
Fix the global finite-field datum $(p,a,q,k_0,k)$ with $k=\overline{\mathbf F}_q$, a prime $\ell\neq p$, a finite extension $E/\Ql$ inside $\Qlb$ with valuation ring
$\mathcal O_E$ and uniformizer $\pi_E$ ([sk-def-sfb-condensed-ring]), an integer $n\ge1$, and put
$A_{E,n}=\mathcal O_E/\pi_E^n$. The admissible coefficient rings are
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as condensed rings: $A_{E,n}$ with its
discrete topology, $\underline{\mathcal O}_E$ and $\underline E$ ([sk-def-sfb-condensed-ring]), and
$\underline{\Qlb}$ ([sk-def-sfb-qlbar-condensed]). For a scheme $X$ the coefficient sheaf is
$\Lambda_X=p_X^*\Lambda$ on $X_{\mathrm{proét}}$ ([sk-def-sfb-pulled-back-coefficients]); it is the
unit of $\otimes^L_{\Lambda}$, and $D(X,\Lambda)=D(X_{\mathrm{proét}},\Lambda)$ is the derived
category of $\Lambda_X$-modules ([sk-def-sfb-derived-categories]). $D^b_c(X,\Lambda)\subseteq
D(X_{\mathrm{proét}},\Lambda)$ consists of the bounded complexes with constructible cohomology
sheaves ([sk-def-sfb-constructible], [sk-def-sfb-bounded-constructible]), and
$D^b_{ctf}(X,\Lambda)\subseteq D^b_c(X,\Lambda)$ of those of finite Tor amplitude over
$\Lambda_X$. These categories come with constructible intervals and the Tate twists of
[sk-def-sp-tate-twist]. Morphisms are separated of finite type.

*Finite coefficients.* For $\Lambda=A=A_{E,n}$ the sheaf $A_X$ is the classical constant sheaf, and
$\nu_X^*$ identifies the étale categories with the pro-étale ones: $D^b_c(X_{\mathrm{ét}},A)$,
the bounded complexes of sheaves of $A$-modules on the small étale site with constructible
cohomology sheaves, and its subcategory $D^b_{ctf}(X_{\mathrm{ét}},A)$, are carried
equivalently onto $D^b_c(X,A)$ and $D^b_{ctf}(X,A)$ ([sk-prop-sf-comparison],
[sk-thm-pe-constructible-comparison], [sk-cor-pe-finite-tor-comparison]). Finite-level
arguments may therefore be carried out on the small étale site.

*Integral and rational coefficients.* For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ the categories
$D^b_c(X,\Lambda)$ are the full subcategories of $D(X_{\mathrm{proét}},\Lambda)$ just defined,
and no other model of them is used. The pulled-back rings satisfy
$\mathcal O_{E,X}\cong\varprojlim_n(A_{E,n})_X$, $E_X\cong\mathcal O_{E,X}[1/\ell]$ and
$\overline{\mathbf Q}_{\ell,X}\cong\varinjlim_EE_X$ ([sk-prop-sfb-qlbar-colimit-x]); these are
theorems about the condensed rings, not definitions. The following consequences are used in
proofs to reduce to finite levels.

1. A complex $K\in D(X_{\mathrm{proét}},\mathcal O_E)$ lies in $D^b_c(X,\mathcal O_E)$ if and
   only if it is derived $\pi_E$-complete and $K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(A_{E,1})_X$
   is in $D^b_c(X,A_{E,1})$; then every reduction
   $K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(A_{E,n})_X$ is in $D^b_c(X,A_{E,n})$, with
   cohomology in one interval independent of $n$, and $K\simeq R\varprojlim_nK_n$
   ([sk-prop-integral-criterion], [det-prop-integral-criterion-reductions]).
2. Extension of scalars along $\mathcal O_{E,X}\to E_X$ identifies $D^b_c(X,E)$ with the
   category obtained from $D^b_c(X,\mathcal O_E)$ by tensoring the Hom groups with $E$; in
   particular every object of $D^b_c(X,E)$ has an integral model
   ([sk-thm-sfb-rationalization-comparison]).
3. Every object and every morphism of $D^b_c(X,\Qlb)$ is obtained by extension of scalars
   from some finite $E$, so that $D^b_c(X,\Qlb)\simeq2\text{-}\varinjlim_ED^b_c(X,E)$
   ([sk-thm-sfb-qlbar-two-colimit]).

For these three coefficient rings, finite Tor amplitude is automatic:
$D^b_{ctf}(X,\Lambda)=D^b_c(X,\Lambda)$ ([det-def-localizing-closure-ctf-equals-bc]).
