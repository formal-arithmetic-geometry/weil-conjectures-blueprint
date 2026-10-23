+++
id = "lem-weil-pbc-limit-finite-presentation"
kind = "lemma"
title = "Noetherian approximation of a finitely presented ring map"
lean = ["Algebra.exists_limit_finite_presentation"]
order = 1879
+++
Let $\varphi:R\to S$ be a homomorphism of commutative rings of finite presentation. Then there exist a nonempty directed set $(\Lambda,\le)$ and the following data: for every $\lambda\in\Lambda$ commutative rings $R_\lambda$, $S_\lambda$ and a ring map $\rho_\lambda:R_\lambda\to S_\lambda$; for $\lambda\le\mu$ ring maps $R_\lambda\to R_\mu$ and $S_\lambda\to S_\mu$ (written $x\mapsto\bar x$), equal to the identity for $\lambda=\mu$, compatible with composition and with $\rho_\lambda,\rho_\mu$; and for every $\lambda$ ring maps $\pi_\lambda:R_\lambda\to R$ and $\kappa_\lambda:S_\lambda\to S$, compatible with the transition maps and with $\varphi\circ\pi_\lambda=\kappa_\lambda\circ\rho_\lambda$; such that (1) $(R,(\pi_\lambda)_\lambda)$ and $(S,(\kappa_\lambda)_\lambda)$ are colimits of the systems $(R_\lambda)$ and $(S_\lambda)$ in the category of commutative rings; (2) every $R_\lambda$ is a finite type $\mathbf Z$-algebra; (3) every $S_\lambda$ is a finite type $R_\lambda$-algebra via $\rho_\lambda$; (4) for $\lambda\le\mu$ the ring map $S_\lambda\otimes_{R_\lambda}R_\mu\to S_\mu$, $s\otimes r\mapsto\bar s\,\rho_\mu(r)$, is an isomorphism; (5) for every $\lambda$ the ring map $S_\lambda\otimes_{R_\lambda}R\to S$, $s\otimes r\mapsto\kappa_\lambda(s)\varphi(r)$ (with $R$ an $R_\lambda$-algebra via $\pi_\lambda$), is an isomorphism.
