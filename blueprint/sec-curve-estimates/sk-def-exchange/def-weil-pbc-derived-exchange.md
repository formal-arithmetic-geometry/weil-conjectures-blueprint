+++
id = "def-weil-pbc-derived-exchange"
kind = "definition"
title = "Derived exchange map"
order = 1322
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-sp-kinjective-bridge", "def-weil-pbc-underived-exchange"]
+++
Let $\mathcal A$ be a Grothendieck abelian category for which $\mathcal A$-valued
sheaves on small étale sites admit sheafification, and let $\square$ be a
commutative square $f\circ g'=g\circ f'$ of schemes as in
[def-weil-pbc-underived-exchange] (for instance a cartesian square
[def-weil-pbc-cartesian-square]). The inverse images $g^{-1}$, $g'^{-1}$ are
exact and induce functors on the bounded below derived categories
[def-weil-pbc-derived-categories] of $\mathcal A$-valued étale sheaves, and the
direct images [def-weil-pbc-direct-image] have right derived functors
$Rf_*$, $Rf'_*$ on $\Dplus$.

The *derived exchange morphism* is the natural transformation

$$
 \Ex_{\square}:g^{-1}Rf_*\longrightarrow Rf'_*g'^{-1}
$$

of functors $\Dplus(X_{\Et},\mathcal A)\to\Dplus(Y'_{\Et},\mathcal A)$
characterized by the universal property of the right derived functor
$g^{-1}Rf_*$ of $g^{-1}f_*$: it is the unique natural transformation such that,
for every bounded below complex $K$ of $\mathcal A$-valued sheaves on $X_{\Et}$,
the composite

$$
 g^{-1}f_*K\xrightarrow{g^{-1}(\eta_K)}g^{-1}Rf_*K
 \xrightarrow{\Ex_{\square,K}}Rf'_*g'^{-1}K
$$

equals the termwise underived exchange morphism
[def-weil-pbc-underived-exchange]
$\Ex^0_{\square,K}:g^{-1}f_*K\to f'_*g'^{-1}K$ followed by the canonical map
$f'_*g'^{-1}K\to Rf'_*g'^{-1}K$; here $\eta_K:f_*K\to Rf_*K$ is the canonical
map. In particular, if $K\xrightarrow{\simeq}I^\bullet$ is an injective
(K-injective [def-sp-kinjective-bridge]) resolution, so that
$f_*I^\bullet$ computes $Rf_*K$, then $\Ex_{\square,K}$ is represented by
$\Ex^0_{\square,I^\bullet}:g^{-1}f_*I^\bullet\to f'_*g'^{-1}I^\bullet$
followed by $f'_*g'^{-1}I^\bullet\to Rf'_*g'^{-1}I^\bullet$; concretely,
choosing a K-injective replacement $g'^{-1}I^\bullet\xrightarrow{\simeq}J^\bullet$
on $X'_{\Et}$, it is the class in $\Dplus(Y'_{\Et},\mathcal A)$ of

$$
 g^{-1}f_*I^\bullet\xrightarrow{\Ex^0_{\square,I^\bullet}}f'_*g'^{-1}I^\bullet
 \longrightarrow f'_*J^\bullet,
$$

whose source is a model of $g^{-1}Rf_*K$ (as $g^{-1}$ is exact) and whose
target is a model of $Rf'_*g'^{-1}K$ (as $J^\bullet$ is K-injective).

Equivalently, $\Ex_{\square,K}$ is the adjoint mate, under the derived
adjunction $f'^{-1}\dashv Rf'_*$, of the composite

$$
 f'^{-1}g^{-1}Rf_*K\xrightarrow{\theta_\square}
 g'^{-1}f^{-1}Rf_*K\xrightarrow{g'^{-1}\varepsilon_f}g'^{-1}K,
$$

where $\theta_\square$ is the square isomorphism of
[def-weil-pbc-underived-exchange] and $\varepsilon_f$ is the counit of the
derived adjunction $f^{-1}\dashv Rf_*$ induced by the inverse-image adjunction
[def-weil-pbc-inverse-image].
