+++
id = "prose-01-06"
kind = "hidden"
title = "The trace formula"
order = 13
+++
Part II proves Poincaré duality and the trace formula.
Why should the Lefschetz formula hold for Frobenius? For a self-map
$\varphi$ of a compact manifold whose fixed points are transverse, the
formula counts each fixed point $x$ with the sign of $\det(1-d\varphi_x)$.
The differential of Frobenius is zero, because $d(u^q)=qu^{q-1}du=0$ in
characteristic $p$. So every fixed point should count with $+1$. On a curve
one can see this directly. Let $u$ be a local coordinate at a fixed point,
and $v$ the same coordinate on the second factor of $X\times X$. The graph
of $F^m$ is $v=u^{q^m}$, and it meets the diagonal $v=u$ with multiplicity one.

The Grothendieck–Lefschetz trace formula states that for every Weil
complex $K$,

$$
\operatorname{Tr}\bigl(F^m\mid R\Gamma_c(X,K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}t_K(y)
$$

(Theorem [theorem-grothendieck-lefschetz-trace-formula]). For the constant
sheaf it is axiom (b). In
Example [example-running-example-trace-formula] we apply it to the curve
$C_0$, where it reads $N_m=1-\operatorname{Tr}(F^m\mid H^1)+3^m$. Since
$N_1=4$, the trace of $F$ on $H^1$ is $0$. Duality gives
$\det(F\mid H^1)=3$, and we recover $Z(C_0,T)=(1+3T^2)/((1-T)(1-3T))$.

We deduce it, as in SGA 5 [sga5, III, III B, XV], from a general
Lefschetz formula. A *correspondence* on $X$ is a pair of maps
$c_1,c_2:C\to X$. For instance, the graph of a map $\varphi$ is a
correspondence with $c_1=\mathrm{id}$ and $c_2=\varphi$. To act on the
cohomology of $K$, a correspondence needs a map $u:c_2^*K\to c_1^!K$. For
the graph of $F$ this is the Frobenius structure $F^*K\to K$. The
Lefschetz–Verdier formula
(Theorem [theorem-proper-pushforward-lefschetz-verdier]) holds when $X$ and
$C$ are proper. It writes the trace on cohomology as a sum, over the fixed
points, of *local terms*, numbers computed from $K$ and $u$ near each
fixed point. In general a local term is not the trace on the stalk.

To apply this to Frobenius on a curve $X$, which need not be proper, we
compactify. The new points at infinity are fixed points at which $K$ is
not locally constant. The main computation of Part II
shows that even so, at every fixed point $y$ of Frobenius on a curve, the
local term is the trace of $\operatorname{Frob}_y$ on $K_{\bar y}$
(Proposition [proposition-frobenius-local-term-curve]). To prove this,
we cut $K$ into its restrictions to $y$ and to the complement of $y$. Local terms are additive
for this decomposition, and for the piece supported at $y$ the local term is
the trace. It therefore suffices to show that the local term vanishes when
$K_{\bar y}=0$.

Here $dF=0$ is used once more. At $(y,y)$ the graph $v=u^{q^m}$ is tangent
to the axis $v=0$, that is, to $X\times\{y\}$, while the diagonal $v=u$ is
not. Blowing up the point $(y,y)$ of $X\times X$ therefore separates the two
curves. The local term can then be computed near the exceptional divisor,
where one shows that it vanishes. In Section [chap-The-trace-formula] we
use instead the transposed graph $\{(F^mx,x)\}$, which is tangent to
$\{y\}\times X$.

Curves suffice for the general case. Indeed, the trace formula is
compatible with $Rf_!$, and a variety can be fibred in curves over a
variety of smaller dimension.
