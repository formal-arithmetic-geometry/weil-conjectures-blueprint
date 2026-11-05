+++
kind = "proof"
of = "corollary-functional-equation--7"
order = 1044012
uses = []
+++
The perfect pairing identifies $W$ with $V^\vee$. Transport $G$ along this
identification, and call the resulting endomorphism $G'$. The similitude
condition says that

$$
F^\vee G'=c\,\id_{V^\vee}.
$$

This is `LinearMap.dualMap_mul_conj_of_similitude`. Apply
`LinearMap.C_det_mul_charpolyRev` to this product relation. The determinant
and characteristic polynomial of $F^\vee$ agree with those of $F$, the
reverse characteristic polynomial is unchanged by conjugation, and
$\dim_K V^\vee=\dim_K V$. These substitutions give the asserted identity.
