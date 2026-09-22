+++
id = "fin2-lem-curve-family-betti"
kind = "lemma"
title = "The cohomology of the fibres of a family of curves"
order = 5179
lean = ["AlgebraicGeometry.Etale.cohomology_fiber_of_smoothProper_curve_family"]
uses = ["def-sbc-smooth-morphisms", "def-sbc-normal-dominant-galois", "sbc-def-coefficient-conventions"]
+++
Let $f:X\to S$ be a smooth proper [def-sbc-smooth-morphisms] morphism with
$S$ of finite type over $k$ and geometrically connected
[def-sbc-normal-dominant-galois] geometric fibres of relative dimension one,
let $n$ be an integer prime to $\operatorname{char}k$, and let $\bar s$ be a
geometric point of $S$. Then
$$
H^q\bigl((X_{\bar s})_{\Et},\underline{\mathbf Z/n\mathbf Z}\bigr)\cong
\begin{cases}\mathbf Z/n\mathbf Z,&q=0,\\
(\mathbf Z/n\mathbf Z)^{2g_{\bar s}},&q=1,\\
\mathbf Z/n\mathbf Z,&q=2,\\
0,&q>2,\end{cases}
$$
where $g_{\bar s}$ is the genus of the smooth proper curve $X_{\bar s}$ over
the algebraically closed field $\kappa(\bar s)$.

## Proof

The fibre $X_{\bar s}$ of the smooth proper $f$ at the algebraic closure
$\kappa(\bar s)$ is a smooth proper curve over the algebraically closed
field $\kappa(\bar s)$ of genus $g_{\bar s}$, connectedness of the geometric
fibres being that of [def-sbc-normal-dominant-galois]. By the
finite-coefficient geometric-fibre formula of the proper-base-change chapter
(the proper morphism $f$ and the constant finite sheaf), the fibre
cohomology computes the stalk of the higher direct images:
$$
H^q\bigl((X_{\bar s})_{\Et},\underline{\mathbf Z/n\mathbf Z}\bigr)
=(R^qf_*\underline{\mathbf Z/n\mathbf Z})_{\bar s}.
$$

The displayed values are the Kummer computation on a proper curve applied to
$C=X_{\bar s}$ of genus $g_{\bar s}$ over the algebraically closed
$\kappa(\bar s)$ (with $n$ prime to
$\operatorname{char}k=\operatorname{char}\kappa(\bar s)$):
$H^0=\mathbf Z/n\mathbf Z$,
$H^1=(\mathbf Z/n\mathbf Z)^{2g_{\bar s}}$, $H^2=\mathbf Z/n\mathbf Z$, and
the vanishing for $q>2$ is the cohomological-dimension bound for a smooth
curve.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-geometric-stalks, def:sc-genus, cor:weil-pbc-geometric-fiber-finite, def:weil-pbc-direct-image, thm:sc-proper-cohomology, lem:sc-cohomological-dimension
