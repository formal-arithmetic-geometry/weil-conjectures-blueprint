+++
kind = "proof"
of = "sk-prop-pe-unbounded-classical"
uses = ["det-pe-unbounded-classical-bounds", "det-pe-unbounded-classical-truncation", "det-pe-unbounded-classical-unit", "det-pe-unbounded-classical-direct-image"]
+++
We first record the cohomological bounds. Every affine $U_i$ étale over $X$ is
affine of finite type over $k$ with $\dim(U_i)\leq\dim(X)$, so Stacks Project,
Tag 0F0V gives $\operatorname{cd}_\ell(U_i)\leq\dim(X)+\operatorname{cd}_\ell(k)$
for $A$-module sheaves; this bound is independent of $i$. A bound of the same
kind holds for the fixed finite-type morphism $g$ and its étale base changes
(Stacks Project, Tag 0F10). For the schemes $X\times_YV_i$ used below, choose a
fixed finite affine open cover of $X$. Since $X$ and $Y$ are separated over $k$,
its intersections and their pullbacks to the affine $V_i$ are affine; each
pullback is étale over the corresponding intersection and has dimension at most
$\dim(X)$. The finite Čech complex of this cover therefore adds a bound
independent of $i$ to the affine bound. On a pro-étale affine limit the bound
for classical sheaves follows from cohomology comparison and continuity. All
these bounds hold for arbitrary $A$-module sheaves
([det-pe-unbounded-classical-bounds] records one uniform bound obtained this
way).

Next, the pro-étale truncation argument. Let $U$ be an affine object of
$X_{\Proet}$, and let $L$ be a pro-étale complex with classical cohomology and
$H^q(L)=0$ for $q>b$. Left completeness ([sk-prop-pe-left-complete]) gives

$$
L\simeq R\varprojlim_n\tau_{\geq-n}L.
$$

For each bounded-below term, derived sections over $U$ have cohomology only up to
degree $b+\dim(X)+\operatorname{cd}_\ell(k)$. Derived sections preserve the
displayed inverse limit, so by the Milnor sequence ([sk-prop-pe-milnor])
$R\Gamma(U,L)$ has no cohomology above
$b+\dim(X)+\operatorname{cd}_\ell(k)+1$. Apply this to $L=\tau_{<N}\nu_X^*K$: for
any prescribed degree $m$, choosing $N<m-\dim(X)-\operatorname{cd}_\ell(k)-2$
makes

$$
H^mR\Gamma(U,\nu_X^*K)\longrightarrow H^mR\Gamma(U,\tau_{\geq N}\nu_X^*K)
$$

an isomorphism. The choice of $N$ depends only on $m$ and the bound, so the
argument applies to every $K\in D(X_{\Et},A)$, bounded below or not
([det-pe-unbounded-classical-truncation]).

On the étale side, $\Gamma(U,-)$ on $A$-module sheaves has enough injective
acyclic objects and cohomological dimension at most
$\dim(X)+\operatorname{cd}_\ell(k)$, so the derived-functor lemma for bounded
cohomological dimension (Stacks Project, Tag 07K7) gives the same truncation for
arbitrary complexes directly. Thus in each degree the unit
$K\to R\nu_{X,*}\nu_X^*K$ in $D(X_{\Et},A)$ is computed on a bounded-below
truncation, where it is an isomorphism; hence the unbounded unit is an
isomorphism ([det-pe-unbounded-classical-unit]).

For direct images, evaluate on $V=\varprojlim_iV_i$ in the affine pro-étale basis
of $Y$. For a classical sheaf, cohomology on $X\times_YV$ is the filtered colimit
of cohomology on the $X\times_YV_i$, and the uniform bounds allow the same
fixed-degree truncation on both sides. Explicitly, use the triangle
$\tau_{<N}K\to K\to\tau_{\geq N}K$. The relative bound for $g$ places
$Rg_{\Et,*}\tau_{<N}K$ in degrees at most $N-1+\operatorname{cd}_\ell(g)$, and the
absolute bounds for the $V_i$ control its derived sections. On the pro-étale
side, the absolute bounds on $X\times_YV_i$ and continuity give the corresponding
bound on $X\times_YV$, up to the one extra Milnor degree found above. For $N$
sufficiently small both lower-tail contributions vanish in the prescribed
degree, and bounded-below direct-image comparison gives the comparison for
unbounded $K$ ([det-pe-unbounded-classical-direct-image]). Finally, $\nu_X^*$
preserves sums because it is an exact left adjoint.
