+++
kind  = "proof"
of    = "thm-sp-grothendieck"
+++
Choose an injective resolution $X\to I^\bullet$
([def-sp-injective-resolutions]) and put $K^\bullet=F(I^\bullet)$, a
complex in $\mathcal B$ concentrated in degrees $\geq0$ with
$\mathcal H^q(K^\bullet)=R^qF(X)$ ([def-sp-left-exact-additive]).

*The $E_2$-page.* Apply the truncation couple [def-sp-truncation-couple] to
$v=G$ and $K^\bullet$ (only the source $\mathcal B$ of $G$ needs injective
resolutions). By the shift and agreement parts (3) and (2) of
[lem-sp-kinjective-computes],

$$
 E_2^{p,q}=\mathcal H^{p+q}\bigl(RG(\mathcal H^q(K^\bullet)[-q])\bigr)
 \cong\mathcal H^p\bigl(RG(R^qF(X)[0])\bigr)\cong R^pG\bigl(R^qF(X)\bigr).
$$

These vanish unless $p\geq0$ and $q\geq0$, and $D^{p,q}=0$ for $q<0$, so
[thm-sp-half-plane-convergence] (with $a=0$) shows that the spectral
sequence of the couple is first-quadrant and converges
([def-sp-convergence]) to $A^n=D^{0,n}=\mathcal H^n(RG(\tau_{\leq n}
K^\bullet))$, with the image filtration
$F^pA^n=\operatorname{im}(D^{p,n-p}\to A^n)$ ([def-sp-image-filtration]).
Since $RG(\tau_{>n}K^\bullet)$ has no cohomology in degrees $\leq n$, the map
$A^n\to\mathcal H^n(RGK^\bullet)$ is an isomorphism.

*The abutment.* Each $K^s=F(I^s)$ is $G$-acyclic, by the hypothesis on $F$
([def-sp-composite-acyclicity]). In the spectral sequence of [thm-sp-if-e1]
for $v=G$ and $K^\bullet$, $E_1^{r,s}=R^rG(K^s)$ therefore vanishes for
$r\neq0$, so it is concentrated in a single row. The differentials $d_k$,
$k\geq2$, join different rows, so they vanish, $E_2=E_\infty$, and in each
total degree $n$ the abutment filtration has a single nonzero graded piece;
this is the edge collapse of [lem-sp-edge-collapse], with the two indices
exchanged, and the edge map is an isomorphism

$$
 \mathcal H^n(RGK^\bullet)\cong E_2^{0,n}=\mathcal H^n\bigl(G(K^\bullet)\bigr)
 =\mathcal H^n\bigl(GF(I^\bullet)\bigr)=R^n(G\circ F)(X),
$$

the last equality by [def-sp-left-exact-additive], $G\circ F$ being left
exact. Hence the spectral sequence converges to $R^{p+q}(G\circ F)(X)$.

*Edge maps.* In degree $n$ the entry $E_2^{n,0}=R^nG(F(X))$ receives no
differentials, so it surjects onto $E_\infty^{n,0}=F^nA^n\subseteq A^n$, and
$A^n\to A^n/F^1A^n=E_\infty^{0,n}$ lands in $E_2^{0,n}=G(R^nF(X))$, since no
differentials leave $(0,n)$; these are the edge maps
$R^nG(F(X))\to R^n(G\circ F)(X)\to G(R^nF(X))$.

*Functoriality.* A morphism $X\to X'$ extends to a morphism of injective
resolutions, unique up to homotopy, hence to a morphism $K^\bullet\to
K'^\bullet$; since $RG$ is functorial (part (1) of
[lem-sp-kinjective-computes]) and truncations are functorial, it induces a
morphism of truncation couples, hence of spectral sequences
([lem-sp-couple-morphism]), compatible with the abutment filtrations.

(*References: Weibel, An Introduction to Homological Algebra, Theorem 5.8.3;
Stacks Project, Lemma 13.22.1 (Tag
[015M](https://stacks.math.columbia.edu/tag/015M)) identifies the acyclicity
condition with the canonical map $R(G\circ F)\to RG\circ RF$ being an
isomorphism, and Lemma 13.22.2 (Tag
[015N](https://stacks.math.columbia.edu/tag/015N)) is the bounded, converging
spectral sequence with finite induced filtration. The relative Leray form
$E_2^{p,q}=R^pg_*(R^qf_*\mathcal F)\Rightarrow R^{p+q}(g\circ f)_*\mathcal
F$, functorial in $\mathcal F$ and available for bounded-below complexes, is
Lemma 20.13.8 (Tag [01F6](https://stacks.math.columbia.edu/tag/01F6)); the
topoi (site) form is Lemma 21.14.6, see the dictionary
[def-sp-etale-dictionary] for the specialization.*)
