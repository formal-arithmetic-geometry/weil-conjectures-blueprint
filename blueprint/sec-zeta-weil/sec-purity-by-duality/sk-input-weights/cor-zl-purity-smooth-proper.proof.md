+++
kind  = "proof"
of    = "cor-zl-purity-smooth-proper"
+++
This is the absolute case of [prop-zl-smooth-proper-relative-purity].
Take $Y_0=\Spec k_0$ and $f_0=a_X:X_0\to\Spec k_0$, the structure morphism of
[def-weil-finite-field-fiber]: it is smooth and proper of pure relative
dimension $d$, and [prop-zl-smooth-proper-relative-purity] imposes no
admissibility hypothesis on it or on the structure morphisms. Take
$\mathcal F_0=(\Qlb)_{X_0}$, the constant Weil sheaf. It is
lisse, and it is punctually $\iota$-pure of weight $0$ in the sense of
[def-weil-punctual-weights]: at every closed point $x$ the local
Frobenius of [def-weil-local-frobenius-trace] is the identity of the
one-dimensional stalk, so its only eigenvalue is $1$ and
$|\iota(1)|=1=q_x^{0/2}$.

The base $\Spec k_0$ has a single closed point $y$, with $q_y=q$ and
geometric point $\bar y=\Spec k$; the geometric fibre of $a_X$ over it is
$X$. The stalk of $R^{i}a_{X*}(\Qlb)_{X_0}$ at $\bar y$ is
$H^{i}(X,\Qlb)$, and the Weil isomorphism on $Ra_{X*}$ of
[prop-weil-operations], iterated once ($y$ has degree $1$), is the action
on cohomology of the global geometric Frobenius of
[def-weil-global-geometric-frobenius]; hence the local operator $F_y$ is
$F$. Clause (b) of [prop-zl-smooth-proper-relative-purity] (with $w=0$)
therefore says that every eigenvalue $\alpha$ of $F$ on $H^{i}(X,\Qlb)$
satisfies $|\iota(\alpha)|=q^{i/2}$, which is $\iota$-purity of weight $i$
of $(H^{i}(X,\Qlb),F)$ in the sense of
[def-weil-frobenius-module-weights]. By clause (a) the canonical map
$H_c^{i}(X,\Qlb)\to H^{i}(X,\Qlb)$ is a Frobenius-equivariant isomorphism
(the proper coincidence of [prop-weil-operations]), and a pure Frobenius
module of weight $i$ is $\iota$-mixed of weights at most $i$ (take $m=1$,
$w_1=i$ in [def-weil-frobenius-module-weights]); this is the assertion on
$H_c^{i}(X,\Qlb)$.
