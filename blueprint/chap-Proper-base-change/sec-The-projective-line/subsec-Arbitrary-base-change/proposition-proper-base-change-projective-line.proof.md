+++
kind = "proof"
of = "proposition-proper-base-change-projective-line"
order = 381
uses = ["proposition-proper-base-change-projective-line--1", "lemma-cohomology-modules-underlying-abelian", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "prose-04-28", "proposition-cohomology-p-1-over-henselian", "lemma-extension-separably-closed-ground-field", "theorem-pbc-injective-acyclicity"]
+++
For a torsion sheaf we compare the two sides on geometric stalks. Both
stalks are the cohomology of a projective line over a separably closed
field, and the base change map becomes the pullback along a field
extension. Bounded below complexes then follow by truncation.

Let $F$ be a torsion sheaf. Choose a geometric
point $\bar t:\operatorname{Spec}\Omega\to T$ and put
$\bar s=g\bar t$. Then the strict localizations fit into a natural map
$T_{(\bar t)}\to S_{(\bar s)}$ of strictly henselian local schemes.
Write $k_s,k_t$ for their residue fields; these are separably closed,
and the map induces an inclusion $k_s\hookrightarrow k_t$.
For each $q\geq0$, using (4.12) and
Proposition [proposition-cohomology-p-1-over-henselian], we obtain the commutative diagram

$$
\begin{CD}
(g^*R^q\pi_*F)_{\bar t}
@>>>
(R^q\pi'_*g'^*F)_{\bar t}\\
@V{\sim}VV @VV{\sim}V\\
H^q(\mathbf P^1_{S_{(\bar s)}},F|)
@>>> H^q(\mathbf P^1_{T_{(\bar t)}},F|)\\
@V{\sim}VV @VV{\sim}V\\
H^q(\mathbf P^1_{k_s},F|)
@>>> H^q(\mathbf P^1_{k_t},F|).
\end{CD}
$$

Here the top arrow is the stalk at $\bar t$ of
the map induced by
(4.3) on $q$th cohomology sheaves, while the middle and
bottom arrows are the natural pullback maps. The
top square commutes by the definition of the base change map: a section over
$\mathbf P^1_V$, for a pointed étale neighbourhood $V\to S$, is pulled
back to $\mathbf P^1_{V\times_ST}$, and passing to the limits over the two strict
localizations gives exactly the middle arrow. The bottom square commutes
by naturality of restriction to the closed fibres.

The vertical arrows are isomorphisms: the upper ones by
(4.12), applied to $\pi$ and to $\pi'$; here
$\mathbf P^1_{S_{(\bar s)}}$ and $\mathbf P^1_{T_{(\bar t)}}$ are the base
changes of $\mathbf P^1_S$ and $\mathbf P^1_T$ to the strict
localizations. The lower ones are isomorphisms by Proposition [proposition-cohomology-p-1-over-henselian],
applied to the strictly henselian local rings of $S_{(\bar s)}$ and
$T_{(\bar t)}$. Hence the top arrow is an isomorphism as soon as the bottom
arrow is, and the bottom arrow is an isomorphism by
Lemma [lemma-extension-separably-closed-ground-field], applied to $C=\mathbf P^1_{k_s}$ and
the extension $k_s\subseteq k_t$. Thus every geometric stalk
of $g^*R^q\pi_*F\to R^q\pi'_*g'^*F$ is an isomorphism.
As geometric stalks are conservative, the base change map for $F$ is an
isomorphism in $D^+(T_{\acute{e}t},\mathbf Z)$. Moreover, cohomology and higher direct images
of sheaves of $\Lambda$-modules agree with those of their underlying abelian
sheaves (Lemma [lemma-cohomology-modules-underlying-abelian]).
Hence the base change map for $F$ is also an isomorphism in $D^+(T_{\acute{e}t},\Lambda)$.

Now let
$K\in D^+(\mathbf P^1_{S,\acute{e}t},\Lambda)$ have torsion cohomology and
fix $m\in\mathbf Z$. The two functors
$g^*R\pi_*,\ R\pi'_*g'^*:D^+(\mathbf P^1_{S,\acute{e}t},\Lambda)\to
D^+(T_{\acute{e}t},\Lambda)$ send $D^{\geq m+1}$ into $D^{\geq m+1}$, since inverse image is exact and derived direct image is
left $t$-exact. Using the truncation triangle for $\tau_{\leq m}K$,
we can therefore reduce the assertion in degree $m$ to the bounded complex $\tau_{\leq m}K$.
By induction on the length, using the truncation triangles and
naturality of the base change map, we reduce further to the
shifted torsion sheaves $H^a(K)[-a]$. For these the assertion has already been proved.

For $\mathrm{IA}_\Lambda(\pi)$, let $I$ be a torsion injective sheaf of
$\Lambda$-modules. Then $R^q\pi_*I=0$ for $q>0$, and the case of sheaves gives
$R^q\pi'_*g'^*I\simeq g^*R^q\pi_*I=0$.
