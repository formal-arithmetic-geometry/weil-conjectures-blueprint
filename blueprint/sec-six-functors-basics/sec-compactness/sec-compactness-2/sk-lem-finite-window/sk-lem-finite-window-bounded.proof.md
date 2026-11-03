+++
kind = "proof"
of = "det-finite-window-bounded"
+++
Induction on the number of nonzero cohomology sheaves of $L$. If $L=0$ there is nothing to prove. If
$L\cong H^q(L)[-q]$, then $\Hom(C,L)=\Ext^{-q}(C,H^q(L))$, which vanishes by [sk-cor-ind-heart-ii]
because $H^q(L)\in\IndCons(X,\Lambda)$ and $-q\geq d_C+1>d_C$. In general let $q_0$ be the smallest degree
with $H^{q_0}(L)\neq0$. The triangle

$$
H^{q_0}(L)[-q_0]\to L\to\tau_{\geq q_0+1}L\to
$$

has outer terms satisfying the hypothesis with fewer nonzero cohomology sheaves (and still lying in
$\Dic(X,\Lambda)$ by [sk-cor-ambient-ind-derived]); the exact sequence
$\Hom(C,H^{q_0}(L)[-q_0])\to\Hom(C,L)\to\Hom(C,\tau_{\geq q_0+1}L)$ and induction give $\Hom(C,L)=0$.
