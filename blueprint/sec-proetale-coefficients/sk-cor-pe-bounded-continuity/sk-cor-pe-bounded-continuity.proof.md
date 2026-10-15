+++
kind = "proof"
of = "sk-cor-pe-bounded-continuity"
uses = ["sk-prop-pe-hypercover", "sk-cor-pe-sections", "sk-cor-pe-wc-sections"]
+++
Use one hypercover $W_\bullet$ for all $i$ ([sk-prop-pe-hypercover]). By
[sk-cor-pe-sections], sections on each $W_r$ commute with filtered colimits, hence so does
the finite sum in each total degree of the hypercover complex. Filtered colimits of modules
are exact, which gives the first assertion ([det-pe-bounded-continuity-sections]). For
direct images, evaluate the cohomology presheaves on affine objects $V$ of
$Y_{\mathrm{proét}}$: each $X\times_YV$ is quasi-compact and quasi-separated, so the first
assertion applies, and sheafification commutes with colimits
([det-pe-bounded-continuity-direct-image]).

In more detail, the functor $M\mapsto M(W_r)$ is exact ([sk-cor-pe-wc-sections]) and commutes
with direct sums ([sk-cor-pe-sections]). An exact additive functor that commutes with direct sums
commutes with all colimits, since a colimit $\varinjlim_jM_j$ is the cokernel of
$\bigoplus_{(j\to j')}M_j\to\bigoplus_jM_j$. In total degree $q$ the hypercover complex is
$\bigoplus_{n+m=q}K_i^m(W_n)$ with $n\ge0$ and $m\ge a$, a finite direct sum with
$0\le n\le q-a$; this is where the common lower bound $a$ is used. Hence the total complex of
$\varinjlim_iK_i^\bullet$ is the filtered colimit of the total complexes, and filtered
colimits of abelian groups are exact. None of this uses the particular ring sheaf
$\mathcal R$, so the argument applies verbatim to any sheaf of rings $A$ on the pro-étale
site of a quasi-compact quasi-separated scheme, which gives the Complement
([det-lem-bounded-continuity-sections], [det-lem-bounded-continuity-direct-image]).

For a single sheaf $M$ in degree $0$ ($a=0$) the hypercover complex is
$M(Z_0)\to M(Z_1)\to\cdots$, and each term commutes with filtered colimits and direct sums,
as does cohomology of complexes of abelian groups
([det-proper-heart-continuity-sections], [det-proper-heart-continuity-cohomology]). For
$R^qp_*$, let $V\to Y$ be affine weakly contractible and $X_V=X\times_YV$, which is
quasi-compact and quasi-separated. Since $\Gamma(V,-)$ is exact,
$(R^qp_*M)(V)=H^q((X_V)_{\mathrm{proét}},M|_{X_V})$; restriction to $X_V$ preserves colimits, so
the comparison map for $R^qp_*$ is an isomorphism on sections over every such $V$. These $V$
form a basis of the site, so evaluation on them detects isomorphisms of sheaves
([sk-cor-pe-sections], [det-proper-heart-continuity-direct-image]). Direct sums are handled in
the same way, or as filtered colimits of finite subsums.
