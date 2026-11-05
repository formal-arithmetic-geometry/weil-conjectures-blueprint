+++
kind = "proof"
of = "lemma-proper-direct-image-unbounded-complexes"
order = 488
uses = ["lemma-uniform-bound-proper-direct-image--1", "lemma-uniform-bound-proper-direct-image--2", "proposition-ind-constructible-sheaves--5", "proposition-ind-constructible-sheaves--6", "proposition-ind-constructible-sheaves--7", "proposition-left-completeness", "proposition-milnor-sequence", "corollary-ambient-ind-derived--1"]
+++
For bounded below $K$ everything is read off from the hypercohomology
spectral sequence, which has only $2d+2$ nonzero columns. A general $K$, in turn, is the derived limit of its truncations $\tau_{\geq-n}K$, and the
column bound shows that in each fixed degree the tower of direct images
is eventually constant. The window (5.6) and the
preservation of direct sums follow from this.

*Bounded below $K$.* The hypercohomology spectral sequence

$$
E_2^{u,v}=R^up_*\mathcal H^v(K)\Longrightarrow\mathcal H^{u+v}(Rp_*K)
$$

converges. By Lemma [lemma-uniform-bound-proper-direct-image], its only nonzero
columns are $0\leq u\leq2d+1$, and their terms lie in
$\IndCons(Y,\Lambda)$. So each $\mathcal H^n(Rp_*K)$ has a finite
filtration whose graded pieces are subquotients of objects of
$\IndCons(Y,\Lambda)$. Since this category is closed under kernels,
cokernels and extensions by Proposition [proposition-ind-constructible-sheaves], we get
$\mathcal H^n(Rp_*K)\in\IndCons(Y,\Lambda)$. Both amplitude bounds
can be read off from the columns.

*Arbitrary $K$.* By Proposition [proposition-left-completeness], $K\simeq R\varprojlim_n
\tau_{\geq-n}K$. Since $Rp_*$ is a right adjoint, it preserves products and
hence derived inverse limits. Thus
$Rp_*K\simeq R\varprojlim_nRp_*\tau_{\geq-n}K$, and it suffices to see
that in each fixed degree the tower $Rp_*\tau_{\geq-n}K$ stabilizes. The fibre of
$\tau_{\geq-n-1}K\to\tau_{\geq-n}K$ is $\mathcal H^{-n-1}(K)[n+1]$, a
single ind-constructible sheaf in degree $-n-1$. By the bounded below
case its direct image has cohomology only in degrees
$[-n-1,-n-1+2d+1]=[-n-1,2d-n]$. In particular it has none
in degrees $q-1$, $q$, $q+1$ once $n>2d+1-q$. For fixed $q$, the long exact
sequences then show that the transition maps of the
towers $\mathcal H^q(Rp_*\tau_{\geq-n}K)$ and
$\mathcal H^{q-1}(Rp_*\tau_{\geq-n}K)$ are isomorphisms for $n$ large.
Since an eventually constant tower has vanishing $\varprojlim^1$, the
Milnor sequence of Proposition [proposition-milnor-sequence] gives

$$
\mathcal H^q(Rp_*K)\simeq
\mathcal H^q(Rp_*\tau_{\geq-n}K)\quad\text{for all sufficiently large }n.
$$

The bounded below case, applied to the right-hand side, shows that
$\mathcal H^q(Rp_*K)\in\IndCons(Y,\Lambda)$, with the bound $b+2d+1$ if $K\in
\Dic^{\leq b}(X,\Lambda)$. The lower bound needs no new argument, because
an object of $\Dic^{\geq a}$ is bounded below.

*The isomorphism (5.6).* It comes from the bounds,
applied to the truncation triangles

$$
\tau_{\leq q}K\to K\to\tau_{\geq q+1}K,
\qquad
\tau_{\leq q-2d-2}K\to\tau_{\leq q}K\to\tau_{\geq q-2d-1}\tau_{\leq q}K.
$$

The direct image of $\tau_{\geq q+1}K$ lives in degrees $\geq q+1$, and
that of $\tau_{\leq q-2d-2}K$ in degrees $\leq q-1$. The long exact
cohomology sequences of the two triangles therefore yield isomorphisms
$\mathcal H^q(Rp_*\tau_{\leq q}K)\simeq\mathcal H^q(Rp_*K)$ and
$\mathcal H^q(Rp_*\tau_{\leq q}K)\simeq
\mathcal H^q(Rp_*\tau_{\geq q-2d-1}\tau_{\leq q}K)$.

*Direct sums, assertion (3).* The window (5.6)
reduces us to families with cohomology in a common finite interval, and for such a family $(M_\alpha)$ we show by induction on the length of the interval
that the map
$\bigoplus_\alpha Rp_*M_\alpha\to Rp_*(\bigoplus_\alpha M_\alpha)$ is an
isomorphism. When the length is zero, each $M_\alpha$ is a shifted object of $\IndCons(X,\Lambda)$, and the claim is
the assertion about direct sums in Lemma [lemma-uniform-bound-proper-direct-image], in
each degree. Then, for the inductive step, we take the direct sum of the truncation
triangles that split off the top cohomology sheaf and apply the five lemma to the long exact cohomology sequences.

Now let $(K_\alpha)$ be arbitrary and fix $q$. Since direct sums of sheaves
are exact, cohomology and truncations commute with direct sums. The
objects $\tau_{\geq q-2d-1}\tau_{\leq q}K_\alpha$ have cohomology in the
common interval $[q-2d-1,q]$. Applying (5.6) to each
$K_\alpha$ and to $\bigoplus_\alpha K_\alpha$, and the first paragraph to
the truncated family, we see that
$\bigoplus_\alpha Rp_*K_\alpha\to Rp_*(\bigoplus_\alpha K_\alpha)$ is an
isomorphism on $\mathcal H^q$. Since $q$ is arbitrary, the map is an isomorphism.
