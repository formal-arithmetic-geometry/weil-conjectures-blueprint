+++
id = "lem-weil-pbc-henselian-etale-retraction-uniqueness"
kind = "lemma"
title = "Uniqueness of a henselian étale retraction"
uses = ["def-weil-pbc-henselian-terminology"]
lean = ["algHom_eq_of_henselianLocalRing_etale"]
order = 1907
+++
Let $(S,\mathfrak m,\kappa)$ be a henselian local ring [def-weil-pbc-henselian-terminology], let $\varphi:S\to B$ be a ring map such that $\operatorname{Spec}B\to\operatorname{Spec}S$ is etale, and let $\mathfrak q'\subset B$ be a prime ideal with $\varphi^{-1}(\mathfrak q')=\mathfrak m$ such that the induced map of residue fields $\kappa\to\kappa(\mathfrak q')$ is bijective. If $\sigma,\tau:B\to S$ are $S$-algebra homomorphisms with $\sigma^{-1}(\mathfrak m)=\mathfrak q'$ and $\tau^{-1}(\mathfrak m)=\mathfrak q'$, then $\sigma=\tau$.
