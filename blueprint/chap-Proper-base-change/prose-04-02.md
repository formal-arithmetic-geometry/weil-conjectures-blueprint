+++
id = "prose-04-02"
kind = "hidden"
title = "Proper base change (2)"
order = 308
+++
For a proper map $f:X\to Y$ of locally compact Hausdorff spaces the answer
is yes. The sets $f^{-1}(V)$, for $V$ a neighbourhood of $y$, form a basis
of neighbourhoods of the compact fibre. The cohomology of a compact
subset is the colimit of the cohomology of its neighbourhoods.

In the étale topology, however, the stalk of $R^qf_*F$ at a geometric point
$\bar y$ is the cohomology of $X\times_YY_{(\bar y)}$, where
$Y_{(\bar y)}$ is the spectrum of the strict henselization of $Y$ at
$\bar y$. This scheme is much larger than the fibre $X_{\bar y}$. For
instance, if $f$ is the identity of a curve and $\bar y$ lies over a
closed point, then it is the spectrum of a strictly henselian local ring
of dimension one, not a point.

Properness cannot be dropped. Let $j:\mathbf G_m\hookrightarrow\mathbf A^1$
be the inclusion, $i:\{0\}\hookrightarrow\mathbf A^1$ the origin, and $A$
the constant sheaf on $\mathbf G_m$ with value a nonzero finite abelian
group. Then the sheaf $i^*j_*A$ is nonzero, while the base change of
$\mathbf G_m$ to the origin is empty.

For proper $f$ the answer is yes. More generally, pulling a proper
family back to a new base and taking its cohomology can be done in either
order. For a cartesian square with $f$ proper, $g:Y'\to Y$ arbitrary and
$X'=X\times_YY'$, the base change map

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism for every bounded below classical complex $K$ with
torsion cohomology sheaves (Theorem [theorem-proper-base-change-classical-pro]).
Taking for $g$ a geometric point gives the stalk formula
(Corollary [corollary-cohomology-geometric-fibres]). The theorem is due to
Artin [sga4, XII–XIII]. Unlike smooth base change
(Section [chap-Smooth-base-change]), it holds for torsion of every
order, including torsion divisible by the residue characteristics.

The content of the theorem is already visible in degree zero, where it is
a statement about connectedness. Sections of the constant sheaf $\{0,1\}$
are open and closed subsets. For a proper scheme over a henselian
local ring, the open and closed subsets correspond to those of the closed
fibre. When $X$ is finite over a henselian local ring $R$, this says
that idempotents of the finite $R$-algebra lift from its reduction
modulo the maximal ideal. This is one form of Hensel's lemma.
Theorem [theorem-comparison-over-henselian-pair-degree] extends the
statement to sections of every étale sheaf of sets. Higher degrees
reduce to degree zero and the projective line. From $\mathbf P^1$ the
general case follows by formal steps, through $(\mathbf P^1)^n$,
$\mathbf P^n$ and Chow's lemma
(Proposition [proposition-proper-base-change-etale-site]).

We make these calculations on the étale site, where the classical
tools are available, and transport them to
classical complexes on the pro-étale site by the comparison
theorems of Section [chap-The-pro-etale-site]. For $\mathcal O_E$ we pass
to the limit over the reductions modulo $\pi_E^n$
(Proposition [proposition-proper-base-change-complete-integral]). Pullback need not
preserve derived completeness, so at this stage the statement for
$\mathcal O_E$ involves the completed inverse image. Once we know that
$Rp_*$ preserves constructibility
(Proposition [proposition-proper-direct-image-constructible-complexes]), the completion is
unnecessary. We then obtain the ordinary base change isomorphism on
$D^b_{\mathrm{ctf}}$ for every admissible coefficient ring.

We use proper base change three times later. It computes the stalks of
$Rf_!$ in the trace formula
(Corollary [corollary-trace-functions-direct-image-compact]). It makes
$Rf_!=Rp_*j_!$ independent of the compactification
(Proposition [proposition-construction-independence-rf-shriek]). And
it bounds the Tor amplitude of $Rp_*$ with finite coefficients
(Proposition [proposition-proper-direct-image-finite-coefficients]).
