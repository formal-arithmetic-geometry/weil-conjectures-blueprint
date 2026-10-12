+++
id = "lem-kun-kunneth-map-natural"
kind = "lemma"
title = "Naturality of the Kunneth map"
order = 2045
uses = ["def-kun-kunneth-map", "def-weil-pbc-cartesian-square", "def-weil-pbc-inverse-image"]
+++
Let

$$
\begin{array}{ccc}
X\times_SY&\xrightarrow{\;q\;}&Y\\
\Big\downarrow{\scriptstyle p}&&\Big\downarrow{\scriptstyle g}\\
X&\xrightarrow{\;f\;}&S
\end{array}
$$

be a cartesian square, $\Lambda$ a commutative ring, and let
$E\to E'$ and $K\to K'$ be morphisms in
$D(X_{\Et},\Lambda)$, respectively $D(Y_{\Et},\Lambda)$. Then the
square

$$
\begin{array}{ccc}
Rf_*E\kunotimes{\Lambda}Rg_*K&\xrightarrow{\ \kappa_{E,K}\ }&
Rc_*\bigl(p^{-1}E\kunotimes{\Lambda}q^{-1}K\bigr)\\
\Big\downarrow{\scriptstyle Rf_*(\varphi)\otimes Rg_*(\psi)}&&
\Big\downarrow{\scriptstyle Rc_*(p^{-1}\varphi\otimes q^{-1}\psi)}\\
Rf_*E'\kunotimes{\Lambda}Rg_*K'&\xrightarrow{\ \kappa_{E',K'}\ }&
Rc_*\bigl(p^{-1}E'\kunotimes{\Lambda}q^{-1}K'\bigr)
\end{array}
$$

commutes; that is, $\kappa$ is natural in $E$ and in $K$.
