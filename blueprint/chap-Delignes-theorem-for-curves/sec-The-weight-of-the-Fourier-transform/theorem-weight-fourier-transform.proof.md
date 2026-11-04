+++
kind = "proof"
of = "theorem-weight-fourier-transform"
order = 1279
uses = ["definition-trace-function", "definition-growth-squared-traces", "corollary-sums-squared-traces-j-shriek", "corollary-plancherel", "proposition-purity-lisse-part-fourier-transform"]
+++
Let $v$ be the weight of $M'$ given by
Proposition [proposition-purity-lisse-part-fourier-transform].
Shifts do not change the squared absolute values of traces. Moreover,
if a nonzero lisse sheaf on a dense open of the line is pure of weight
$u$, then its direct image $j_*$ has $\nu=u$
(Corollary [corollary-sums-squared-traces-j-shriek]). Applying this
to $M'$ and to $M$, and using the Plancherel formula
(Corollary [corollary-plancherel]), we get

$$
v=\nu(j'_*M')
=\nu(\operatorname{FT}_\psi((j_*M)[1]))
=\nu((j_*M)[1])+1=w+1.
$$

The first equality holds because $M'$ is pure of weight $v$, the second
is the defining isomorphism of $M'$, the third is Plancherel, and the
last holds because $M$ is pure of weight $w$.
