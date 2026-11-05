+++
kind = "proof"
of = "lemma-change-coefficients-internal-hom"
order = 643
uses = ["proposition-topos-functoriality"]
+++
Internal Hom is a right adjoint. As for $f^!$, there is no formal reason
for it to commute with extension of scalars, and we argue as in the proof
of Proposition [proposition-six-operations-dctf]. The comparison map for $\cHom(-,L)$ is compatible with triangles in the first argument, so we choose a finite stratification on whose strata $K$ is locally
$\Lambda_S\otimes P$ with $P$ perfect. By the five lemma and finite cones
we may then reduce to the case $K=a_!P$, with $a:S\hookrightarrow X$
locally closed and $P$ a locally constant perfect complex on $S$. The
identity

$$
\cHom_X(a_!P,L)
\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!L)
$$

commutes with extension of scalars by
Lemmas [lemma-change-coefficients-direct-image]
and [lemma-change-coefficients-exceptional-inverse-image], the
isomorphism of Definition [definition-change-of-coefficients-maps](3),
and the comparison for the dual of a perfect complex. For the last of these, recall that $P$ is locally a finite complex of finite projective modules, and for such modules
$\cHom(P,\Lambda)_{\Lambda'}=\cHom(P_{\Lambda'},\Lambda')$ term by term.
Moreover, all of these identifications are defined by the same evaluation pairing.
Hence their composite is the map of
Definition [definition-change-of-coefficients-maps](6).
