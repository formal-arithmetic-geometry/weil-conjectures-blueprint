+++
kind = "proof"
of = "sk-lem-proper-unbounded-window"
uses = ["sk-lem-proper-heart-bound", "sk-prop-ind-heart", "sk-prop-pe-left-complete", "sk-prop-pe-milnor"]
+++
*Bounded below $K$.* The hypercohomology spectral sequence

$$
E_2^{u,v}=R^up_*\mathcal H^v(K)\Longrightarrow\mathcal H^{u+v}(Rp_*K)
$$

converges. By [sk-lem-proper-heart-bound], its only nonzero columns are $0\leq u\leq2d+1$, and their terms
lie in $\IndCons(Y,\Lambda)$. Thus each $\mathcal H^n(Rp_*K)$ has a finite filtration whose graded pieces
are subquotients of objects of $\IndCons(Y,\Lambda)$. Since this category is closed under kernels,
cokernels and extensions ([sk-prop-ind-heart]), we conclude that $\mathcal H^n(Rp_*K)\in\IndCons(Y,\Lambda)$.
Both amplitude bounds can be read off from the columns ([det-proper-unbounded-window-bounded-below]).

*Arbitrary $K$.* By [sk-prop-pe-left-complete], $K\simeq R\varprojlim_n\tau_{\geq-n}K$. Since $Rp_*$ is a
right adjoint, it preserves products and hence derived inverse limits, so that
$Rp_*K\simeq R\varprojlim_nRp_*\tau_{\geq-n}K$. The fibre of $\tau_{\geq-n-1}K\to\tau_{\geq-n}K$ is
$\mathcal H^{-n-1}(K)[n+1]$. Its direct image has cohomology only in degrees $[-n-1,2d-n]$, and hence
none in degrees $q-1$, $q$, $q+1$ once $n>2d+1-q$. Fix $q$. The long exact sequences show that the
transition maps of the towers $\mathcal H^q(Rp_*\tau_{\geq-n}K)$ and $\mathcal H^{q-1}(Rp_*\tau_{\geq-n}K)$
are isomorphisms for $n$ large. An eventually constant tower has vanishing $\varprojlim^1$, and therefore
the Milnor sequence of [sk-prop-pe-milnor] shows that

$$
\mathcal H^q(Rp_*K)\simeq\mathcal H^q(Rp_*\tau_{\geq-n}K)\quad\text{for all sufficiently large }n.
$$

Applying the bounded below case to the right-hand side, we see that
$\mathcal H^q(Rp_*K)\in\IndCons(Y,\Lambda)$, and, if $K\in\Dic^{\leq b}(X,\Lambda)$, we also get the bound
$b+2d+1$. Since an object of $\Dic^{\geq a}$ is bounded below, the lower bound was proved in the first
step ([det-proper-unbounded-window-arbitrary]).

*The isomorphism (W).* We apply the bounds to the truncation triangles

$$
\tau_{\leq q}K\to K\to\tau_{\geq q+1}K,\qquad
\tau_{\leq q-2d-2}K\to\tau_{\leq q}K\to\tau_{\geq q-2d-1}\tau_{\leq q}K.
$$

The direct image of $\tau_{\geq q+1}K$ lives in degrees $\geq q+1$, and that of $\tau_{\leq q-2d-2}K$ in
degrees $\leq q-1$. Hence the long exact cohomology sequences of the two triangles yield isomorphisms
$\mathcal H^q(Rp_*\tau_{\leq q}K)\simeq\mathcal H^q(Rp_*K)$ and
$\mathcal H^q(Rp_*\tau_{\leq q}K)\simeq\mathcal H^q(Rp_*\tau_{\geq q-2d-1}\tau_{\leq q}K)$
([det-proper-unbounded-window-iso]).

*Direct sums, assertion (3).* First let $(M_\alpha)$ be a family with cohomology in a common finite
interval of degrees. We show by induction on the length of the interval that the map
$\bigoplus_\alpha Rp_*M_\alpha\to Rp_*(\bigoplus_\alpha M_\alpha)$ is an isomorphism. For length zero,
$M_\alpha$ is a shifted object of $\IndCons(X,\Lambda)$, and the claim is the assertion about direct sums
in [sk-lem-proper-heart-bound], in each degree. For the inductive step, we take the direct sum of the
truncation triangles that split off the top cohomology sheaf and apply the five lemma to the long exact
cohomology sequences ([det-proper-unbounded-window-ii-bounded]).

Now let $(K_\alpha)$ be arbitrary and fix $q$. Since direct sums of sheaves are exact, cohomology and
truncations commute with direct sums. The objects $\tau_{\geq q-2d-1}\tau_{\leq q}K_\alpha$ have cohomology
in the common interval $[q-2d-1,q]$. Applying (W) to each $K_\alpha$ and to $\bigoplus_\alpha K_\alpha$,
and the first paragraph to the truncated family, we see that
$\bigoplus_\alpha Rp_*K_\alpha\to Rp_*(\bigoplus_\alpha K_\alpha)$ is an isomorphism on $\mathcal H^q$.
Since $q$ is arbitrary, the map is an isomorphism ([det-lem-proper-unbounded-window-ii]).
