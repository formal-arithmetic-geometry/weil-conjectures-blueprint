+++
id = "lem-trf-frobenius-open-square"
kind = "lemma"
title = "Frobenius preserves an open subscheme defined over the finite field"
order = 2706
uses = ["def-trf-scheme-frobenius", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties"]
+++
Fix the finite-field datum.
Let $j_0:X_0\hookrightarrow Y_0$ be an
open immersion
over $k_0=\mathbf F_q$, and let $j:X\hookrightarrow Y$
be its base change to $k$. For the
scheme and Galois Frobenii,
each square

$$
\begin{array}{ccc}
X&\xrightarrow{h}&X\\
{\scriptstyle j}\downarrow&&\downarrow{\scriptstyle j}\\
Y&\xrightarrow{\bar h}&Y
\end{array}
$$

is Cartesian, where $(h,\bar h)=(\Phi_X^m,\Phi_Y^m)$ or
$(g_X^m,g_Y^m)$, and $m\geq0$. With
$s=\Spec k$, $g_s=\Spec(\gamma)$, and structure maps $a_X,a_Y$,

$$
a_Xg_X^m=g_s^ma_X,\qquad a_Yg_Y^m=g_s^ma_Y.
$$

In particular these Galois maps are not asserted to be $k$-morphisms.
