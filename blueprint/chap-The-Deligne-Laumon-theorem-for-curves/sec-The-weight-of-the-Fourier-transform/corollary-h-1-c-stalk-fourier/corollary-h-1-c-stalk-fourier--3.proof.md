+++
kind = "proof"
of = "corollary-h-1-c-stalk-fourier--3"
order = 1287006
uses = ["proposition-fourier-transform-middle-extension", "proposition-purity-lisse-part-fourier-transform", "theorem-weight-fourier-transform", "proposition-weights-j-boundary-points", "corollary-h-1-c-stalk-fourier--2"]
+++
By Proposition [proposition-fourier-transform-middle-extension], choose
a lisse sheaf $M'$ on a dense open of the dual line such that
$\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]$.
Proposition [proposition-purity-lisse-part-fourier-transform] makes
$M'$ punctually $\iota$-pure of some real weight $v$.
The weight calculation in Theorem [theorem-weight-fourier-transform]
gives $v\le w+1$.

Consequently $M'$ has punctual weights at most $w+1$.
Proposition [proposition-weights-j-boundary-points] gives the same
bound for $j'_*M'$ on the whole dual line, including $0'$.
Since $0'$ is rational, its residue cardinality is $q$.
Transport the bound at $0'$ along the Frobenius-equivariant
isomorphism of [corollary-h-1-c-stalk-fourier--2].
