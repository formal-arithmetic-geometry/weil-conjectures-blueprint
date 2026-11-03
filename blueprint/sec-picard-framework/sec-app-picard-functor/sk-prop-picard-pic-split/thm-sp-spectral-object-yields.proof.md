+++
kind  = "proof"
of    = "thm-sp-spectral-object-yields"
+++
Step 1: the exact couple. The short exact sequences $0\to F^{p+1}K^\bullet\to
F^pK^\bullet\to\operatorname{gr}^pK^\bullet\to0$ have long exact cohomology
sequences, exact by the long exact sequence of a short exact sequence of
complexes ([lem-sp-long-exact-of-triangle]), namely

$$
 \cdots\to H^{p+q}(F^{p+1}K^\bullet)\xrightarrow{\ \alpha\ }
 H^{p+q}(F^pK^\bullet)\xrightarrow{\ g\ }
 H^{p+q}(\operatorname{gr}^pK^\bullet)\xrightarrow{\ f\ }
 H^{p+q+1}(F^{p+1}K^\bullet)\to\cdots .
$$

They assemble into an exact couple [def-sp-exact-couple] with
$D^{p,q}=H^{p+q}(F^pK^\bullet)$ and
$E^{p,q}=H^{p+q}(\operatorname{gr}^pK^\bullet)$, the maps $\alpha,g,f$
having bidegrees $(-1,+1)$, $(0,0)$, $(+1,0)$; the exactness required of a
couple is exactly the exactness of these sequences.

Step 2: the pages. The spectral sequence of the couple, started at the page
$r_0=1$ ([def-sp-exact-couple]), is a spectral sequence
[def-sp-spectral-sequence] whose differentials $d_r=g_r\circ f_r$ have
bidegree $(+r,1-r)$. Its first page is $E_1=E$, and $d_1=g\circ f$ is the
connecting homomorphism followed by the projection, as stated in (a).

Step 3: convergence. Assume the filtration bounded and fix $n=p+q$. Then
$H^n(F^pK^\bullet)\to H^n(K^\bullet)$ is an isomorphism for $p\ll0$ (the
complexes agree in degrees $n-1,n,n+1$), and $H^n(F^pK^\bullet)=0$ for
$p\gg0$ (it is a subquotient of $F^pK^n=0$); hence $F^pH^n=H^n$ for $p\ll0$
and $F^pH^n=0$ for $p\gg0$, so the induced filtration is finite and
separated. In the couple, $E_r^{p,q}=Z_r/B_r$ with
$Z_r=f^{-1}(\operatorname{im}\alpha^{r-1})$ and
$B_r=g(\ker\alpha^{r-1})$ ([def-sp-convergence]). For $r$ large the source
$H^{n+1}(F^{p+r}K^\bullet)$ of $\alpha^{r-1}$ into $H^{n+1}(F^{p+1}K^\bullet)$
vanishes, so $Z_r=\ker f=\operatorname{im}g$, and
$\ker\bigl(\alpha^{r-1}:H^n(F^pK^\bullet)\to H^n(F^{p-r+1}K^\bullet)\bigr)$
is the kernel $\ker\iota$ of $\iota:H^n(F^pK^\bullet)\to H^n(K^\bullet)$; so
the differentials at $(p,q)$ vanish from then on, and

$$
 E_\infty^{p,q}=\frac{g\bigl(H^n(F^pK^\bullet)\bigr)}
 {g(\ker\iota)}\cong
 \frac{H^n(F^pK^\bullet)}{\ker\iota+\operatorname{im}\alpha}
 \cong\frac{\operatorname{im}\iota}{\iota(\operatorname{im}\alpha)}
 =\frac{F^pH^n(K^\bullet)}{F^{p+1}H^n(K^\bullet)},
$$

using $\ker g=\operatorname{im}\alpha$. The isomorphism is induced by
$\iota$, compatibly with $g$, which is the convergence of
[def-sp-convergence] to the image filtration
[def-sp-image-filtration]. This is (b).

Step 4: functoriality. A morphism of filtered complexes maps the short exact
sequences of Step 1 to each other, so it induces maps on
$H(F^pK^\bullet)$ and $H(\operatorname{gr}^pK^\bullet)$ which commute with
the maps induced by inclusions and projections and, by naturality of the
connecting homomorphism, with $f$; that is a morphism of exact couples, and
[lem-sp-couple-morphism] turns it into a morphism of spectral sequences. If it
is an isomorphism on $E_1$, it is an isomorphism on every page by
[lem-sp-page-induction]. This is (c).

Step 5: the first-quadrant variant. If $E_1^{p,q}=0$ outside the first
quadrant, so are all later pages, which are subquotients of $E_1$. On page
$r$ the differential leaving $(p,q)$ lands in $(p+r,q-r+1)$, outside the
quadrant once $r>q+1$, and the one arriving comes from $(p-r,q+r-1)$,
outside once $r>p$; so for $r>\max(p,q+1)$ the entry $(p,q)$ is stable, and
the pages $r\geq2$ form a first-quadrant cohomological spectral sequence. If
moreover $F^0H^n=H^n$ and $F^{n+1}H^n=0$, the isomorphisms
$E_\infty^{p,q}\cong\operatorname{gr}^pH^{p+q}(K^\bullet)$ of (b) for
$0\leq p\leq n$ exhibit $\bigl(H^n(K^\bullet)\bigr)_{n\geq0}$, with the
induced filtrations, as the abutment. This is (d).
