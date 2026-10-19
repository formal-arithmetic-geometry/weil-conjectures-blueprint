+++
kind  = "proof"
of    = "thm-sp-if-e1"
+++
*The couple.* The sequences
$0\to\sigma_{\geq s+1}K^\bullet\to\sigma_{\geq s}K^\bullet\to K^s[-s]\to0$
are split in each degree, so they give distinguished triangles
$\sigma_{\geq s+1}K^\bullet\to\sigma_{\geq s}K^\bullet\to K^s[-s]\to
\sigma_{\geq s+1}K^\bullet[1]$. The derived functor $Rv$ of
[def-sp-kinjective-bridge], computed by K-injective resolutions, is
well defined, functorial and compatible with shifts
([lem-sp-kinjective-computes]), and it carries these triangles to
distinguished triangles. Cohomology is a homological functor, so
[lem-sp-long-exact-of-triangle] gives the long exact sequences

$$
 \cdots\to\mathcal H^n(Rv\,\sigma_{\geq s+1}K^\bullet)\xrightarrow{\ \alpha\ }
 \mathcal H^n(Rv\,\sigma_{\geq s}K^\bullet)\xrightarrow{\ g\ }
 \mathcal H^n(Rv(K^s[-s]))\xrightarrow{\ f\ }
 \mathcal H^{n+1}(Rv\,\sigma_{\geq s+1}K^\bullet)\to\cdots,
$$

which form an exact couple [def-sp-exact-couple] in the indices $(s,n)$, with
$\alpha$, $g$, $f$ of degrees $(-1,0)$, $(0,0)$, $(1,1)$.

*The first page.* By the shift compatibility (3) of
[lem-sp-kinjective-computes],
$\mathcal H^n(Rv(K^s[-s]))\cong\mathcal H^{n-s}(Rv(K^s[0]))$, which is
$R^{n-s}v(K^s)$ by part (2) of the same lemma, the derived functor of
[def-sp-left-exact-additive]. The differential $d_1=g\circ f$ is induced by
the composite of the boundary $K^s[-s]\to\sigma_{\geq s+1}K^\bullet[1]$ of the
split sequence with the projection
$\sigma_{\geq s+1}K^\bullet[1]\to K^{s+1}[-s]$; this composite is the map of
complexes concentrated in one degree given by $d_K:K^s\to K^{s+1}$, so
$d_1=R^rv(d_K)$.

*Convergence.* Let $K^m=0$ for $m<m_0$. For $s\leq m_0$ one has
$\sigma_{\geq s}K^\bullet=K^\bullet$, so the maps
$\iota:D^{s,n}\to\mathcal H^n(RvK^\bullet)$ induced by
$\sigma_{\geq s}K^\bullet\to K^\bullet$ are isomorphisms. For $s>n$, the
complex $\sigma_{\geq s}K^\bullet$ has a K-injective resolution by a complex
of injectives concentrated in degrees $\geq s$ ([def-sp-kinjective-bridge]),
so $D^{s,n}=0$. Thus in each total degree the couple is bounded, and the
computation of the stable terms is the one for a bounded filtered complex: at
a fixed $(s,n)$, for $r$ large the source of $\alpha^{r-1}$ into
$D^{s+1,n+1}$ vanishes and $\ker\bigl(\alpha^{r-1}\text{ on }D^{s,n}\bigr)=
\ker\iota$, so the differentials at $(s,n)$ vanish and the stable term is
$g(D^{s,n})/g(\ker\iota)\cong\operatorname{im}\iota/\iota(\operatorname{im}
\alpha)$, the graded piece of the image filtration, compatibly with $g$ and
$\iota$. This is the convergence of [def-sp-convergence].

*Independence.* By part (1) of [lem-sp-kinjective-computes], $RvK^\bullet$
and hence $\mathcal H^n(RvK^\bullet)$ do not depend, up to canonical
isomorphism, on the chosen K-injective resolution.
