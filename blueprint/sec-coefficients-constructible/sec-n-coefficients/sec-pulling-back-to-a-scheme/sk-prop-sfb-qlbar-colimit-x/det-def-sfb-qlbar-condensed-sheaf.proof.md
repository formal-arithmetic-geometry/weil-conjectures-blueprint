+++
kind = "proof"
of = "det-def-sfb-qlbar-condensed-sheaf"
+++
**A criterion for subpresheaves.** Let $G\subseteq F$ be a subpresheaf of a sheaf $F$ (of sets) on a
site. Suppose that for every object $S$, every covering sieve $R$ on $S$ and every $a\in F(S)$ whose
restrictions $a|_{T}$ along all arrows $T\to S$ of $R$ lie in $G(T)$, we have $a\in G(S)$. Then $G$
is a sheaf. Indeed, a compatible family $(a_T\in G(T))_{T\in R}$ is compatible in $F$, so it glues
uniquely to $a\in F(S)$ with $a|_T=a_T\in G(T)$; by the hypothesis $a\in G(S)$; and uniqueness in $G$
follows from uniqueness in $F$.

**Verification.** $F=C(-,\Qlb)$ is a sheaf by [def-sfb-continuous-map-condensed-ring]. In the
coherent topology on profinite sets, a covering sieve $R$ on $S$ contains a finite family
$\pi_\nu\colon S_\nu\to S$, $\nu=1,\dots,n$, with $\coprod_\nu S_\nu\to S$ surjective. Let
$a\in C(S,\Qlb)$ with $a\circ\pi_\nu\in\underline{\Qlb}(S_\nu)$, say $a(\pi_\nu(S_\nu))\subseteq E_\nu$.
By surjectivity,
$$
a(S)=\bigcup_\nu a(\pi_\nu(S_\nu))\subseteq E_1\cdots E_n,
$$
which is a finite subextension by [det-def-sfb-qlbar-condensed-subextensions]. So
$a\in\underline{\Qlb}(S)$, and $\underline{\Qlb}$ is a sheaf of sets; since its ring operations are
those of the subpresheaf of rings, it is a sheaf of commutative rings.

By [det-def-sfb-ring-object-sheaf], its underlying abelian sheaf is a ring object, commutative
because all $\underline{\Qlb}(S)$ are commutative.
