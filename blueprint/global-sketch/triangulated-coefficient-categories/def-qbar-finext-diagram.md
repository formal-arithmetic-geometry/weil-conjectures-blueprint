+++
id = "def-qbar-finext-diagram"
kind = "definition"
title = "Finite coefficient index and transition diagram"
order = 17
uses = ["def-weil-finite-coefficient-datum", "def-weil-rational-coefficients"]
+++
For a scheme $Y$, fix a prime $\ell\neq p$ and an algebraic closure
$\Qlb/\Ql$, as in
Definition [def-weil-finite-coefficient-datum].
Let $\mathcal E_\ell$ be the poset category whose objects are the finite
extensions $\Ql\subset E\subset\Qlb$, with one arrow $E\to L$ exactly
when $E\subset L$. The compositum of finitely many objects is a common
upper bound, so $\mathcal E_\ell$ is filtered. We use a small skeleton of
this poset in a Grothendieck universe containing the coefficient fields and
the categories below. Put

$$
\mathcal C_E(Y)=D^b_c(Y,E),
\qquad
T_{L/E}(K)=K\otimes_E L.
$$

The transition datum includes exact natural isomorphisms

$$
\eta_E:T_{E/E}\xrightarrow{\sim}\operatorname{id},
\qquad
a_{M,L,E}:T_{M/L}T_{L/E}\xrightarrow{\sim}T_{M/E}
$$

for $E\subset L\subset M$. The unit equations, the tower pentagon, and
the shift comparisons are part of this datum.
