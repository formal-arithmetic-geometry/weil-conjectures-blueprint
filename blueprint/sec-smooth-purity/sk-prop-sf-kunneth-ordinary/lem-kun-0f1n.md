+++
id = "lem-kun-0f1n"
kind = "lemma"
title = "Base change for pushforward tensored with an arbitrary complex"
lean = ["AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap"]
order = 2125
uses = ["def-kun-derived-tensor", "def-kun-tor-amplitude", "def-kun-truncations", "def-kun-unbounded-exchange", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "lem-kun-0f10", "lem-kun-0f11", "lem-kun-0f1j", "lem-kun-bounded-flat-replacement", "lem-kun-complex-colimit-hocolim", "lem-kun-derived-tensor-direct-sums", "lem-kun-flat-bounded-tor-amplitude", "lem-kun-functor-preserves-hocolim", "lem-kun-hocolim-truncations"]
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

of schemes of finite type over $K$ with
$X'=X\times_{\Spec(K)}S'$ and $Y=X'\times_{S'}T$. The canonical
map

$$
p^{-1}E\kunotimes{\kunZn}(f')^{-1}Rg_*F
\longrightarrow
Rh_*\bigl(h^{-1}p^{-1}E\kunotimes{\kunZn}e^{-1}F\bigr)
$$

is an isomorphism for all $E\in D(X_{\Et},\kunZn)$ and
$F\in D(T_{\Et},\kunZn)$.
