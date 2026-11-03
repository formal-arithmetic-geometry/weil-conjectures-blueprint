+++
id = "lem-weil-pbc-henselian-etale-retraction-existence"
kind = "lemma"
title = "Existence of a henselian étale retraction"
uses = ["def-weil-pbc-henselian-terminology"]
lean = ["exists_algHom_of_henselianLocalRing_etale"]
order = 2028
+++
Let $(S,\mathfrak m,\kappa)$ be a henselian local ring [def-weil-pbc-henselian-terminology], let $\varphi:S\to B$ be a ring map such that $\operatorname{Spec}B\to\operatorname{Spec}S$ is etale, and let $\mathfrak q'\subset B$ be a prime ideal with $\varphi^{-1}(\mathfrak q')=\mathfrak m$ such that the induced map of residue fields $\kappa\to\kappa(\mathfrak q')$ is bijective. Then there exists an $S$-algebra homomorphism $\sigma:B\to S$ with $\sigma^{-1}(\mathfrak m)=\mathfrak q'$.
