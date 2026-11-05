+++
kind = "proof"
of = "proposition-function-sheaf-dictionary--2"
order = 1028008
uses = ["proposition-properties-trace"]
+++
The internal hom out of the lisse sheaf $G^\vee$ is exact. Thus
$$
H^j(G\otimes^{\mathbf L}_{\Qbarl}K)
\simeq\mathcal{H}om(G^\vee,H^j(K))
$$
(`AlgebraicGeometry.WeilComplex.homologySheafTensorLisseIso`). On geometric
stalks the evaluation pairing identifies the internal hom with the hom
space, compatibly with Frobenius. Its trace is the trace on $H^j(K)$ times
the trace of inverse Frobenius on $G^\vee$; the latter is the trace on $G$.
This gives `AlgebraicGeometry.WeilSheaf.traceFunction_ihom_dual`.
Take the alternating sum over $j$ and factor out $t_{G,m}$.
