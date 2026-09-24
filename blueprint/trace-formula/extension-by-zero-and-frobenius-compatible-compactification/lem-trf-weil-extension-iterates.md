+++
id = "lem-trf-weil-extension-iterates"
kind = "lemma"
title = "Iterates of the Weil extension by zero"
order = 3941
uses = ["def-trf-iterated-weil-map", "def-trf-weil-extension-zero", "def-weil-derived-pullback-tensor-hom", "def-weil-extension-by-zero", "lem-trf-absolute-frobenius-site", "lem-trf-iterated-weil-cocycle", "lem-trf-open-square-exchange", "lem-trf-weil-extension-strict", "prop-trf-scheme-galois-comparison"]
+++
Use the Weil extension by zero
$(\bar K,\bar\varphi)$ of $(K,\varphi)$, which is a strict Weil
complex by [lem-trf-weil-extension-strict]. For $m\geq1$, the
iterated Weil and scheme-Frobenius
maps satisfy

$$
\bar\varphi^{[m]}=j_!\varphi^{[m]}\circ b_{g_Y^m},
\qquad
\bar u_m=j_!u_m\circ b_{\Phi_Y^m}.
$$

The equalities use the canonical
pullback
identifications for composite maps.

## Proof

For $m=1$ the first formula is
[def-trf-weil-extension-zero]. The pair
$(\bar K,\bar\varphi)$ is a strict Weil complex by
[lem-trf-weil-extension-strict], so the iterates of
[def-trf-iterated-weil-map] apply to it. If the formula holds at
$m$, use the
cocycle formula of [lem-trf-iterated-weil-cocycle] for $m+1$.
Naturality of $b_g$ moves $j_!\varphi^{[m]}$ through the next
pullback; the pasting identity of
[lem-trf-open-square-exchange] combines the two open-square
comparisons into $b_{g_Y^{m+1}}$. What remains on $X$ is
$\varphi\circ Lg_X^*\varphi^{[m]}=\varphi^{[m+1]}$.
This proves the first formula by induction.

The comparison $\kappa^{(m)}$ in
[prop-trf-scheme-galois-comparison] comes from the canonical
relative-Frobenius maps of
[lem-trf-absolute-frobenius-site]. These restrict to the same
maps on $X$. It follows that the square

$$
\begin{array}{ccc}
L\Phi_Y^{m*}j_!K&\xrightarrow{\kappa^{(m)}_{j_!K}}
&Lg_Y^{m*}j_!K\\
{\scriptstyle b_{\Phi_Y^m}}\downarrow&&
\downarrow{\scriptstyle b_{g_Y^m}}\\
j_!L\Phi_X^{m*}K&\xrightarrow{j_!\kappa^{(m)}_K}
&j_!Lg_X^{m*}K
\end{array}
$$

commutes. More explicitly, use the two vertical isomorphisms to
view both composites as maps between extensions by zero.
The functor $j_!$ is fully faithful by the open localization
adjunction in [def-weil-extension-by-zero]. Equality may
therefore be checked after restriction to $X$, where the maps
are precisely the same relative-Frobenius comparison. Compose
this square with $j_!\varphi^{[m]}$ and use the first formula.
Since $u_m=\varphi^{[m]}\kappa^{(m)}_K$, this gives the second
formula.
