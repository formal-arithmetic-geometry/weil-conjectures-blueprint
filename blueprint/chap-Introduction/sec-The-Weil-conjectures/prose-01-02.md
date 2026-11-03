+++
id = "prose-01-02"
kind = "hidden"
title = "The Weil conjectures"
order = 5
+++
Let $X_0$ be a smooth projective geometrically connected curve of genus
$g$ over the finite field $\mathbf F_q$, and let $N_m$ be the number of
its points with coordinates in $\mathbf F_{q^m}$. The projective line
has $1+q^m$ such points, and $N_m$ is close to this number:

$$
|N_m-(1+q^m)|\le 2g\,q^{m/2}.
$$

Hasse proved this for elliptic curves and Weil for all curves.

To state Weil's conjectures in higher dimension we put all the numbers
$N_m$ into one generating function. For a separated scheme $X_0$ of
finite type over $\mathbf F_q$, its *zeta function* is

$$
Z(X_0,T)=\exp\Bigl(\sum_{m\ge 1}\#X_0(\mathbf F_{q^m})\frac{T^m}{m}\Bigr)
\in 1+T\mathbf Z[[T]].
$$

The coefficients are integers, because $Z(X_0,T)$ is also the product of
the factors $(1-T^{\deg x})^{-1}$ over the closed points $x$ of $X_0$. Here
$\deg x$ is the degree of the residue field of $x$ over $\mathbf F_q$. This
product is the analogue of the Euler product of the Riemann zeta function.
For example, $\#\mathbf P^1(\mathbf F_{q^m})=1+q^m$ gives
$Z(\mathbf P^1,T)=1/((1-T)(1-qT))$. Weil conjectured the following.

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
   Betti number. For instance, $b_i=b_{2d-i}$. If $X_0$ is the
   reduction of a smooth projective variety over a number field at a
   prime of good reduction, then $b_i$ is the $i$th Betti number of the
   associated complex manifold.

For a curve, $Z(X_0,T)=P_1(T)/((1-T)(1-qT))$ with $P_1$ of degree
$2g$. Statement (3) says that $P_1(T)=\prod_{j=1}^{2g}(1-\alpha_jT)$ with
$|\alpha_j|=q^{1/2}$. Taking
logarithms gives $N_m=1+q^m-\sum_j\alpha_j^m$, and the bound above follows. The
name comes from the substitution $T=q^{-s}$: the zeros of $P_1(q^{-s})$
satisfy $|q^{-s}|=q^{-1/2}$, that is, they lie on the line
$\operatorname{Re}s=\tfrac12$.

We follow one example through the notes, the elliptic curve

$$
C_0\colon\ y^2=x^3-x\qquad\text{over }\mathbf F_3 .
$$

Counting points, including the point at infinity, gives $N_1=4$, $N_2=16$
and $N_3=28$. For an elliptic curve, $P_1$ has degree $2$ and leading
coefficient $q$. This coefficient is the determinant of Frobenius on $H^1$,
which duality computes. So $P_1=1-aT+qT^2$, and comparing the coefficients
of $T$ in $Z$ gives $a=1+q-N_1$. Here $a=0$, and $P_1(T)=1+3T^2$. Its
reciprocal roots $\pm i\sqrt3$ have absolute value $3^{1/2}$. As a check, the formula
$N_m=1+3^m-\bigl((i\sqrt3)^m+(-i\sqrt3)^m\bigr)$ gives $16$ and $28$ for
$m=2,3$. We return to this curve after duality, after the
trace formula and at the end
(Examples [example-running-example-duality], [example-running-example-trace-formula] and [example-running-example-purity]).
