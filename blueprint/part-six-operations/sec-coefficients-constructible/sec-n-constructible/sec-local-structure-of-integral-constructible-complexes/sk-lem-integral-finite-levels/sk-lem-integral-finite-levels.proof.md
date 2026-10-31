+++
kind = "proof"
of = "sk-lem-integral-finite-levels"
uses = ["sk-thm-pe-constructible-comparison", "sk-cor-pe-finite-tor-comparison", "sk-prop-pe-milnor"]
+++
The filtration of $\mathcal O_E/\pi_E^n$ by the powers of $\pi_E$ has
graded pieces $\mathbf F_E$. Tensoring its short exact sequences with
$K$ over $\mathcal O_{E,X}$, we get triangles
$K_1\to K_{n}\to K_{n-1}$, up to the identification
$\pi_E^{n-1}\mathcal O_E/\pi_E^n\simeq\mathbf F_E$. Complexes with
constructible cohomology in $[a,b]$ are closed under extensions in
triangles, by the long exact cohomology sequence and because constructible
sheaves form a weak Serre subcategory, so induction on $n$ shows that
$K_n$ is bounded in $[a,b]$ with constructible cohomology. Locally constant
finite sheaves of modules also form a weak Serre subcategory, so the same
induction works on a fixed stratum, and a single stratification works for
all $n$. By the comparison theorem for constructible sheaves
(Theorem [sk-thm-pe-constructible-comparison]), these finite sheaves and
complexes are classical, that is, pulled back from the étale site.

For the Tor bound we use
$K_n\otimes^{\mathbf L}_{\mathcal O_E/\pi_E^n}\mathbf F_E\simeq K_1$.
At an étale geometric point $\bar x$, take a bounded above resolution of the
stalk of $K_n$ by finite free modules over the Artinian local ring
$\mathcal O_E/\pi_E^n$. Cancelling a two-term identity summand whenever
a differential matrix has a unit entry, we obtain a minimal resolution,
whose differentials have entries in $(\pi_E)$ and hence vanish after
tensoring with $\mathbf F_E$. Since stalks commute with derived tensor
products, the minimal resolution tensored with $\mathbf F_E$ computes the
stalk of $K_1$ at $\bar x$, and it has zero differential. Hence its rank
in degree $q$ is $\dim_{\mathbf F_E}H^q(K_1)_{\bar x}$. This vanishes outside $[a,b]$, and so the
stalk has a bounded finite free resolution in $[a,b]$. This bound on
stalks implies the same Tor bound on the étale site, and by
Corollary [sk-cor-pe-finite-tor-comparison] the bound holds on the
pro-étale site, for Tor against arbitrary sheaves of modules there.

Finally, $K=R\varprojlim K_n$ by completeness. The Milnor sequence
(2.2) implies the lower bound and the vanishing above
$b+1$. In the top degree we have
$H^b(K_n)=H^b(K_{n+1})\otimes_{\mathcal O_E/\pi_E^{n+1}}\mathcal O_E/\pi_E^n$,
and hence the transition maps are epimorphisms. By the last assertion of
Proposition [sk-prop-pe-milnor] their $R^1\varprojlim$ vanishes, so
$H^{b+1}(K)=0$.
