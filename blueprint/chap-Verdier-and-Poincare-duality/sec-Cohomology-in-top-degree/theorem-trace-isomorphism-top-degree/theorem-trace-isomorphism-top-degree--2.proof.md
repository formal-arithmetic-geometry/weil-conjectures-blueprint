+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--2"
order = 866005
+++
A sheaf placed in degree zero has no cohomology in negative degrees. By
clause [proposition-pro-etale-site-separably-closed--3], $\mathcal C_A$ is the constant pro-étale sheaf with
value $A$, that is, $\nu_S^*$ of the constant étale sheaf $A$, since inverse
image preserves constant sheaves. Let $N$ be the order of $A$. By
Theorem [theorem-bounded-below-cohomology-comparison], in the form of
clause [theorem-bounded-below-cohomology-comparison--3] with $\Lambda=\mathbf Z/N$, we have
$H^i(S_{\mathrm{pro}\acute{e}t},\mathcal C_A)=H^i(S_{\acute{e}t},A)$. Write $A=\bigoplus_\ell A_\ell$
as the sum of its $\ell$-primary parts, for the finitely many primes $\ell$
dividing $N$, all different from the characteristic of $k'$. Étale
cohomology commutes with finite direct sums, so we may assume that $A$ is
$\ell$-primary. Let $\bar k$ be an algebraic closure of $k'$. Since $k'$ is
separably closed, $\bar k/k'$ is purely inseparable, so
$S_{\bar k}=S\times_{k'}\bar k$ has the same étale topos and the same
dimension as $S$. By [sga4, X, Cor. 4.3],
$\operatorname{cd}_\ell(S_{\bar k})\le2\dim S_{\bar k}\le2d$. Hence
$H^i(S_{\acute{e}t},A)=0$ for $i>2d$.

For the last assertion, $X$ is of finite type and of dimension $d$ over the
algebraically closed field $k$, and for the finite coefficient ring $A$ the
coefficient sheaf $A_X$ is $\mathcal C_A$ by clause [proposition-pro-etale-site-separably-closed--3]. The order
of $A$ is a power of $\ell$, which is invertible in $k$.

*Source:* the proof of Theorem [theorem-trace-isomorphism-top-degree].
