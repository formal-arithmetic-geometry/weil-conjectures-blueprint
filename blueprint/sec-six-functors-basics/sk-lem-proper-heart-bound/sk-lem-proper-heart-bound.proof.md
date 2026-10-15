+++
kind = "proof"
of = "sk-lem-proper-heart-bound"
uses = ["sk-lem-coefficient-heart", "sk-thm-sfb-qlbar-two-colimit", "sk-lem-stratified-lattice", "sk-prop-pe-milnor", "sk-cor-pe-bounded-continuity", "sk-thm-sfb-proper-base-change", "sk-prop-ind-heart"]
+++
*Reduction to a lattice.* The vanishing of $R^qp_*$ for $q>2d+1$ is stable under extensions. By part (3)
of [sk-lem-coefficient-heart], every $M\in\Cons(X,\Lambda)$ is a finite extension of sheaves $a_!L$, with
$a\colon S\hookrightarrow X$ a locally closed immersion and $L$ lisse. For $\Lambda=\Qlb$, $L$ is the scalar
extension $\overline{\mathbf Q}_{\ell,X}\otimes_{E}L_E$ of a lisse $E_S$-module $L_E$ for some finite $E/\mathbf Q_\ell$
([sk-thm-sfb-qlbar-two-colimit]); for $\Lambda=E$ put $L_E=L$. By [sk-lem-stratified-lattice], after
refining $S$ by a finite stratification (which replaces $a_!L$ by a finite extension of sheaves of the
same form), $L_E$ contains a lisse finite free $\mathcal O_{E,S}$-lattice $L_0$ with $L_0[1/\ell]=L_E$. It is
therefore enough to prove the bound for $a_!L_0$, and then to pass to $a_!L_E=(a_!L_0)[1/\ell]$ and, if
$\Lambda=\Qlb$, to its scalar extension $a_!L$ ([det-proper-heart-bound-reduction]).

The sheaf $a_!L_0$ is derived $\pi_E$-complete. Indeed $a$ is a closed immersion composed with a
quasi-compact open immersion; closed pushforward is exact and preserves products (Stacks, Tag 09BM), and
extension by zero is exact and preserves limits (Stacks, Tag 09BP). So both preserve the derived inverse
limit that expresses the completeness of $L_0$.

*The torsion bound.* Fix an affine weakly contractible $V\to Y$ and let $p_V\colon X_V\to V$ be the base
change of $p$; it is proper, with the same bound $d$. Since $L_0$ is flat,
$a_!L_0\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\pi_E^n$ is the sheaf $a_!(L_0/\pi_E^n)$, which is a classical
constructible étale sheaf of $\mathcal O_E/\pi_E^n$-modules pulled back to the pro-étale site. The proper
vanishing theorem (Stacks, Tag 095U) says that for a proper morphism whose fibres have dimension at most
$d$ the higher direct images $R^qp_*$ of torsion sheaves vanish for $q>2d$; it applies over the
non-Noetherian scheme $V$. Together with the comparison (Stacks, Tag 09A6) of étale and pro-étale direct
images, it shows that $R^qp_{V,*}$ of this sheaf vanishes for $q>2d$. As $V$ is weakly contractible,
$\Gamma(V,-)$ is exact on all pro-étale sheaves (Stacks, Tag 0991), so $H^q(X_V,-)=\Gamma(V,R^qp_{V,*}(-))$ and

$$
H^q\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)=0\quad(q>2d)
$$

([det-proper-heart-bound-torsion]).

*The limit.* Restriction to $X_V$ is exact and commutes with products, hence with derived inverse limits,
so completeness gives $(a_!L_0)|_{X_V}\simeq R\varprojlim_n a_!(L_0/\pi_E^n)|_{X_V}$. Derived global
sections also commute with derived inverse limits: a product of K-injective complexes is K-injective and
sections preserve products. The Milnor exact sequence ([sk-prop-pe-milnor])

$$
0\to\varprojlim^1_nH^{q-1}\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)\to H^q(X_V,a_!L_0)
\to\varprojlim_nH^q\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)\to0
$$

then gives $H^q(X_V,a_!L_0)=0$ for $q>2d+1$ ([det-proper-heart-bound-lattice]).

*Back to $\Lambda$.* The sheaf $(a_!L_0)[1/\ell]$ is the filtered colimit of $a_!L_0$ along multiplication
by $\ell$, so [sk-cor-pe-bounded-continuity] gives the same vanishing for it. For $\Lambda=\Qlb$, scalar
extension from $E$ to $\Qlb$ is the filtered colimit of the extensions to finite $F\supset E$; as sheaves
of abelian groups each of these is a finite direct sum of copies of the original sheaf, because $F$ is
finite free over $E$. The continuity lemma again gives the bound. Since this holds for every affine weakly
contractible $V$, the formula $(R^qp_*M)(V)=H^q(X_V,M|_{X_V})$ from the proof of
[sk-cor-pe-bounded-continuity] gives $R^qp_*(a_!L)=0$ for $q>2d+1$, and by the first step $R^qp_*M=0$
for $q>2d+1$ and every $M\in\Cons(X,\Lambda)$ ([det-proper-heart-bound-rational]).

*Passage to $\IndCons(X,\Lambda)$.* By [sk-thm-sfb-proper-base-change], $Rp_*$ maps $\Dbc(X,\Lambda)$ into
$\Dbc(Y,\Lambda)$, so $R^qp_*M\in\Cons(Y,\Lambda)$ for constructible $M$. Every object of
$\IndCons(X,\Lambda)$ is a filtered colimit of constructible sheaves, and $R^qp_*$ commutes with filtered
colimits and direct sums by [sk-cor-pe-bounded-continuity]. This gives all three assertions
([det-proper-heart-bound-indcons]).
