+++
id = "def-weil-pbc-ring-map-quasi-finite-at-prime"
kind = "definition"
title = "Ring map quasi-finite at a prime (affine notion)"
lean = ["Algebra.IsQuasiFiniteAtPrime"]
order = 1637
+++
Let $\varphi:R\to S$ be a ring map of finite type, i.e. $S$ is finitely generated as an $R$-algebra. Let $\mathfrak q\subset S$ be a prime ideal and $\mathfrak p=\varphi^{-1}(\mathfrak q)$, with residue field $\kappa(\mathfrak p)=R_{\mathfrak p}/\mathfrak pR_{\mathfrak p}$, and let $F=S\otimes_R\kappa(\mathfrak p)$ be the fibre ring of $S$ over $\mathfrak p$, with $j:S\to F$, $s\mapsto s\otimes1$. Let $\overline{\mathfrak q}\subset F$ be the prime ideal of $F$ corresponding to $\mathfrak q$, i.e. the unique prime ideal of $F$ with $j^{-1}(\overline{\mathfrak q})=\mathfrak q$ ($\operatorname{Spec}F$ is homeomorphic, via $j$, to the set of primes of $S$ lying over $\mathfrak p$). We say that $R\to S$ is *quasi-finite at $\mathfrak q$* if $\overline{\mathfrak q}$ is an isolated point of $\operatorname{Spec}(F)$, that is, the singleton $\{\overline{\mathfrak q}\}$ is open in the Zariski topology of $\operatorname{Spec}(S\otimes_R\kappa(\mathfrak p))$.
