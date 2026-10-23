+++
kind  = "proof"
of    = "lemma-weil-pbc-gabber-effacement"
uses = ["def-weil-pbc-torsion-etale-sheaf", "lemma-weil-pbc-constructible-approximation", "lemma-weil-pbc-constructible-finite-pushforward", "lemma-weil-pbc-pushout-monicity", "lemma-weil-pbc-etale-degree-zero"]
+++
*Step 1: a bounded representative.* $F$ is the filtered union of its subsheaves
$F[n]$ killed by $n$ [def-weil-pbc-torsion-etale-sheaf], inverse image to $T_0$
commutes with this colimit, and cohomology of the quasi-compact quasi-separated
scheme $T_0$ commutes with filtered colimits. Hence there are a sheaf of
$\Lambda$-modules $G$ with $nG=0$ for some $n\geq1$, a morphism $b:G\to F$ and a
class $z\in H^q(T_0,G_0)$ with $b_0(z)=c$.

*Step 2: lifting $z$ to $T$.* For an abelian sheaf $G$ killed by $n$, restriction
$H^q(T,G)\to H^q(T_0,G_0)$ is surjective. Indeed, regard $G$ as a sheaf of
$\mathbf Z/n$-modules. A closed-fibre class of a $\mathbf Z/n$-sheaf comes from a
constructible $\mathbf Z/n$-sheaf $C$ mapping to it
[lemma-weil-pbc-constructible-approximation]; $C$ embeds into a finite sum of
direct images of finite constant sheaves along finite finitely presented maps
[lemma-weil-pbc-constructible-finite-pushforward]; each component of the class is
killed by a finite finitely presented cover;
pushing out along $C\to G$ [lemma-weil-pbc-pushout-monicity] gives a
monomorphism of $\mathbf Z/n$-sheaves $G\hookrightarrow G'$ killing the class.
With this effacement, induction on $q$ in the long exact cohomology sequences of
$0\to G\to G'\to G'/G\to0$ on $T$ and on $T_0$ (degree zero being
[lemma-weil-pbc-etale-degree-zero]) shows that restriction is bijective for all
$\mathbf Z/n$-sheaves in all degrees, in particular surjective. Choose
$x\in H^q(T,G)$ restricting to $z$.

*Step 3: an acyclic target.* Embed $G$ into an injective sheaf $J$ of
$\Lambda$-modules and let $E=\ker(n:J\to J)$. Since $nG=0$ the embedding factors
through a monomorphism $a:G\hookrightarrow E$. The sheaf $E$ is killed by $n$,
hence torsion, and $H^q(T,E)=0$ for $q>0$: $E$ is an injective sheaf of
$\Lambda/n$-modules, because $\operatorname{Hom}_{\Lambda/n}(-,E)=
\operatorname{Hom}_\Lambda(-,J)$ on sheaves of $\Lambda/n$-modules, and injective
sheaves of modules are acyclic. Therefore the image of $z$ in
$H^q(T_0,E_0)$, which is the restriction of the image of $x$ in $H^q(T,E)=0$,
vanishes.

*Step 4: pushout.* Let $F'=F\amalg_GE$ be the pushout of $b$ and $a$. Since $a$ is
a monomorphism, so is $F\to F'$ [lemma-weil-pbc-pushout-monicity], and $F'$ is a
quotient of the torsion sheaf $F\oplus E$, hence torsion. The image of
$c=b_0(z)$ in $H^q(T_0,F'_0)$ equals the image of $a_0(z)=0$ under
$E\to F'$, so it is zero.
