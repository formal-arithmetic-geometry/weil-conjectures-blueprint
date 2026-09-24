+++
id = "lem-fd-as-cover"
kind = "lemma"
title = "The Artin–Schreier covering"
order = 1737
uses = ["def-fd-artin-schreier-sheaf", "def-weil-pbc-etale-site"]
+++
The morphism $\pi:Y\to X_0$, $\operatorname{Spec}\mathcal O[T]/(T^p-T-f)\to X_0$, is finite etale of degree $p$, and $\mathrm{Aut}(Y/X_0)\cong\mathbf F_p$, acting by $T\mapsto T+a$.

## Proof

The ring $B=\mathcal O_{X_0}[T]/(T^p-T-f)$ is the covering ring of the
Artin–Schreier sheaf construction [def-fd-artin-schreier-sheaf]:
it is a free $\mathcal O_{X_0}$-module with basis $1,T,\ldots,T^{p-1}$, so $\pi$ is finite of degree $p$; it is etale because the formal derivative of $T^p-T-f$ is $-1$, a unit of $B$, so $B$ is *standard etale* over $\mathcal O_{X_0}$ in the sense of [def-weil-pbc-etale-site]. For $a\in\mathbf F_p$ the map $T\mapsto T+a$ is well defined because $(T+a)^p-(T+a)-f=T^p-T-f+a^p-a=T^p-T-f$, and these $p$ endomorphisms are the only ones: an $\mathcal O_{X_0}$-algebra endomorphism sends $T$ to a root of $T^p-T-f$, and the difference of two roots is a root of $X^p-X=\prod_{a\in\mathbf F_p}(X-a)$, hence is one of the constants $a\in\mathbf F_p$ (at a geometric point $B\otimes\bar k$ is a product of copies of $\bar k$, where the roots of $X^p-X$ are exactly the constants in $\mathbf F_p$). The action is faithful, so $\mathrm{Aut}(Y/X_0)\cong\mathbf F_p$.

*Recorded in advance* from chapter *Fourier–Deligne transform* of the source.
