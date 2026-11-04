+++
kind = "proof"
of = "lemma-bounds-finite-reductions"
order = 229
uses = ["proposition-milnor-sequence", "theorem-comparison-constructible-sheaves", "corollary-finite-tor-amplitude-under-comparison"]
+++
Everything about $K_n$ is obtained from $K_1$ by induction on $n$, using
that $K_n$ is an extension of $K_{n-1}$ by $K_1$. The Tor bound needs an
extra argument with minimal resolutions, and the bound on $K$ itself then
follows from the Milnor sequence.

The filtration of $\mathcal O_E/\pi_E^n$ by the powers of $\pi_E$ has
graded pieces $\mathbf F_E$. Tensoring its short exact sequences with
$K$ over $\mathcal O_{E,X}$, we get triangles
$K_1\to K_{n}\to K_{n-1}$, up to the identification
$\pi_E^{n-1}\mathcal O_E/\pi_E^n\simeq\mathbf F_E$. Complexes with
constructible cohomology in $[a,b]$ are closed under extensions in
triangles. This follows from the long exact cohomology sequence and the fact
that constructible sheaves form a weak Serre subcategory. Induction on $n$ now shows
that $K_n$ is bounded in $[a,b]$ with constructible cohomology. Locally constant
finite sheaves of modules also form a weak Serre subcategory. Hence the same
induction works on a fixed stratum, and a single stratification works for
all $n$. By the comparison theorem for constructible sheaves
(Theorem [theorem-comparison-constructible-sheaves]), these finite sheaves and
complexes are classical, that is, pulled back from the étale site.

For the Tor bound we use
$K_n\otimes^{\mathbf L}_{\mathcal O_E/\pi_E^n}\mathbf F_E\simeq K_1$.
At an étale geometric point $\bar x$, take a bounded above resolution of the
stalk of $K_n$ by finite free modules over the Artinian local ring
$\mathcal O_E/\pi_E^n$. Cancelling a two-term identity summand whenever
a differential matrix has a unit entry, we obtain a minimal resolution.
Its differentials have entries in $(\pi_E)$, so they vanish after
tensoring with $\mathbf F_E$. Since stalks commute with derived tensor
products, the minimal resolution tensored with $\mathbf F_E$ computes the
stalk of $K_1$ at $\bar x$, with zero differential. Its rank
in degree $q$ is therefore $\dim_{\mathbf F_E}H^q(K_1)_{\bar x}$. This vanishes
outside $[a,b]$, and we conclude that the stalk has a bounded finite free
resolution in $[a,b]$. A bound on stalks gives the same Tor bound on the
étale site. Corollary [corollary-finite-tor-amplitude-under-comparison] carries
it to the pro-étale site, for Tor against arbitrary sheaves of modules there.

By completeness $K=R\varprojlim K_n$. The Milnor sequence
(2.2) gives the lower bound and the vanishing above
$b+1$. For $H^{b+1}(K)$ we use the top degree, where
$H^b(K_n)=H^b(K_{n+1})\otimes_{\mathcal O_E/\pi_E^{n+1}}\mathcal O_E/\pi_E^n$.
Thus the transition maps are epimorphisms. Their $R^1\varprojlim$ vanishes by the
last assertion of Proposition [proposition-milnor-sequence], and this means
that $H^{b+1}(K)=0$.
