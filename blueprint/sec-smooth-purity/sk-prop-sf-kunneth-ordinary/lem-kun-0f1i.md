+++
id = "lem-kun-0f1i"
kind = "lemma"
title = "Base change towards spectra of fields"
order = 2123
uses = ["def-kun-bc-property", "def-pc-separably-closed", "def-kun-torsion-invertible", "def-kun-unbounded-exchange", "def-weil-pbc-hypercohomology-filtrations", "def-weil-pbc-scheme-conventions", "lem-kun-0eys", "lem-kun-0f1c", "lem-kun-0f1d", "lem-kun-0f1i-normal", "lem-kun-bc-base-change", "lem-kun-bc-map-on-cohomology", "lem-kun-geometric-reduced-perfect", "lem-kun-invertible-orders-colimit", "lem-kun-sep-closure-conservative", "lem-kun-stalk-faithful-derived", "lem-kun-unbounded-exchange-agrees", "lem-kun-zn-sheaf-invertible-orders", "lemma-weil-pbc-direct-image-filtered-colimit", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $K$ be a field and let $X$ be a scheme of finite type over
$K$. For any commutative diagram

$$
\begin{array}{ccccc}
X&\longleftarrow&X'&\longleftarrow&Y\\
\Big\downarrow{\scriptstyle f}&&\Big\downarrow{\scriptstyle f'}&&\Big\downarrow{\scriptstyle h}\\
\Spec(K)&\longleftarrow&S'&\longleftarrow&T
\end{array}
$$

of schemes over $K$ with $X'=X\times_{\Spec(K)}S'$ and
$Y=X'\times_{S'}T$ and with $g:T\to S'$ quasi-compact and quasi-separated, and for every abelian sheaf $F$ on $T_{\Et}$ whose
stalks are torsion of orders invertible in $K$, the exchange
morphism

$$
(f')^{-1}Rg_*F\longrightarrow Rh_*e^{-1}F
$$

is an isomorphism.
