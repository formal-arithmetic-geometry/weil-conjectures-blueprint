+++
kind  = "proof"
of    = "lem-weil-stratum-ambient-hom"
+++
Factor $s$ into an open and a closed immersion. The adjunctions of
[def-weil-open-closed-recollement], [lem-exc-closed-ambient] construct
$Rs^!$ as their composite. Extension by zero for an open or closed
immersion is exact, and its stalkwise description gives, for all
complexes, $Q\otimes^LRs_!P=Rs_!(s^*Q\otimes^LP)$; use flat
resolutions to derive the tensor product. For every test complex
$Q$ on $X$, the adjunctions and the internal Hom of
[def-weil-derived-pullback-tensor-hom] give

$$
\begin{aligned}
\operatorname{Hom}_X(Q,R\mathcal Hom_X(Rs_!P,M))
&=\operatorname{Hom}_X(Rs_!(s^*Q\otimes^LP),M)\\
&=\operatorname{Hom}_S(s^*Q\otimes^LP,Rs^!M)\\
&=\operatorname{Hom}_X(Q,Rs_*R\mathcal Hom_S(P,Rs^!M)).
\end{aligned}
$$

Yoneda proves the assertion. The maps are defined by evaluation and
the adjunction counits, so the identity is compatible with both.
