+++
id = "lemma-weil-pbc-curve-constructible-primary-reduction"
kind = "lemma"
title = "Constructible and primary reduction on curves"
order = 1179
uses = ["lemma-weil-pbc-curve-filtered-cohomology", "lemma-weil-pbc-eight-curve-devissage", "lemma-weil-pbc-universal-homeomorphism-coverings", "lemma-weil-pbc-universal-homeomorphism-site-equivalence"]
+++
Let $X$ be a separated curve of finite type over an algebraically closed field
$k$ (so $\dim X\leq1$), and let $k'/k$ be an algebraically closed extension.
Suppose that for every prime $\ell$ and every constructible sheaf $G$ of
$\mathbf F_\ell$-modules on $X_{\mathrm{red}}$ the pullback maps

$$
 H^q(X_{\mathrm{red}},G)\longrightarrow
 H^q((X_{\mathrm{red}})_{k'},G_{k'})
$$

are isomorphisms for all $q$. Then for every torsion sheaf $F$ on $X_{\Et}$
the pullback maps $H^q(X,F)\to H^q(X_{k'},F_{k'})$ are isomorphisms for all
$q$. The same holds with the hypothesis only for primes
$\ell\neq\operatorname{char}k$ and the conclusion only for $F$ prime to
$\operatorname{char}k$.
