+++
id = "thm-sp-spectral-object-yields"
kind = "theorem"
title = "The spectral sequence of a filtered complex"
lean = ["CategoryTheory.DecreasingFiltration.exactCouple", "CategoryTheory.DecreasingFiltration.exactCouple_d", "CategoryTheory.DecreasingFiltration.homologyFiltration", "CategoryTheory.DecreasingFiltration.convergesTo_exactCouple"]
order = 521
uses = ["def-sp-convergence", "def-sp-exact-couple", "def-sp-filtration", "def-sp-spectral-sequence", "lem-sp-couple-morphism", "lem-sp-long-exact-of-triangle", "lem-sp-page-induction"]
+++
Let $\mathcal A$ be an abelian category and let $K^\bullet$ be a complex in
$\mathcal A$ equipped with a decreasing filtration
[def-sp-filtration] $F^\bullet K^\bullet$ by subcomplexes which is *bounded*:
for every degree $n$ one has $F^pK^n=K^n$ for $p\ll0$ and $F^pK^n=0$ for
$p\gg0$. For $p\leq q$ put

$$
 X^{[p,q]}:=F^pK^\bullet/F^qK^\bullet ,
$$

so that $0\to X^{[q,r]}\to X^{[p,r]}\to X^{[p,q]}\to0$ is a short exact
sequence of complexes for $p\leq q\leq r$. Then:

- (a) there is a cohomological spectral sequence [def-sp-spectral-sequence]
  $\bigl(E_r^{p,q},d_r\bigr)_{r\geq1}$ with
  $$
   E_1^{p,q}=H^{p+q}\bigl(X^{[p,p+1]}\bigr)
   =H^{p+q}\bigl(\operatorname{gr}^pK^\bullet\bigr),
   \qquad
   d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1},
  $$
  the differential $d_1$ being the boundary homomorphism of the long exact
  cohomology sequence of the displayed short exact sequence with $(p,q,r)$
  replaced by $(p,p+1,p+2)$, and with, for every $r\geq1$ and every $N\geq
  r$, $E_r^{p,q}\cong Z_r^{p,q}/B_r^{p,q}$, where
  $$
  \begin{gathered}
  Z_r^{p,q}=\operatorname{im}\bigl(H^{p+q}(X^{[p,p+N]})\to
   H^{p+q}(X^{[p,p+r]})\bigr),\\
   B_r^{p,q}=\operatorname{im}\bigl(H^{p+q}(X^{[p-r+1,p+N]})\to
   H^{p+q}(X^{[p,p+r]})\bigr),
  \end{gathered}
  $$
  and with the identification $\mathcal H(E_r)\cong E_{r+1}$ natural;
- (b) the induced filtration
  $F^pH^n(K^\bullet):=\operatorname{im}\bigl(H^n(F^pK^\bullet)\to
  H^n(K^\bullet)\bigr)$ is finite and separated on each $H^n(K^\bullet)$, and
  there are natural isomorphisms
  $E_\infty^{p,q}\cong\operatorname{gr}^pH^{p+q}(K^\bullet)$ in the sense of
  [def-sp-convergence]: the spectral sequence converges to the cohomology of
  $K^\bullet$;
- (c) the construction is functorial in the pair
  $(K^\bullet,F^\bullet K^\bullet)$;
- (d) first-quadrant variant: if in addition $F^pK^\bullet=K^\bullet$ for
  $p\leq0$ and the graded pieces $\operatorname{gr}^pK^\bullet$ have
  cohomology concentrated in degrees $[p,p+1]$, then $E_r^{p,q}=0$ unless
  $p\geq0$ and $q\geq0$, and the entries stabilize for $r>\max(p,q)+1$.
