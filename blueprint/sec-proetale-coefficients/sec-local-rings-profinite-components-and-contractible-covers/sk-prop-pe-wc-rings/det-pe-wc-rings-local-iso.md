+++
id = "det-pe-wc-rings-local-iso"
kind = "lemma"
title = "Local rings of a weakly étale algebra over a strictly henselian point"
lean = ["Algebra.WeaklyEtale.bijective_localRingHom_of_isStrictlyHenselianLocalRing"]
order = 937
uses = ["thm-weil-pbc-weak-etale-strict-local", "lem-weil-pbc-ind-etale-stability"]
+++
Let $R\to B$ be weakly étale (for instance ind-étale), and let $\mathfrak n\subset B$ be a
prime such that, for $\mathfrak m=\mathfrak n\cap R$, the local ring $R_{\mathfrak m}$ is
strictly henselian. Then $R_{\mathfrak m}\to B_{\mathfrak n}$ is an isomorphism.
