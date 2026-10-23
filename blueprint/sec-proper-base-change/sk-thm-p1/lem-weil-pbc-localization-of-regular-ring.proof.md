+++
kind = "proof"
of = "lem-weil-pbc-localization-of-regular-ring"
+++
Conditions (a)-(c) say that $\varphi$ is a localization of $R$ at $M$ in the usual sense: every element of $R'$ has the form $\varphi(r)\varphi(s)^{-1}$ (if $y=\varphi(r)u$ with $\varphi(s)u=1$, then $y\varphi(s)=\varphi(r)$), and $\varphi(x)=\varphi(y)$ implies $sx=sy$ for some $s\in M$ (apply (c) to $x-y$). By the uniqueness of localizations, $R'$ is therefore isomorphic as an $R$-algebra to $M^{-1}R$, so it suffices to show that $M^{-1}R$ is regular.

$M^{-1}R$ is Noetherian, being a localization of the Noetherian ring $R$ (ideals of $M^{-1}R$ are extended from ideals of $R$).

Let $\mathfrak p$ be a prime of $M^{-1}R$ and $\mathfrak q$ its contraction to $R$, a prime ideal disjoint from $M$. By transitivity of localization, $(M^{-1}R)_{\mathfrak p}$ is a localization of $R$ at the set of elements of $R$ whose image in $M^{-1}R$ lies outside $\mathfrak p$; these are exactly the elements outside $\mathfrak q$. Hence $(M^{-1}R)_{\mathfrak p}\cong R_{\mathfrak q}$, which is a regular local ring because $R$ is regular. Thus every localization of $M^{-1}R$ at a prime is regular local, and $M^{-1}R$ is regular.

Finally, regularity (Noetherianity together with the regular-local condition at every prime) is invariant under ring isomorphism, so $R'\cong M^{-1}R$ is regular.
