+++
kind = "proof"
of = "sk-thm-p1"
uses = ["sk-def-conv", "sk-def-ia", "sk-prop-pbc-p1-henselian", "sk-lem-pbc-curve-field-extension", "sk-def-pbc-conventions", "sk-thm-iff"]
+++
For a torsion sheaf $F$ in degree zero, the geometric stalks of both sides of
the exchange map are computed by the cohomology of $\mathbf P^1$ over strict
localizations. By the henselian comparison [sk-prop-pbc-p1-henselian] we may
replace these by the cohomology of $\mathbf P^1$ over the separably closed
residue fields, and [sk-lem-pbc-curve-field-extension] compares the latter. The case of
complexes then follows by truncation.

*Strict-local stalks.* For a quasi-compact quasi-separated $f:Z\to S$, a
geometric point $\bar s$, and an abelian étale sheaf $G$,

$$
(R^qf_*G)_{\bar s}\simeq H^q(Z\times_SS_{(\bar s)},G|),\qquad
S_{(\bar s)}=\operatorname{Spec}\cO^{\mathrm{sh}}_{S,\bar s}.
$$

Indeed, the stalk is the filtered colimit of $H^q(Z\times_SV,G|)$ over pointed
étale neighbourhoods $(V,\bar v)$ of $\bar s$, and étale cohomology
continuity identifies that colimit with the cohomology of the indicated limit
scheme (Stacks Project, Tag 03Q9).

*Torsion sheaves.* We first take a torsion sheaf $F$ in degree zero. Choose a
geometric point $\bar t:\operatorname{Spec}\Omega\to T$ and put
$\bar s=g\bar t$. The strict localizations fit into a natural map
$T_{(\bar t)}\to S_{(\bar s)}$ of strictly henselian local schemes. Write
$k_s,k_t$ for their residue fields; these are separably closed, and the map
induces an inclusion $k_s\hookrightarrow k_t$. For each $q\geq0$, the
strict-local stalk formula and [sk-prop-pbc-p1-henselian] give the
commutative diagram

$$
\begin{array}{ccc}
(g^{-1}R^qp_*F)_{\bar t} & \xrightarrow{\ \Ex_{\bar t}\ } & (R^qp'_*g'^{-1}F)_{\bar t}\\
\downarrow\wr & & \downarrow\wr\\
H^q(\mathbf P^1_{S_{(\bar s)}},F|) & \longrightarrow & H^q(\mathbf P^1_{T_{(\bar t)}},F|)\\
\downarrow\wr & & \downarrow\wr\\
H^q(\mathbf P^1_{k_s},F|) & \longrightarrow & H^q(\mathbf P^1_{k_t},F|).
\end{array}
$$

The top arrow $\Ex_{\bar t}$ is the stalk at $\bar t$ of the map of abelian
sheaves on $T_{\Et}$ induced by the derived exchange on $q$th cohomology
sheaves. The middle and bottom arrows are the natural pullback maps. The top
square commutes by the definition of exchange: a section over $\mathbf P^1_V$,
for a pointed étale neighbourhood $V\to S$, is pulled back to
$\mathbf P^1_{V\times_ST}$. Passing to the two strict localization limits
gives exactly the middle arrow. The bottom square is naturality of
restriction to the closed fibres.

The bottom arrow is an isomorphism by [sk-lem-pbc-curve-field-extension].
Hence every geometric stalk of $g^{-1}R^qp_*F\to R^qp'_*g'^{-1}F$ is an
isomorphism. Geometric stalks are conservative, so exchange for $F$ is an
isomorphism in $D^+(T_{\Et},\mathbf Z)$. Cohomology and higher direct image of
$\Lambda$-module sheaves agree with those of their underlying abelian sheaves
(see *Module and abelian cohomology* in [sk-def-pbc-conventions]),
so this also proves the assertion with the stated coefficient ring and its
module structure.

*Complexes.* Now let $K\in D^+(\mathbf P^1_{S,\Et},\Lambda)$ have torsion
cohomology and fix $m\in\mathbf Z$. The two functors
$g^{-1}Rp_*,\ Rp'_*g'^{-1}:D^+(\mathbf P^1_{S,\Et},\Lambda)\to
D^+(T_{\Et},\Lambda)$ send $D^{\geq m+1}$ into $D^{\geq m+1}$, since inverse
image is exact and direct image is left exact. The truncation triangle for
$\tau_{\leq m}K$ therefore reduces the degree-$m$ assertion to
$\tau_{\leq m}K$, which is bounded. Successive truncation triangles reduce
this bounded case to the shifted torsion sheaves $H^a(K)[-a]$. Exchange is
compatible with these triangles and has already been proved for those
sheaves. It follows that exchange is an isomorphism in every degree for $K$.

*Injective acyclicity.* Finally, if $I$ is a torsion injective sheaf of
$\Lambda$-modules, then $R^qp_*I=0$ for $q>0$. The sheaf case of the theorem
gives $R^qp'_*g'^{-1}I\simeq g^{-1}R^qp_*I=0$. This is
$\mathrm{IA}_\Lambda(p)$ of [sk-def-ia], which is condition 3 of [sk-thm-iff]
for $p$ when $\Lambda$ is torsion as an abelian group.
