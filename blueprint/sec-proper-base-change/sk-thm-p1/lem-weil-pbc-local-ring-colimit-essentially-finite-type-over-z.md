+++
id = "lem-weil-pbc-local-ring-colimit-essentially-finite-type-over-z"
kind = "lemma"
title = "A local ring is a directed colimit of local rings essentially of finite type over Z"
lean = ["CommRingCat.exists_local_essFiniteType_colimit"]
order = 1985
+++
Let $(R,\mathfrak m)$ be a local ring (a commutative ring with exactly one maximal ideal $\mathfrak m$). Then there exist a nonempty directed set $(\Lambda,\le)$, for every $\lambda\in\Lambda$ a local ring $(R_\lambda,\mathfrak p_\lambda)$, for $\lambda\le\mu$ local homomorphisms $r_{\mu\lambda}:R_\lambda\to R_\mu$ (a ring map $\varphi:(C,\mathfrak m_C)\to(D,\mathfrak m_D)$ of local rings is *local* if $\varphi(\mathfrak m_C)\subseteq\mathfrak m_D$), with $r_{\lambda\lambda}=\mathrm{id}$ and $r_{\nu\mu}\circ r_{\mu\lambda}=r_{\nu\lambda}$ for $\lambda\le\mu\le\nu$, and for every $\lambda$ a local homomorphism $\pi_\lambda:R_\lambda\to R$ with $\pi_\mu\circ r_{\mu\lambda}=\pi_\lambda$, such that (1) $(R,(\pi_\lambda)_{\lambda\in\Lambda})$ is a colimit of the system $(R_\lambda,r_{\mu\lambda})$ in the category of commutative rings, and (2) every $R_\lambda$ is essentially of finite type over $\mathbf Z$.
