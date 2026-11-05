+++
kind = "proof"
of = "lemma-bounds-squared-traces--3"
order = 1202009
uses = ["proposition-weights-j-boundary-points", "definition-trace-function", "lemma-point-count-bound"]
+++
By [proposition-weights-j-boundary-points], $j_*M$ is punctually of
weights $\le a$. The complement of $U_0$ is a finite set $Z$ of
closed points. Let $N$ bound the dimensions of the stalks of $j_*M$
at these points, and put $d=\sum_{x\in Z}[k(x):k_0]$.

The bound `AlgebraicGeometry.WeilSheaf.norm_map_traceFunction_le`
shows that each summand is at most $N^2q^{na}$. There are at most
$d$ rational points over $Z$: for each $x$, the rational points
above it inject into the $k_0$-embeddings of $k(x)$ into $k_n$,
whose number is at most $[k(x):k_0]$. This is
`AlgebraicGeometry.Scheme.Hom.card_fieldPoints_base_eq_le`, the
pointwise count underlying [lemma-point-count-bound]. Summing gives
$E_n\le dN^2q^{na}$, so take $C=dN^2$.
