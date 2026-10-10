+++
id = "lemma-weil-pbc-finite-exchange"
kind = "lemma"
title = "Finite exchange isomorphism"
order = 1121
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite", "AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite"]
uses = ["def-kun-separably-closed", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-geometric-fibre", "def-weil-pbc-property", "def-weil-pbc-scheme-conventions", "def-weil-pbc-underived-exchange", "lemma-openclosed-point-ulift", "lemma-openclosed-stalk-upperstar", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let the coefficient category $\mathcal A$ be concrete, with forgetful
functor reflecting isomorphisms and preserving filtered colimits, and with
sheafification on small étale sites compatible with the forgetful functor.
Consider a cartesian square

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y
\end{array}
$$

with $f$ finite and $g$ arbitrary. Then the underived exchange map

$$
 g^{-1}f_*F\xrightarrow{\sim}f'_*g'^{-1}F
$$

is an isomorphism for every sheaf $F$ on $X_{\Et}$, and the derived exchange
morphism [def-weil-pbc-derived-exchange]
$g^{-1}Rf_*K\to Rf'_*g'^{-1}K$ is an isomorphism for every $K\in\Dplus(X_{\Et})$.
