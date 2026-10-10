+++
kind  = "proof"
of    = "lem-sp-grothendieck-enough-injectives"
+++
This is Grothendieck's theorem (Stacks Project, chapter Injectives, the
section on Grothendieck abelian categories). Let $\mathcal A$ be a
Grothendieck abelian category [def-sp-grothendieck-abelian] with generator
$U$.

**Step 1: a Baer criterion.** An object $I$ is injective as soon as every
morphism $V\to I$ from a subobject $V\subseteq U$ extends to $U$. Indeed,
let $A\subseteq B$ and $f:A\to I$. Consider pairs $(A',f')$ with
$A\subseteq A'\subseteq B$ and $f'|_A=f$, ordered by extension. The union of
a chain of such subobjects is their filtered colimit, which is again a
subobject of $B$ because filtered colimits are exact, and the $f'$ glue on
it; so Zorn's lemma gives a maximal pair $(A',f')$. If $A'\ne B$, then since
$U$ is a generator there is $u:U\to B$ whose image is not contained in $A'$.
Put $V:=u^{-1}(A')\subseteq U$; by hypothesis $f'\circ u|_V$ extends to
$h:U\to I$, and $f'$ and $h$ agree on $V$, so they define a morphism on
$A'+u(U)=\operatorname{coker}(V\to A'\oplus U)$ extending $f'$, contradicting
maximality. Hence $A'=B$.

**Step 2: the embedding.** The subobjects of $U$ form a set $\Sigma$. For an
object $M$ let $M\to M_1$ be the pushout of
$\bigoplus_{(V,\varphi)}V\hookrightarrow\bigoplus_{(V,\varphi)}U$ along
$\bigoplus\varphi:\bigoplus V\to M$, the sums running over all
$V\in\Sigma$ and $\varphi:V\to M$. It is a monomorphism, as a pushout of a
monomorphism in an abelian category, and every $\varphi:V\to M$ extends to
$U\to M_1$. Iterate transfinitely, $M_{\alpha+1}:=(M_\alpha)_1$ and
$M_\lambda:=\operatorname{colim}_{\alpha<\lambda}M_\alpha$ for limit
$\lambda$, up to a regular cardinal $\kappa>|\Sigma|$, and put
$I:=M_\kappa$. Since filtered colimits are exact, each $M\to M_\alpha$ is a
monomorphism. A morphism $\varphi:V\to I$ with $V\subseteq U$ factors
through some $M_\alpha$, $\alpha<\kappa$: the subobjects
$\varphi^{-1}(M_\alpha)$ of $V$ form an increasing chain with union $V$
(exactness of filtered colimits), indexed by $\kappa$, and taking values in
the set of subobjects of $V$, of cardinality $<\kappa$, so the chain is
stationary from some $\alpha<\kappa$ on, with value $V$. Then $\varphi$
extends to $U\to M_{\alpha+1}\to I$. By Step 1, $I$ is injective, and
$M\hookrightarrow I$. So $\mathcal A$ has enough injectives.
