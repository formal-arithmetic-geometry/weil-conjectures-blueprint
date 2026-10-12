+++
kind  = "proof"
of    = "prop-functional-equation"
+++
1. **1.** The exponential series defining $Z(X_0,T)$ is the
point-count zeta series of [def-weil-point-counts-zeta]; the
trace-to-determinant calculation in
[prop-trace-determinant] identifies it with the normalized product
$$
Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}.
$$
All subsequent manipulations therefore take place in the Laurent rational
function field $\mathbf Q(T)$.
1. **2.** The reciprocity relations in
[prop-duality-reciprocity] give
$$
b_i=b_{2d-i},\qquad D_iD_{2d-i}=q^{db_i},\qquad
P_i(q^{-d}T^{-1})
=(-1)^{b_i}T^{-b_i}D_{2d-i}^{-1}P_{2d-i}(T),
$$
where the last equality is the displayed relation with $i$ replaced by
$2d-i$. Reindexing the product in Step 1 by $i\mapsto2d-i$, and using
$(-1)^{2d-i}=(-1)^i$, gives
$$
\begin{aligned}
Z(X_0,q^{-d}T^{-1})
&=\prod_{i=0}^{2d}
\left((-1)^{b_i}T^{-b_i}D_{2d-i}^{-1}P_{2d-i}(T)\right)^{(-1)^{i+1}}\\
&=(-1)^\chi T^\chi
\left(\prod_{i=0}^{2d}D_i^{(-1)^i}\right)Z(X_0,T).
\end{aligned}
$$
These same reciprocity relations show that $d\chi$ is even. This is
immediate if $d$ is even. If $d$ is odd, then
[prop-duality-reciprocity] gives that $b_d$ is even, while pairing
the terms indexed by $i$ and $2d-i$ gives
$$
\chi=
2\sum_{0\leq i<d}(-1)^ib_i+(-1)^db_d,
$$
which is even. Thus the normalized sign in
[def-weil-functional-equation-sign] is defined.
The determinant-constant definition in
[def-weil-functional-equation-sign] names the product in parentheses
$\Delta$, and the same definition gives
$$
\varepsilon=(-1)^\chi q^{-d\chi/2}\Delta.
$$
The determinant relation also implies
$$
\Delta^2
=\prod_{i=0}^{2d}(D_iD_{2d-i})^{(-1)^i}
=\prod_{i=0}^{2d}q^{db_i(-1)^i}
=q^{d\chi}.
$$
1. **3.** Squaring the preceding normalization and using
[def-weil-functional-equation-sign] yields
$$
\varepsilon^2
=(-1)^{2\chi}q^{-d\chi}\Delta^2=1.
$$
Since $\varepsilon\in\mathbf Q^\times$, it follows that
$\varepsilon\in\{1,-1\}$.
1. **4.** Substituting
$(-1)^\chi\Delta=\varepsilon q^{d\chi/2}$ into the product identity of
Step 2 gives
$$
Z(X_0,q^{-d}T^{-1})
=\varepsilon q^{d\chi/2}T^\chi Z(X_0,T).
$$
Replacing $\Delta$ by its defining product from
[def-weil-functional-equation-sign] gives equivalently
$$
Z(X_0,q^{-d}T^{-1})
=(-1)^\chi T^\chi
\left(\prod_{i=0}^{2d}D_i^{(-1)^i}\right)Z(X_0,T),
$$
which proves both asserted forms.
