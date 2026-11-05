+++
id = "prose-01-02"
kind = "hidden"
title = "The Weil conjectures"
order = 5
+++
Let $X_0$ be a smooth projective geometrically connected curve of genus
$g$ over the finite field $\mathbf F_q$, and let $N_m$ be the number of
its points with coordinates in $\mathbf F_{q^m}$. The projective line has
exactly $1+q^m$ such points, and the *Hasse–Weil bound* says that
every curve of genus $g$ comes close to this count:

$$
|N_m-(1+q^m)|\le 2g\,q^{m/2}.
$$

Hasse proved it for elliptic curves [hasse36] and Weil for all
curves [weil48-courbes].

To state Weil's conjectures in higher dimension we put all the numbers
$N_m$ into one generating function. For a separated scheme $X_0$ of
finite type over $\mathbf F_q$, its *zeta function* is

$$
Z(X_0,T)=\exp\Bigl(\sum_{m\ge 1}\#X_0(\mathbf F_{q^m})\frac{T^m}{m}\Bigr)
\in 1+T\mathbf Q[[T]].
$$

A closed point $x$ of $X_0$ with residue field $\mathbf F_{q^{\deg x}}$
accounts for exactly $\deg x$ points of $X_0(\mathbf F_{q^m})$ when
$\deg x$ divides $m$, and for none otherwise. Hence
$\#X_0(\mathbf F_{q^m})=\sum_{\deg x\mid m}\deg x$, so

$$
\sum_{m\ge1}\#X_0(\mathbf F_{q^m})\frac{T^m}{m}
=\sum_{x\in|X_0|}\sum_{k\ge1}\frac{T^{k\deg x}}{k}
=-\sum_{x\in|X_0|}\log\bigl(1-T^{\deg x}\bigr).
$$

Only finitely many closed points have a given degree, so exponentiating
gives the Euler product

$$
Z(X_0,T)=\prod_{x\in|X_0|}\bigl(1-T^{\deg x}\bigr)^{-1},
$$

whose factors are power series with integer coefficients. So the
coefficients of $Z(X_0,T)$ are integers. For example,
$\#\mathbf P^1(\mathbf F_{q^m})=1+q^m$ gives
$Z(\mathbf P^1,T)=1/((1-T)(1-qT))$. Set $T=q^{-s}$. Since the residue
field of $x$ has $N(x)=q^{\deg x}$ elements, the Euler product becomes

$$
\zeta_{X_0}(s)=Z(X_0,q^{-s})=\prod_{x\in|X_0|}\bigl(1-N(x)^{-s}\bigr)^{-1},
$$

the analogue of Riemann's

$$
\zeta(s)=\sum_{n\ge1}n^{-s}=\prod_{p}\bigl(1-p^{-s}\bigr)^{-1},
$$

in which the closed points of $\operatorname{Spec}\mathbf Z$ have residue
fields with $p$ elements. Riemann conjectured that the nontrivial zeros of
$\zeta(s)$ lie on the line $\operatorname{Re}s=\tfrac12$.
Weil conjectured the following.

1. *Rationality.* $Z(X_0,T)$ is a rational function of $T$.
2. *Functional equation.* If $X_0$ is smooth and proper of pure
   dimension $d$, then $Z(X_0,1/(q^dT))=\pm q^{d\chi/2}T^{\chi}Z(X_0,T)$,
   where $\chi=\sum_i(-1)^ib_i$ is the Euler characteristic, with $b_i$
   as in (4). For a curve of genus $g$ it equals $2-2g$.
3. *Riemann hypothesis.* If $X_0$ is smooth and proper of pure
   dimension $d$, then
   $$
   Z(X_0,T)=\frac{P_1(T)P_3(T)\cdots P_{2d-1}(T)}
   {P_0(T)P_2(T)\cdots P_{2d}(T)},
   $$
   where $P_i\in\mathbf Z[T]$ has constant term $1$, and its reciprocal
   roots (the numbers $\alpha$ with $P_i(1/\alpha)=0$) are algebraic
   integers all of whose complex conjugates have absolute value $q^{i/2}$.
4. *Betti numbers.* The degree $b_i$ of $P_i$ behaves like a
   Betti number. For instance, $b_i=b_{2d-i}$, as for Poincaré duality
   on a compact manifold of real dimension $2d$. More precisely, suppose
   that $X_0$ comes from characteristic zero: there is a smooth projective
   variety $Y$ over a number field $K$ and a prime $\mathfrak p$ of $K$
   with residue field $\mathbf F_q$ such that $Y$ extends to a smooth
   projective scheme over the local ring $\mathcal O_{K,\mathfrak p}$ whose
   special fibre is $X_0$. Then $b_i$ is the $i$th Betti number of the compact
   complex manifold $Y(\mathbf C)$, for any embedding $K\subset\mathbf C$.
   For a curve of genus $g$ this gives $b_0=b_2=1$ and $b_1=2g$.

For a curve the conjectures recover the Hasse–Weil bound. Here
$Z(X_0,T)=P_1(T)/((1-T)(1-qT))$ with $P_1$ of degree $2g$, and statement
(3) says that $P_1(T)=\prod_{j=1}^{2g}(1-\alpha_jT)$ with
$|\alpha_j|=q^{1/2}$. Comparing the logarithmic derivatives of both sides
with the definition of $Z$ gives

$$
N_m=1+q^m-\sum_{j=1}^{2g}\alpha_j^m,
$$

and since each $|\alpha_j^m|=q^{m/2}$, the Hasse–Weil bound follows. This
is also why (3) is called the Riemann hypothesis. In the variable $s$ with
$T=q^{-s}$, the zeros of $P_1(q^{-s})$ satisfy $|q^{-s}|=q^{-1/2}$, that is,
they lie on the line $\operatorname{Re}s=\tfrac12$, exactly where Riemann
conjectured the zeros of $\zeta(s)$ to lie.

We follow one example through the notes, the elliptic curve

$$
C_0\colon\ y^2=x^3-x\qquad\text{over }\mathbf F_3 .
$$

Counting points, including the point at infinity, gives $N_1=4$, $N_2=16$
and $N_3=28$. Suppose the Weil conjectures hold for $C_0$. Then
$Z(C_0,T)=P_1(T)/((1-T)(1-3T))$, where $P_1$ has degree $b_1=2g=2$. Its
leading coefficient is $q=3$, because by duality it is the determinant of
Frobenius on $H^1$ (Example [example-running-example-duality]). So
$P_1=1-aT+qT^2$, and comparing the coefficients of $T$ in $Z$ gives
$a=1+q-N_1=0$. Hence $P_1(T)=1+3T^2$, whose reciprocal roots $\pm i\sqrt3$
have absolute value $3^{1/2}$. Statements (1)–(4) alone would not fix the
leading coefficient: $1-3T^2$ also satisfies them, with the sign $-$ in (2),
and it is the count $N_2=16$ that excludes it. As a check, the formula
$N_m=1+3^m-\bigl((i\sqrt3)^m+(-i\sqrt3)^m\bigr)$ gives $16$ and $28$ for
$m=2,3$. We return to this curve after duality, after the
trace formula and at the end
(Examples [example-running-example-duality], [example-running-example-trace-formula] and [example-running-example-purity]).
