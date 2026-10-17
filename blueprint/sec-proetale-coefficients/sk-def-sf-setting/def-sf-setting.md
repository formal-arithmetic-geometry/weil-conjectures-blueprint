+++
id = "def-sf-setting"
kind = "definition"
title = "Coefficients and sites"
order = 1811
uses = ["sk-def-sfb-condensed-ring", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-derived-categories", "sk-def-sfb-constructible", "sk-def-sfb-bounded-constructible", "sk-def-sp-tate-twist", "sk-prop-sf-comparison", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-sfb-rationalization-comparison"]
lean = ["AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible", "AlgebraicGeometry.Etale.DerivedCategory.boundedConstructibleFiniteTor", "AlgebraicGeometry.Etale.constantComplex"]
+++
Fix the global finite-field datum $(p,a,q,k_0,k)$ with $k=\overline{\mathbf F}_q$, a prime $\ell\neq p$, a finite extension $E/\Ql$ inside $\Qlb$ with valuation ring
$\mathcal O_E$ and uniformizer $\varpi_E$ (the $\pi_E$ of [sk-def-sfb-condensed-ring]), an integer $n\ge1$, and put
$A_{E,n}=\mathcal O_E/\varpi_E^n$. The *coefficient stages* are the admissible coefficient rings
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as condensed rings: $A_{E,n}$ with its
discrete topology, $\underline{\mathcal O}_E$ and $\underline E$ ([sk-def-sfb-condensed-ring]), and
$\underline{\Qlb}$ ([sk-def-sfb-qlbar-condensed]). For a scheme $X$ the coefficient sheaf is
$\Lambda_X=p_X^*\Lambda$ on $X_{\mathrm{proét}}$ ([sk-def-sfb-pulled-back-coefficients]); it is the
unit of $\otimes^L_{\Lambda}$, and $D(X,\Lambda)=D(X_{\mathrm{proét}},\Lambda)$ is the derived
category of $\Lambda_X$-modules ([sk-def-sfb-derived-categories]). $D^b_c(X,\Lambda)\subseteq
D(X_{\mathrm{proét}},\Lambda)$ consists of the bounded complexes with constructible cohomology
sheaves ([sk-def-sfb-constructible], [sk-def-sfb-bounded-constructible]), and
$D^b_{ctf}(X,\Lambda)\subseteq D^b_c(X,\Lambda)$ of those of finite Tor amplitude. The stages
come with constructible intervals and the Tate twists of [sk-def-sp-tate-twist].
Morphisms are separated of finite type.

*Finite stage.* For $\Lambda=A=A_{E,n}$ the sheaf $A_X$ is the classical constant sheaf, and
$\nu_X^*$ identifies the étale categories with the pro-étale ones: $D^b_c(X_{\mathrm{ét}},A)$,
the bounded complexes of sheaves of $A$-modules on the small étale site with constructible
cohomology sheaves, and its subcategory $D^b_{ctf}(X_{\mathrm{ét}},A)$, are carried
equivalently onto $D^b_c(X,A)$ and $D^b_{ctf}(X,A)$ ([sk-prop-sf-comparison],
[sk-thm-pe-constructible-comparison], [sk-cor-pe-finite-tor-comparison]). Finite-stage
arguments may therefore be carried out on the small étale site.

*Adic stages.* The pulled-back rings satisfy $\mathcal O_{E,X}\cong\varprojlim_n(A_{E,n})_X$,
$E_X\cong\mathcal O_{E,X}[1/\ell]$ and $\overline{\mathbf Q}_{\ell,X}\cong\varinjlim_EE_X$
([sk-prop-sfb-qlbar-colimit-x]). These are theorems, not definitions. Through them, the
integral criterion ([sk-prop-integral-criterion]), the rationalization comparison
([sk-thm-sfb-rationalization-comparison]) and descent to a finite coefficient field
([sk-thm-sfb-qlbar-two-colimit]) identify $D^b_c(X,\mathcal O_E)$, $D^b_c(X,E)$ and
$D^b_c(X,\Qlb)$ with the derived-complete integral category
([def-weil-derived-complete-integral-detailed]), the rationalized category
([def-weil-rationalization-karoubi]) and the common-stage category
([def-weil-algebraically-closed-coefficients]). Later sections use these as working
models.
