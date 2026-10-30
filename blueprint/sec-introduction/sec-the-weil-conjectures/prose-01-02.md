+++
id = "prose-01-02"
kind = "hidden"
title = "The Weil conjectures"
order = 5
+++
The Weil conjectures, formulated by Weil in 1949 (Wei), are
statements about the number of solutions of polynomial equations over
finite fields. The simplest case already shows what is at stake. Let
$X_0$ be a smooth projective geometrically connected curve of genus
$g$ over $\mathbf F_q$, and
let $N_m$ be the number of its points over $\mathbf F_{q^m}$. Then
$N_m$ is close to $1+q^m$, the number of points of the projective
line, and the precise form of this statement is the bound

$$
|N_m-(1+q^m)|\le 2g\,q^{m/2}.
$$

Hasse proved it for elliptic curves and Weil for all curves. Written in
terms of the zeta function, it says that the zeros of a certain
function of a complex variable $s$ lie on the line $\operatorname{Re}s=\tfrac12$,
which is why it is called the Riemann hypothesis for $X_0$. Weil
conjectured that the same structure exists in every dimension.

Let $X_0$ be a separated scheme of finite type over $\mathbf F_q$. Its
zeta function is

$$
Z(X_0,T)=\exp\Bigl(\sum_{m\ge 1}\#X_0(\mathbf F_{q^m})\frac{T^m}{m}\Bigr)
\in 1+T\mathbf Z[[T]].
$$

Weil conjectured the following.

1. *Rationality.* $Z(X_0,T)$ is a rational function of $T$.
2. *Functional equation.* If $X_0$ is smooth and proper of pure
   dimension $d$, then $Z(X_0,1/(q^dT))=\pm q^{d\chi/2}T^{\chi}Z(X_0,T)$
   for an integer $\chi$, the self-intersection number of the diagonal.
3. *Riemann hypothesis.* If $X_0$ is smooth and proper of pure
   dimension $d$, then

$$
Z(X_0,T)=\frac{P_1(T)P_3(T)\cdots P_{2d-1}(T)}
{P_0(T)P_2(T)\cdots P_{2d}(T)},
$$

where $P_i\in\mathbf Z[T]$ has constant term $1$ and its reciprocal
roots are algebraic integers all of whose complex conjugates have
absolute value $q^{i/2}$.
4. *Betti numbers.* The degree $b_i$ of $P_i$ is an invariant of
   $X_0$ that behaves like a Betti number; for instance $b_i=b_{2d-i}$,
   and if $X_0$ is the reduction, at a prime of good reduction, of a
   smooth projective variety over a number field, $b_i$ is the $i$th
   Betti number of the associated complex manifold.

For a curve, (3) says that $Z(X_0,T)=P_1(T)/((1-T)(1-qT))$ with $P_1$ of
degree $2g$ and reciprocal roots of absolute value $q^{1/2}$, and taking
logarithms gives the bound on $N_m$ above.

We follow one example through the notes: the elliptic curve

$$
C_0\colon\ y^2=x^3-x\qquad\text{over }\mathbf F_3 .
$$

Counting points gives $N_1=4$, $N_2=16$ and $N_3=28$. The Weil conjectures
predict $Z(C_0,T)=P_1(T)/((1-T)(1-3T))$ with
$P_1(T)=1-(1+3-N_1)T+3T^2=1+3T^2$, which has reciprocal roots $\pm i\sqrt3$ of absolute value
$3^{1/2}$, and then $N_m=1+3^m-\bigl((i\sqrt3)^m+(-i\sqrt3)^m\bigr)$. For
$m=2,3$ this gives $16$ and $28$, as it should. We return to it after
duality, after the trace formula and at the end
(Examples [sk-ex-ex-run-duality], [sk-ex-ex-run-trace] and [sk-ex-ex-run-end]).
