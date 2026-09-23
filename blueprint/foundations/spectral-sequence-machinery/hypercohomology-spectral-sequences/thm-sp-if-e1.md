+++
id = "thm-sp-if-e1"
kind = "theorem"
title = "Hypercohomology spectral sequence via a Cartan--Eilenberg resolution"
order = 1223
uses = ["def-sp-convergence", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "def-sp-truncation-couple", "lem-sp-kinjective-computes", "thm-sp-spectral-object-yields"]
+++
Let $v$ be as in [def-sp-truncation-couple] and let $A^{\bullet,\bullet}$ be
a Cartan--Eilenberg resolution of a bounded-below complex $K^\bullet$: the
row $A^{\bullet,s}$ is an injective resolution
[def-sp-injective-resolutions] of $K^s$, and the column cohomologies are the
$\mathcal H^s(K^\bullet)$. Then the filtration of the total complex by the
*second* degree gives the spectral sequence

$$
 E_1^{r,s}=R^rv(K^s)\Longrightarrow
 \mathcal H^{r+s}(RvK^\bullet),
$$

$d_1:E_1^{r,s}\to E_1^{r,s+1}$, induced by the differential of $K^\bullet$,
and the abutment is the cohomology of the derived functor of $K^\bullet$,
independent of the resolution.

**Status.** The proof formerly invoked Stacks Tags 0130/0131 for the whole
bicomplex spectral sequence without constructing it. It is now an application
of [thm-sp-spectral-object-yields] to the total complex of the double complex
with its second-degree filtration, together with the standard identification
of the row cohomology with the derived functors.

## Proof

Each row $A^{\bullet,s}$ is an injective resolution of $K^s$, so the entries
$R^rv(K^s)$ are the $r$-th cohomology of $v(A^{\bullet,s})$ by
[def-sp-injective-resolutions]. Apply [thm-sp-spectral-object-yields] to the
total complex
$K^\bullet:=\operatorname{Tot}\bigl(v(A^{\bullet,\bullet})\bigr)$ with its
decreasing filtration by the second degree,
$F^sK^\bullet:=\bigoplus_{s'\geq s}v(A^{\bullet,s'})$. This is a filtration
by subcomplexes: the total differential preserves the second degree in its
first summand and raises it in its second, so $\bigoplus_{s'\geq s}$ is
stable. It is bounded in each degree, because a total degree receives only
finitely many rows, the complex $K^\bullet$ being bounded below. The graded
pieces are $\operatorname{gr}^sK^\bullet=\operatorname{Tot}
\bigl(v(A^{\bullet,s})\bigr)$, so item (a) of that theorem gives

$$
 E_1^{r,s}=H^{r+s}\bigl(\operatorname{Tot}(v(A^{\bullet,s}))\bigr)
 =H^r\bigl(v(A^{\bullet,s})\bigr)=R^rv(K^s),
$$

the middle identification being the standard one for a complex concentrated
in a single degree of the second index, and the differential $d_1$ being the
boundary homomorphism of the filtration, which is induced by the differential
of $K^\bullet$ because the rows are resolutions of the $K^s$ and the maps
between them come from $K^\bullet$. Item (b) of the same theorem identifies
the abutment with the cohomology of the total complex, $\mathcal
H^{r+s}(\operatorname{Tot}(v(A^{\bullet,\bullet})))$, and this is $\mathcal
H^{r+s}(RvK^\bullet)$ because a Cartan--Eilenberg resolution computes the
derived functor of the complex, as recorded in
[def-sp-left-exact-additive]. Independence of the resolution follows by
comparing any two of them with a K-injective representative,
[lem-sp-kinjective-computes].
