+++
kind = "proof"
of = "lem-weil-pbc-module-injects-localizations-associated-primes"
+++
Let $m\in M$ map to zero in every $M_{\mathfrak p}$ for $\mathfrak p\in\operatorname{Ass}(M)$, and suppose $m\ne0$. The cyclic submodule $N=Rm\subseteq M$ is nonzero. Since $0\cdot m=0$, the scalar $0$ is a zerodivisor on $N$; since over a Noetherian ring the set of zerodivisors on a module is the union of its associated primes, $0$ lies in some associated prime $\mathfrak p\in\operatorname{Ass}(N)$. Thus $\operatorname{Ass}(N)$ is nonempty.

Since associated primes of a submodule are associated primes of the module, the prime $\mathfrak p\in\operatorname{Ass}(N)$ chosen in Step 1 belongs to $\operatorname{Ass}(M)$. Hence the kernel assumption gives $m/1=0$ in $M_{\mathfrak p}$.

Because $\mathfrak p\in\operatorname{Ass}(N)$, choose $z\in N$ with $\operatorname{Ann}_R(z)=\mathfrak p$ and write $z=rm$ for some $r\in R$. By the definition of the localization, $m/1=0$ in $M_{\mathfrak p}$ means that some $s\in R\setminus\mathfrak p$ satisfies $sm=0$. Then $sz=srm=0$, so $s\in\operatorname{Ann}_R(z)=\mathfrak p$, a contradiction. Thus $m=0$; this includes the empty-product case, since a nonzero $m$ would have produced an associated prime in Step 1.
