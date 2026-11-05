+++
kind = "proof"
of = "proposition-proper-base-change-projective-line--1"
order = 380002
+++
Let $F$ be a torsion sheaf. Choose a geometric
point $\bar t:\operatorname{Spec}\Omega\to T$ and put
$\bar s=g\bar t$.  The strict localizations fit into a natural map
$T_{(\bar t)}\to S_{(\bar s)}$ of strictly henselian local schemes.
Write $k_s,k_t$ for their residue fields. These are separably closed,
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

The top arrow is the stalk at $\bar t$ of
the map induced by
(4.3) on $q$th cohomology sheaves. The middle and
bottom arrows are the natural pullback maps. The
top square commutes by the definition of the base change map: a section over
$\mathbf P^1_V$, for a pointed étale neighbourhood $V\to S$, is pulled
back to $\mathbf P^1_{V\times_ST}$, and passing to the limits over the two strict
localizations gives exactly the middle arrow. The bottom square commutes
by naturality of restriction to the closed fibres.

The vertical arrows are isomorphisms. The upper ones are isomorphisms by
(4.12), applied to $\pi$ and to $\pi'$; here
$\mathbf P^1_{S_{(\bar s)}}$ and $\mathbf P^1_{T_{(\bar t)}}$ are the base
changes of $\mathbf P^1_S$ and $\mathbf P^1_T$ to the strict
localizations. The lower ones are isomorphisms by Proposition [proposition-cohomology-p-1-over-henselian],
applied to the strictly henselian local rings of $S_{(\bar s)}$ and
$T_{(\bar t)}$. Hence the top arrow is an isomorphism as soon as the bottom
arrow is. The bottom arrow is an isomorphism by
Lemma [lemma-extension-separably-closed-ground-field], applied to $C=\mathbf P^1_{k_s}$ and
the extension $k_s\subseteq k_t$. Thus every geometric stalk
of $g^*R^q\pi_*F\to R^q\pi'_*g'^*F$ is an isomorphism.
As geometric stalks are conservative, the base change map for $F$ is an
isomorphism in $D^+(T_{\acute{e}t},\mathbf Z)$. Cohomology and higher direct images
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

*Source:* the proof of Proposition [proposition-proper-base-change-projective-line].
