+++
kind  = "proof"
of    = "det-compact-trace-perfect-at-point"
uses  = ["det-compact-trace-point-objects"]
+++
The ring $A$ is Noetherian, so $C$ has a bounded-above resolution
$P^\bullet\to C$ by finite free $A$-modules. Suppose $C$ has Tor amplitude in
$[a,b]$, and truncate $P^\bullet$ below the Tor bound: replace the terms in
degrees $\le a$ by the single module $Q=\operatorname{coker}(P^{a-1}\to P^a)$
in degree $a$. The remaining last syzygy $Q$ is finitely presented, and it is
flat because $C$ has no Tor in degrees below $a$; hence $Q$ is projective. The
truncated complex is a bounded complex of finite projective $A$-modules
quasi-isomorphic to $C$
([Stacks, Tag 0658](https://stacks.math.columbia.edu/tag/0658)).

For the consequence: at the geometric point $s$ an object of $\Dctf(s,A)$ is a
bounded complex with finitely generated cohomology modules and finite Tor
amplitude. By [det-compact-trace-point-objects] this applies to
$R\Gamma_c(X,K)$ and to every geometric stalk $K_{\bar x}$.
