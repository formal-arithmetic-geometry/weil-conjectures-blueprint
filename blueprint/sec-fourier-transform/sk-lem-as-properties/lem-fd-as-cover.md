+++
id = "lem-fd-as-cover"
kind = "lemma"
title = "The Artin–Schreier covering"
lean = ["AlgebraicGeometry.Etale.exists_eq_artinSchreierTranslation_of_comp_artinSchreierMap"]
order = 3929
uses = ["def-fd-artin-schreier-sheaf", "def-weil-pbc-etale-site"]
+++
Let $X_0$ be a scheme of characteristic $p$ and $f\in\Gamma(X_0,\mathcal O_{X_0})$. The morphism $\pi:Y\to X_0$, $\operatorname{Spec}\mathcal O_{X_0}[T]/(T^p-T-f)\to X_0$ (the Artin–Schreier covering of $f$, i.e. the pullback along $f$ of $\mathrm{AS}_p$ of [def-fd-artin-schreier-sheaf] for $k=\mathbf F_p$), is finite etale of degree $p$; the translations $\sigma_a:T\mapsto T+a$ ($a\in\mathbf F_p$) are automorphisms of $Y$ over $X_0$ acting simply transitively on every geometric fibre, so they make $Y$ an $\mathbf F_p$-torsor over $X_0$. The resulting map $\mathbf F_p\to\mathrm{Aut}(Y/X_0)$ is injective, the automorphisms of $Y$ as an $\mathbf F_p$-torsor (those commuting with the $\sigma_a$) are $\Gamma(X_0,\mathbf F_p)$, and $\mathbf F_p\to\mathrm{Aut}(Y/X_0)$ is an isomorphism when $Y$ is connected. It is not an isomorphism in general: for $f=0$ the cover $Y\cong\coprod_{a\in\mathbf F_p}X_0$ is split, and for $p=3$, $X_0=\operatorname{Spec}\mathbf F_3$ the full automorphism group of $Y$ over $X_0$ is $S_3$.
