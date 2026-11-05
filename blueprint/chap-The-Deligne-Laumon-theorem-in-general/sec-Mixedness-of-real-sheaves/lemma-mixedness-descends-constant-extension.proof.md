+++
kind = "proof"
of = "lemma-mixedness-descends-constant-extension"
order = 1338
uses = ["proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images"]
+++
Since $g^*G$ is mixed, so is $g_*g^*G$ by
Lemma [lemma-finite-quasi-finite-direct-images]. The unit
$G\to g_*g^*G$ has the Weil-equivariant retraction
$(\deg g)^{-1}\operatorname{Tr}$. Indeed, étale locally the unit is
the diagonal and the trace is the sum over the copies. These local
maps glue because the sum is invariant under permutations of the
copies. So $G$ is a Weil subsheaf of $g_*g^*G$. A Weil subobject of a
mixed sheaf is mixed
(Proposition [proposition-weights-under-usual-operations]), and
therefore $G$ is mixed.
