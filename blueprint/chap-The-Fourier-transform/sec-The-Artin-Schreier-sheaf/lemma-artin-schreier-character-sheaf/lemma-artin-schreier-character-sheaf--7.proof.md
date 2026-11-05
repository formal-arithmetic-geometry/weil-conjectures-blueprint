+++
kind = "proof"
of = "lemma-artin-schreier-character-sheaf--7"
order = 1217013
uses = ["lemma-artin-schreier-character-sheaf--1", "lemma-artin-schreier-character-sheaf--6", "definition-weights"]
+++
Let $d=[k(x):k_0]$ and choose a point $y$ over $x$ with values in
$\mathbf F_{q^d}$. Put
$c=\operatorname{Tr}_{\mathbf F_{q^d}/k_0}(ay)$. This choice depends on
$a$ and $x$, but not on $\psi$.
By [lemma-artin-schreier-character-sheaf--6], the local Frobenius at $x$
has trace $\psi(c)$. Its stalk is a line by
[lemma-artin-schreier-character-sheaf--1], so an endomorphism is its trace
times the identity, as in
`LinearMap.eq_trace_smul_id_of_finrank_eq_one`.

For the norm identity, let $p=\operatorname{char}(K)$. Additivity gives
$\chi(c)^p=\chi(pc)=\chi(0)=1$. Since $p\ne0$, applying $\iota$ shows
that $\iota(\chi(c))$ is a root of unity and has absolute value one.
The weight-zero conclusion follows from [definition-weights].
