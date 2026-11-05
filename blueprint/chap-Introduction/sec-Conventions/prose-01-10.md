+++
id = "prose-01-10"
kind = "hidden"
title = "Conventions"
order = 21
+++
We fix a prime $\ell$ and a field $k$ that is finite or algebraically
closed, of characteristic different from $\ell$. Unless said otherwise,
schemes are separated and of finite type over $k$, and morphisms are
$k$-morphisms. The hypothesis on $k$ is needed to bound the
$\ell$-cohomological dimension of $k$
(Lemma [lemma-cohomological-dimension-base-field]), while the constructions of
Sections [sec-Coefficient-rings] and [sec-Derived-functors] make sense for arbitrary
schemes. Finally, a citation such as [Stacks, [0F0C](https://stacks.math.columbia.edu/tag/0F0C)] refers to the tag of a result in the
Stacks Project [stacks].

On the pro-étale site we regard every coefficient ring $\Lambda$ as a
condensed ring, that is, as a sheaf of rings on profinite sets, which
remembers the topology of $\Lambda$. (On the étale site, which we use only
with finite coefficients, a finite ring is simply a ring.) The coefficient sheaf $\Lambda_X$ on $X$ is then the pullback
of $\Lambda$ along the map from $X$ to a point
(Section [sec-Coefficient-rings]). For a finite ring $A$ this pullback
is the classical constant sheaf.

Derived categories are the classical ones. Namely, $D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is
the derived category of the abelian category of sheaves of
$\Lambda_X$-modules. On these categories all functors are derived, and we write them $f^*$,
$Rf_*$, $Rf_!$ and $f^!$. Unless another category is named, we have
$f^*:D(Y_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ and
$Rf_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$, whereas the
categories on which $Rf_!$ and $f^!$ act are fixed where these functors
are defined. To avoid set-theoretic problems, we take sizes with respect to a fixed universe that is large
enough to contain the w-contractible covers of
Theorem [theorem-existence-contractible-covers].

The table below lists the main notation, together with the technical terms
(lisse, Weil structure, pure, mixed, real) whose meaning in these notes is
fixed by a definition, and the place where each is defined. The Frobenius $F$ of the Introduction, which raises
coordinates to their $q$-th powers, is written $\Phi_X$ in the body of the
notes. A Frobenius structure $F^*K\simeq K$ becomes there a Weil structure
$\operatorname{Fr}_X^*K\simeq K$ for the geometric Frobenius
$\operatorname{Fr}_X$, and
Lemma [lemma-scheme-frobenius-geometric-frobenius] shows that the two
give the same operators.

**Notation**

| symbol | meaning | defined in |
|---|---|---|
| $X_{\mathrm{pro}\acute{e}t}$ | the pro-étale site | [definition-small-pro-etale-site] |
| $\Lambda_X$, $\Lambda_X(d)$ | coefficient sheaf, Tate twists | [definition-tate-twists] |
| $\Dbc(X,\Lambda)$, $D^b_{\mathrm{ctf}}(X,\Lambda)$ | constructible complexes | [definition-constructible-sheaves] |
| lisse | locally of constant finite presentation | [definition-lisse-sheaves] |
| $K_n$ | reduction modulo $\pi_E^n$ | [definition-derived-adic-completeness] |
| $\operatorname{cd}_\ell$ | cohomological dimension | [definition-cohomological-dimension] |
| $R\underline\Gamma_Z$ | local cohomology | [definition-local-cohomology] |
| $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ | localizing subcategory | [definition-localizing-subcategory] |
| $Rf_!$, $f^!$ | exceptional operations | [theorem-exceptional-inverse-image] |
| $\omega_f$ | relative dualizing complex | [definition-relative-dualizing-complex] |
| $\operatorname{Tr}_f$ | trace map | [definition-trace-map] |
| $\mathbb D_X$ | Verdier dual | [definition-verdier-dual-evaluation] |
| $\operatorname{Fr}_X$, Weil structure | geometric Frobenius, $\operatorname{Fr}_X^*K\simeq K$ | [definition-weil-structure] |
| $\Phi_X$ | $q$-power Frobenius | [definition-frobenius-correspondences-their-operators] |
| $c$, $\Fix(c)$ | correspondences | [definition-correspondence] |
| $T_c(u)$ | action of a correspondence | [definition-action-correspondence] |
| $\operatorname{Tr}_c(u)$, $\operatorname{LT}$ | trace class, local terms | [definition-trace-class-local-terms] |
| pure, mixed | $\iota$-weights | [definition-weights] |
| $\operatorname{dw}_\iota$ | determinant weight | [definition-determinant-weight] |
| real | real Weil sheaves | [definition-real-sheaves] |
| $j_*\mathcal F$ | middle extension | [definition-middle-extension] |
| $\operatorname{FT}_\psi$ | Fourier transform | Section [chap-The-Fourier-transform] |
| $T_\ell A$, $V_\ell A$ | Tate module | [definition-tate-module] |
