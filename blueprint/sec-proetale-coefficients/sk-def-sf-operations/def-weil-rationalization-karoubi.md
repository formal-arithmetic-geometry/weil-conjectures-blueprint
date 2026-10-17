+++
id = "def-weil-rationalization-karoubi"
kind = "definition"
title = "Rationalization (scalar localization)"
lean = ["AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructibleRational", "AlgebraicGeometry.Etale.derivedCompleteRationalScalarExtension"]
order = 1819
uses = ["def-weil-derived-complete-integral-detailed", "def-weil-derived-tensor", "def-weil-finite-field-fiber", "def-weil-finite-torsion-constructibility", "sk-def-sfb-condensed-ring", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-bounded-constructible", "sk-thm-sfb-rationalization-comparison", "sk-prop-sfb-finite-extension-compatibility"]
+++
For the global finite-field datum [def-weil-finite-field-fiber], fix a prime
$\ell\neq p$, a finite extension $E/\Ql$, a scheme $Y$, and a uniformizer
$\varpi_E$ of its valuation ring $\mathcal O_E$. The derived-complete
integral category [def-weil-derived-complete-integral-detailed] is
$D^b_c(Y,\mathcal O_E)$, built from the finite-torsion coefficients
[def-weil-finite-torsion-constructibility] $A_{E,n}=\mathcal
O_E/\varpi_E^n$. If $\mathcal C$ is an $\mathcal O_E$-linear triangulated
category, its rationalization $\mathcal C[1/\varpi_E]$ has the same objects
and, for $K,L\in\mathcal C$,

$$
 \Hom_{\mathcal C[1/\varpi_E]}(K,L)
 =\Hom_{\mathcal C}(K,L)\otimes_{\mathcal O_E}E.
$$

No Karoubi (idempotent) completion is taken in this construction: the notation
$\mathcal C[1/\varpi_E]$ denotes the raw scalar localization displayed above,
in which no idempotent is formally adjoined. For $E=\Ql$, this uses $\mathcal
O_E=\Zl$ and $\varpi_E=\ell$.

The rational coefficient category is the condensed one:
$D^b_c(Y,E)\subseteq D(Y_{\mathrm{proét}},E)$ is the category of bounded complexes of modules
over $E_Y=p_Y^*\underline E$ ([sk-def-sfb-condensed-ring],
[sk-def-sfb-pulled-back-coefficients]) with constructible cohomology sheaves
([sk-def-sfb-bounded-constructible]). For $Y$ of finite type over $k$, extension of scalars
$K\mapsto E_Y\otimes_{\mathcal O_{E,Y}}K$ induces an equivalence

$$
 D^b_c(Y,\mathcal O_E)[1/\varpi_E]\xrightarrow{\ \sim\ }D^b_c(Y,E)
$$

([sk-thm-sfb-rationalization-comparison]). Inverting $\varpi_E$ is the same as inverting
$\ell$, since $\ell$ is a unit times a power of $\varpi_E$. We identify the two categories
along this equivalence and write

$$
 D^b_c(Y,E)=
 D^b_c(Y,\mathcal O_E)[1/\varpi_E].
$$

So objects of $D^b_c(Y,E)$ may be represented by integral objects, and morphisms by
$\Hom_{D^b_c(Y,\mathcal O_E)}(K,L)\otimes_{\mathcal O_E}E$.

If $E\subset L$ is a finite extension, the scalar-extension functor is

$$
 -\otimes_E L:D^b_c(Y,E)\longrightarrow D^b_c(Y,L),
$$

the extension of scalars $L_Y\otimes_{E_Y}-$ along the morphism of condensed rings
$\underline E\to\underline L$ ([sk-prop-sfb-finite-extension-compatibility]). On integral
representatives it is the completed derived tensor product [def-weil-derived-tensor] with
$\mathcal O_L$, levelwise modulo powers of the two uniformizers, followed by
rationalization.
