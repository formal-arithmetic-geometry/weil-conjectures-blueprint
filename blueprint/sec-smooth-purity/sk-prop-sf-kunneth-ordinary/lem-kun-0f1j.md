+++
id = "lem-kun-0f1j"
kind = "lemma"
title = "Base change for pushforward tensored with a bounded-below complex of finite tor amplitude"
lean = ["AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_of_isGE"]
order = 3161
uses = ["def-kun-derived-tensor", "def-kun-tor-amplitude", "def-kun-truncations", "def-kun-unbounded-exchange", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-kun-03sa", "lem-kun-095r", "lem-kun-0f0g", "lem-kun-0f1i", "lem-kun-0f1m", "lem-kun-bc-base-change", "lem-kun-change-of-rings-tensor", "lem-kun-constant-constructible", "lem-kun-derived-tensor-t-est", "lem-kun-derived-tensor-triangulated", "lem-kun-kflat-criteria", "lem-kun-leray-finite", "lem-kun-proj-formula-natural", "lem-kun-stalk-faithful-derived", "lem-kun-tensor-t-est", "lem-kun-zn-sheaf-invertible-orders", "lemma-weil-pbc-constructible-finite-pushforward", "lemma-weil-pbc-direct-image-filtered-colimit", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-exchange", "thm-constructible-serre"]
+++
Let $K$ be a field and $n\ge1$ an integer invertible in $K$.
Consider a commutative diagram

$$
\begin{array}{ccccc}
X&\xleftarrow{\;p\;}&X'&\xleftarrow{\;h\;}&Y\\
\Big\downarrow{}&&\Big\downarrow{\scriptstyle f'}&&\Big\downarrow{\scriptstyle e}\\
\Spec(K)&\longleftarrow&S'&\xleftarrow{\;g\;}&T
\end{array}
$$

of schemes with $X$ of finite type over $K$, with $X'=X\times_{\Spec(K)}S'$ and
$Y=X'\times_{S'}T$, and with $g$ quasi-compact and
quasi-separated. (The finite-type hypothesis on $X$ is used in the proof,
which applies [lem-kun-0f1i], stated for schemes of finite type over $K$,
to the finite $X$-schemes $X_i$.) The canonical map

$$
p^{-1}E\kunotimes{\kunZn}(f')^{-1}Rg_*F
\longrightarrow
Rh_*\bigl(h^{-1}p^{-1}E\kunotimes{\kunZn}e^{-1}F\bigr)
$$

(adjoint to the map
$h^{-1}p^{-1}E\kunotimes{\kunZn}e^{-1}g^{-1}Rg_*F\to h^{-1}p^{-1}E\kunotimes{\kunZn}e^{-1}F$
induced by the counit of [def-weil-pbc-inverse-image]) is an
isomorphism for every $E\in\Dplus(X_{\Et},\kunZn)$ of
tor amplitude in $[a,\infty)$ for
some $a\in\mathbf Z$ and every $F\in\Dplus(T_{\Et},\kunZn)$.
