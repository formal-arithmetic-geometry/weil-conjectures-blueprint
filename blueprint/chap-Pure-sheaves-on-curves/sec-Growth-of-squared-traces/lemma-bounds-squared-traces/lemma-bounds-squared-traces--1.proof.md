+++
kind = "proof"
of = "lemma-bounds-squared-traces--1"
order = 1202007
uses = ["definition-trace-function", "lemma-point-count-bound"]
+++
Choose a bound $N$ for the dimensions of the stalks of $F$, using
`AlgebraicGeometry.WeilSheaf.IsLisse.exists_forall_finrank_stalk_le`.
The punctual weight bound gives

$$
|\iota t_{F,n}(y)|\le Nq^{na/2}
$$

at every $y\in X_0(k_n)$, by
`AlgebraicGeometry.WeilSheaf.norm_map_traceFunction_le`.
Lemma [lemma-point-count-bound] gives $\#X_0(k_n)\le Dq^n$ for
$n\ge1$. Squaring the trace bound and summing gives the assertion
with $C=DN^2$.
