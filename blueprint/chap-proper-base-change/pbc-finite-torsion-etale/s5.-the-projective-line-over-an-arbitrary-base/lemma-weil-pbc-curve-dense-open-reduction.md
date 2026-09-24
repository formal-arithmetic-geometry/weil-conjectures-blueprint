+++
id = "lemma-weil-pbc-curve-dense-open-reduction"
kind = "lemma"
title = "Dense-open localization reduction"
order = 1778
uses = ["lemma-weil-pbc-curve-constructible-primary-reduction", "lemma-weil-pbc-eight-curve-devissage"]
+++
Let $X$ be a reduced curve and $F$ a constructible $\mathbf F_\ell$-sheaf.
There is a dense open immersion $j:U\hookrightarrow X$ with
$U=\coprod_iU_i$ irreducible and $F|_U$ finite locally constant. If
$i:Z=X\setminus U\hookrightarrow X$, then

$$
0\longrightarrow j_!j^{-1}F\longrightarrow F
\longrightarrow i_*i^{-1}F\longrightarrow0
$$

reduces extension-invariance to $j_!G$ and to sheaves on the zero-dimensional
scheme $Z$.

## Proof

Constructibility gives a finite stratification. Remove the finite closed
strata and all intersections of distinct irreducible components. The
resulting $U=\coprod_aU_a$ meets every component, each $U_a$ is irreducible,
and $G=j^{-1}F$ is finite locally constant.

Let $\epsilon:j_!G\to F$ be extension by zero of the identity of $G$, and
let $\rho:F\to i_*i^{-1}F$ be restriction to $Z$. At a geometric point of
$U$, the stalks of $(\epsilon,\rho)$ are
$G_{\bar x}\xrightarrow{\mathrm{id}}F_{\bar x}\to0$; at a geometric point
of $Z$ they are $0\to F_{\bar z}\xrightarrow{\mathrm{id}}F_{\bar z}$.
Geometric stalks are exact and conservative, so

$$
0\longrightarrow j_!G\xrightarrow{\epsilon}F
\xrightarrow{\rho}i_*i^{-1}F\longrightarrow0
$$

is exact with the displayed maps.

The reduced zero-dimensional scheme $Z$ is a finite disjoint union of
$k$-points. Exact finite direct image and Leray give

$$
H^q(X,i_*i^{-1}F)=H^q(Z,i^{-1}F)=0\quad(q>0),\qquad
H^0(Z,i^{-1}F)=\bigoplus_{\bar z\in Z}F_{\bar z}.
$$

The last group is finite. The long exact sequence is therefore

$$
\begin{split}
0&\to H^0(X,j_!G)\to H^0(X,F)\to
\bigoplus_{\bar z\in Z}F_{\bar z}\\
&\to H^1(X,j_!G)\to H^1(X,F)\to0,
\end{split}
$$

and restriction induces $H^q(X,j_!G)\cong H^q(X,F)$ for $q>1$.

These maps separate the eight assertions as follows. Assertions (1)–(3)
and (8) use the isomorphisms in degrees at least two, also after replacing
$X$ by an open $W$ and $U$ by $W\cap U$. Assertions (4) and (5) use the
displayed five-term sequence and finiteness of the boundary-stalk sum.
For (6) and (7), base change preserves $Z$, its stalk groups, $\epsilon$,
$\rho$, and the boundary map; the two five-term sequences form a commuting
diagram, and the five lemma handles degrees $0,1$, while the higher-degree
maps are already identified. Thus the eight assertions hold for $F$ if
and only if they hold for $j_!G$.

Finally $j_!G=\bigoplus_a j_{a,!}(G|_{U_a})$. The inclusions and projections
split this finite sum, and repeated split exact sequences
$0\to E_1\to E_1\oplus E_2\to E_2\to0$ together with short-exact devissage
reduce to the individual irreducible components.
