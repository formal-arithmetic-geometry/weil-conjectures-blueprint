+++
id = "fin2-lem-curve-family-betti"
kind = "lemma"
title = "The cohomology of the fibres of a family of curves"
order = 3222
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-sbc-normal-dominant-galois", "def-sbc-smooth-morphisms", "def-sc-genus", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-sc-cohomological-dimension", "sbc-def-coefficient-conventions", "thm-sc-proper-cohomology"]
+++
Let $f:X\to S$ be a
smooth proper morphism with $S$ of
finite type over $k$ and
geometrically connected
geometric fibres of
relative dimension one, let $n$ be an integer prime to
$\operatorname{char}k$, and let $\bar s$ be a
geometric point of $S$.
Then

$$
H^q\bigl((X_{\bar s})_{{\mathrm{et}}},\underline{\mathbf Z/n\mathbf Z}\bigr)\cong
\begin{cases}\mathbf Z/n\mathbf Z,&q=0,\\
(\mathbf Z/n\mathbf Z)^{2g_{\bar s}},&q=1,\\
\mathbf Z/n\mathbf Z,&q=2,\\
0,&q>2,\end{cases}
$$

where $g_{\bar s}$ is the genus
([def-sc-genus]) of the smooth proper curve $X_{\bar s}$ over the
algebraically closed field $\kappa(\bar s)$.

## Proof

The fibre $X_{\bar s}$ of the smooth proper
$f$ of [def-sbc-smooth-morphisms] at the algebraic
closure $\kappa(\bar s)$ is a smooth proper curve over the
algebraically closed field $\kappa(\bar s)$ of genus $g_{\bar s}$ in
the sense of [def-sc-genus], connectedness of the geometric
fibres being that of [def-sbc-normal-dominant-galois]. By
[cor-weil-pbc-geometric-fiber-finite], the finite-coefficient
geometric-fibre formula of the proper-base-change chapter (the proper morphism $f$ and
the constant finite sheaf), the fibre cohomology computes the stalk
of the higher direct images of [def-weil-pbc-direct-image]:

$$
H^q\bigl((X_{\bar s})_{{\mathrm{et}}},\underline{\mathbf Z/n\mathbf Z}\bigr)
=(R^qf_*\underline{\mathbf Z/n\mathbf Z})_{\bar s}.
$$

The displayed values are [thm-sc-proper-cohomology] applied to
the smooth proper curve $C=X_{\bar s}$ of genus $g_{\bar s}$ over the
algebraically closed $\kappa(\bar s)$ (with $n$ prime to
$\operatorname{char}k=\operatorname{char}\kappa(\bar s)$):
$H^0=\mathbf Z/n\mathbf Z$, $H^1=(\mathbf Z/n\mathbf Z)^{2g_{\bar s}}$,
$H^2=\mathbf Z/n\mathbf Z$, and the vanishing for $q>2$ is
lem:sc-cohomological-dimension.
