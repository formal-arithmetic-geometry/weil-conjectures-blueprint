+++
kind  = "proof"
of    = "lem-a1-subquotient-pure"
+++
Fix a closed point $x$ and let $(V_x,F_x)$ be the stalk Frobenius
module of $\mathcal G$ at $x$, with eigenvalue multiset $S_x$ as in
[def-weil-punctual-weights]. The geometric stalk functor on $\Cons(X,\Qlb)$ is exact
([sk-lem-coefficient-heart](1): kernels and cokernels are computed in
$\Mod(X_{\mathrm{proét}},\Qlb)$, where pullback to a geometric point is exact), so the stalk module of $\mathcal S$ at $x$ is an
$F_x$-stable subquotient of $(V_x,F_x)$; hence its eigenvalue multiset
is a submultiset of $S_x$, which is the spectrum bookkeeping of
[lem-a1-spectrum-exact-sequence] applied successively to the
subobject and to the quotient. Every eigenvalue of $(V_x,F_x)$ has
$\iota$-modulus $q_x^{w/2}$ by the punctual purity of weight $w$ of
[def-weil-punctual-weights], hence so does every eigenvalue of the
stalk module of $\mathcal S$; the closed point $x$ was arbitrary, so
$\mathcal S$ is punctually $\iota$-pure of weight $w$.
