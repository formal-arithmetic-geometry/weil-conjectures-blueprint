+++
kind = "proof"
of = "sk-thm-p1"
uses = ["sk-def-conv", "sk-def-ia", "sk-prop-pbc-p1-henselian", "sk-lem-pbc-curve-field-extension", "sk-def-pbc-conventions", "sk-thm-iff", "sk-cor-curve-invariance"]
+++
We first treat a torsion sheaf $F$. Choose a geometric
point $\bar t:\operatorname{Spec}\Omega\to T$ and put
$\bar s=g\bar t$. The strict localizations fit into a natural map
$T_{(\bar t)}\to S_{(\bar s)}$ of strictly henselian local schemes.
Write $k_s,k_t$ for their residue fields. These are separably closed,
and the map induces an inclusion $k_s\hookrightarrow k_t$.
For each $q\geq0$, using (4.11) and
Proposition [sk-prop-pbc-p1-henselian], we obtain the commutative diagram

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

The top arrow is the stalk at $\bar t$ of
the map induced by
(4.3) on $q$th cohomology sheaves. The middle and
bottom arrows are the natural pullback maps. The
top square commutes by the definition of the base change map: a section over
$\mathbf P^1_V$, for a pointed étale neighbourhood $V\to S$, is pulled
back to $\mathbf P^1_{V\times_ST}$, and passing to the limits over the two strict
localizations gives exactly the middle arrow. The bottom square commutes
by naturality of restriction to the closed fibres.

The bottom arrow is an isomorphism by
Lemma [sk-cor-curve-invariance], so every geometric stalk
of $g^*R^q\pi_*F\to R^q\pi'_*g'^*F$ is an isomorphism.
As geometric stalks are conservative, the base change map for $F$ is an
isomorphism in $D^+(T_{\acute{e}t},\mathbf Z)$. Since cohomology and higher direct images
of sheaves of $\Lambda$-modules agree with those of their underlying abelian
sheaves (see the remark after Convention [sk-def-pbc-conventions]), the
base change map for $F$ is also an isomorphism in $D^+(T_{\acute{e}t},\Lambda)$.

Now let
$K\in D^+(\mathbf P^1_{S,\acute{e}t},\Lambda)$ have torsion cohomology and
fix $m\in\mathbf Z$. The two functors
$g^*R\pi_*,\ R\pi'_*g'^*:D^+(\mathbf P^1_{S,\acute{e}t},\Lambda)\to D^+(T_{\acute{e}t},\Lambda)$ send $D^{\geq m+1}$ into $D^{\geq m+1}$, since inverse image is exact and derived direct image is
left $t$-exact. Using the truncation triangle for $\tau_{\leq m}K$,
we can therefore reduce the assertion in degree $m$ to the bounded complex $\tau_{\leq m}K$,
and then, by induction on the length using the truncation triangles and
naturality of the base change map, to the
shifted torsion sheaves $H^a(K)[-a]$. For these we have already proved the assertion,
so the base change map for $K$ is an isomorphism in every degree.

Finally, if $I$ is a torsion injective sheaf of $\Lambda$-modules, then
$R^q\pi_*I=0$ for $q>0$. By the case of sheaves, we get
$R^q\pi'_*g'^*I\simeq g^*R^q\pi_*I=0$. This is $\mathrm{IA}_\Lambda(\pi)$.
