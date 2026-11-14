+++
kind = "proof"
of = "lemma-proper-direct-image-unbounded-complexes--1"
order = 487003
uses = ["definition-lisse-sheaves", "lemma-stability--3", "proposition-exact-products--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--3", "definition-constructible-sheaves--4", "lemma-constructible-sheaves--3", "lemma-constructible-sheaves--6", "proposition-ind-constructible-sheaves--2", "proposition-ind-constructible-sheaves--3", "proposition-ind-constructible-sheaves--7", "lemma-uniform-bound-proper-direct-image--1", "definition-relative-picard-functor--2"]
+++
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

*Source:* the proof of Lemma [lemma-proper-direct-image-unbounded-complexes].
