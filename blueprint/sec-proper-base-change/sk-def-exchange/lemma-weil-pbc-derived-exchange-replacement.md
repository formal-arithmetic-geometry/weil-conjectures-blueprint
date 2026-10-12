+++
id = "lemma-weil-pbc-derived-exchange-replacement"
kind = "lemma"
title = "Derived exchange replacement independence"
order = 1043
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_ext", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_fac_app"]
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-underived-exchange", "lem-weil-pbc-derived-exchange-termwise", "lemma-weil-pbc-underived-exchange-naturality"]
+++
Let $\square$ be a commutative square of schemes and $\mathcal A$ a coefficient
category as in [def-weil-pbc-derived-exchange]. For every bounded below
complex $K$ of $\mathcal A$-valued sheaves on $X_{\Et}$, the composite

$$
 g^{-1}f_*K\xrightarrow{g^{-1}(\eta_K)}g^{-1}Rf_*K
 \xrightarrow{\Ex_{\square,K}}Rf'_*g'^{-1}K
$$

of the derived exchange morphism [def-weil-pbc-derived-exchange] with
$g^{-1}$ of the canonical map $\eta_K:f_*K\to Rf_*K$ equals the termwise
underived exchange morphism [def-weil-pbc-underived-exchange]
$\Ex^0_{\square,K}:g^{-1}f_*K\to f'_*g'^{-1}K$ followed by the canonical map
$f'_*g'^{-1}K\to Rf'_*g'^{-1}K$. Conversely, every natural transformation
$g^{-1}Rf_*\to Rf'_*g'^{-1}$ on $\Dplus(X_{\Et},\mathcal A)$ satisfying this
identity for every bounded below complex $K$ equals $\Ex_{\square}$. In
particular, if $K$ is a bounded below complex of injectives
[def-weil-pbc-kinjective-resolutions], $\Ex_{\square,K}$ is computed by the
termwise underived exchange morphism, independently of any choices.
