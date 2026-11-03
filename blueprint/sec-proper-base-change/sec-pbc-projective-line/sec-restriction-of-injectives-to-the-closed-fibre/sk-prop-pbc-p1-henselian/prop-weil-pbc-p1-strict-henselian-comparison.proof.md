+++
kind  = "proof"
of    = "prop-weil-pbc-p1-strict-henselian-comparison"
+++
Only the underlying abelian sheaf of $F$ matters. *Reduction to a prime.* The
class of abelian sheaves for which the comparison holds in all degrees is closed
under extensions (five lemma in the long exact cohomology sequences on $X$ and
$X_0$) and under filtered colimits (cohomology of the quasi-compact
quasi-separated schemes $X$ and $X_0$ commutes with filtered colimits, as does
inverse image). A torsion sheaf is the filtered union of its subsheaves $F[n]$
[def-weil-pbc-torsion-etale-sheaf], a sheaf killed by $n$ is a finite extension of
sheaves killed by primes, so it suffices to treat an abelian sheaf $G$ with
$rG=0$ for a prime $r$, i.e. a sheaf of $\mathbf F_r$-modules.

*Sheaves of $\mathbf F_r$-modules.* Induction on $q$. Degree zero is
[lemma-weil-pbc-etale-degree-zero], $X$ being proper over the henselian local
ring $A$. For $q\geq1$ embed $G$ into an injective sheaf $I$ of
$\mathbf F_r$-modules and put $Q=I/G$. The underlying abelian sheaf of $I$ has no
higher cohomology on $X$, and $H^q(X_0,I_0)=0$ for $q>0$ by
[prop-weil-pbc-p1-acyclicity]. Inverse image is exact, so $0\to G_0\to I_0\to
Q_0\to0$ is exact, and the long exact sequences of $0\to G\to I\to Q\to0$ on $X$
and on $X_0$, connected by restriction, identify $H^q(X,G)$ and $H^q(X_0,G_0)$
with the cokernels of $H^{q-1}(X,I)\to H^{q-1}(X,Q)$ and
$H^{q-1}(X_0,I_0)\to H^{q-1}(X_0,Q_0)$; by the induction hypothesis for $I$ and
$Q$ in degree $q-1$, restriction is bijective on these cokernels. All maps are
restriction maps, so the isomorphisms are natural in $F$.
