+++
id = "sk-cor-trace"
kind = "theorem"
title = "The trace isomorphism in top degree"
order = 524
lean = ["AlgebraicGeometry.WeilSheaf.exists_traceCup_isPerfect"]
uses = ["sk-def-trace-cup", "sk-lem-finite", "sk-lem-geo-cartier", "sk-prop-an", "sk-thm-purity-transport", "sk-thm-regular", "sk-thm-sf-identification", "sk-thm-smooth-purity", "sk-def-sp-trace", "sk-prop-scalar-six", "sk-def-ops", "sk-thm-derived-duality"]
tags = ["sketch"]
+++
Let $X/k$ be smooth, proper and connected of pure dimension
$d$, with $k$ algebraically closed. For every admissible
coefficient ring,

$$
H^i(X,\Lambda_X)=0\quad(i\notin[0,2d]),\qquad
H^0(X,\Lambda_X)=\Lambda,
$$

and the trace map $\operatorname{tr}_X$, the map induced on
$H^{2d}$ by $\operatorname{Tr}_X$ of Definition [sk-def-sp-trace]
and untwisted, is an isomorphism

$$
\operatorname{tr}_X:H^{2d}(X,\Lambda_X)
\xrightarrow{\sim}\Lambda(-d).
$$

For a geometric point $x:\operatorname{Spec}k\hookrightarrow X$,
the isomorphisms

$$
x^!\omega_X\simeq(a_Xx)^!\Lambda=\Lambda,
\qquad\omega_X\simeq\Lambda_X(d)[2d].
$$

turn the counit $x_*x^!\omega_X\to\omega_X$ for the closed point into a
map $\Lambda\to R\Gamma(X,\Lambda_X(d))[2d]$. The image
$[x]\in H^{2d}(X,\Lambda_X(d))$ of $1$ under this map satisfies
$\operatorname{tr}_X(d)([x])=1$.

*Complement.*

1. **(i)** The twisted trace $\operatorname{tr}_X(d):H^{2d}(X,\Lambda_X(d))\to\Lambda$
   is the map produced by the duality of [sk-thm-sf-identification] for
   $K=\Lambda_X$ in degree $0$: the isomorphism
   $H^{2d}(X,\Lambda_X(d))\simeq\Hom(R\Gamma(X,\Lambda_X),\Lambda)$ assembled from
   $Ra_{X!}\simeq Ra_{X*}$, the adjunction $a_X^*\dashv Ra_{X*}$, the isomorphism
   $\Lambda_X(d)[2d]\simeq\omega_X$ and the adjunction $Ra_{X!}\dashv a_X^!$,
   followed by evaluation at $1\in H^0(X,\Lambda_X)$.
2. **(ii)** The class $[x]$ is $(-1)^d$ times the image in $H^{2d}(X,\Lambda_X(d))$,
   by forgetting supports, of the fundamental class $[x\subset X]$ of the regular
   closed immersion $x$ of codimension $d$ ([sk-thm-regular], $c=d$); equivalently,
   the class in $H^{2d}_x(X,\Lambda_X(d))$ given by the image of $1$ in $x^!\omega_X$,
   of which $[x]$ is the image, is étale-locally at $x$, in coordinates
   $t_1,\dots,t_d$, the product $c_{V(t_1)}\cup\cdots\cup c_{V(t_d)}$ of the Cartier classes of the
   coordinate hyperplanes ([sk-lem-geo-cartier]), each $\partial\kappa(t_j)$ being
   $-c_{V(t_j)}$. Here $[x\subset X]$ is defined at
   $\Lambda=A_{E,n}$; at $\Oe$ it means the compatible system of the finite-level
   classes, and at $E$, $\Qlb$ its image under scalar extension.
3. **(iii)** For field coefficients the constant-coefficient pairings

   $$
   H^i(X,\Lambda)\times H^{2d-i}(X,\Lambda)
   \xrightarrow{\ \cup\ }H^{2d}(X,\Lambda)
   \xrightarrow{\operatorname{tr}_X}\Lambda(-d)
   $$

   (the trace–cup pairings of [sk-def-trace-cup]) are perfect, and graded
   commutativity gives
   $\langle y,x\rangle=(-1)^{i(2d-i)}\langle x,y\rangle=(-1)^i\langle x,y\rangle$.
   In particular the middle pairing has sign $(-1)^d$; over characteristic-zero
   coefficient fields it is alternating for odd $d$.
