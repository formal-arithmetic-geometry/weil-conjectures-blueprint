+++
kind  = "proof"
of    = "lem-ag-homomorphism-image-closed"
+++
Put $S=f(G(L))$; since $f$ is a homomorphism, $S$ is a subgroup of
$K(L)$. Let $W\subseteq K$ be an affine open. Since $G$ is of finite
type, $f^{-1}(W)$ is covered by finitely many affine opens of finite type
over $L$, so Chevalley's theorem, part (1) of
[lem-wf-affine-constructible-open], shows that $f(G)\cap W$ is
constructible in $W$; thus $f(G)$ is locally constructible in $K$.
The closed points of $K$ are its $L$-points, and a closed point
$t\in f(G)$ has a nonempty fibre, which is a scheme of finite type over
$L$ and therefore has an $L$-point
([lem-wf-affine-nullstellensatz-vanishing]). Hence the $L$-points of
$f(G)$ are exactly $S$.

Let $J$ be the closure of $f(G)$ in $K$, with its reduced structure.
Closed points are dense in every locally constructible subset of a scheme
locally of finite type over $L$, so $J$ is the closure of $S$ and $J(L)$
is the closure of $S$ in $K(L)$. The closure of a
subgroup $H\subseteq K(L)$ is again a subgroup: for fixed $y\in H$ the
closed condition $xy\in\overline H$ holds on $H$, hence on $\overline H$;
then for fixed $x\in\overline H$ the closed condition $xy\in\overline H$
holds on $H$, hence on $\overline H$; inversion is the same argument.
Since $J\times_LJ$ is reduced and its closed points are the pairs of
$L$-points ([lem-wf-affine-product-reduced], applied to products of
affine opens of $J$), the vanishing principle of
[lem-wf-affine-nullstellensatz-vanishing] shows that multiplication and
inversion of $K$ restrict to $J$. Thus $J$ is a closed subgroup scheme
of $K$.

The locally constructible set $f(G)$ is dense in $J$, so by part (2) of
[lem-wf-affine-constructible-open], applied in an affine open of $J$
meeting $f(G)$, it contains a nonempty open $U\subseteq J$; then $U(L)\subseteq S$ and $U(L)\neq\varnothing$. Pick
$u\in U(L)$. Translations of $J$ by its $L$-points are automorphisms of
$J$ ([lem-sc-translation-automorphism]), so $u^{-1}U$ is an open
neighbourhood of $1$ in $J$ with $L$-points in $S$, and the translates
$s\,u^{-1}U$ with $s\in S$ show that $S$ is open in $J(L)$. The other
cosets of $S$ in $J(L)$ are open for the same reason, so $S$ is also
closed in $J(L)$. Since $S$ is dense in $J(L)$, we get $S=J(L)$.

Finally, $J\smallsetminus f(G)$ is locally constructible and contains no
closed point. A nonempty constructible subset of an affine scheme of
finite type over $L$ contains a nonempty locally closed subset, hence a
closed point; applying this in the affine opens of $J$ shows that
$J\smallsetminus f(G)$ is empty, so $f(G)=J$ is closed. In summary, the
closure $J$ of $f(G)$, with its reduced structure, is a closed subgroup
scheme of $K$ with $f(G)=J$ and $J(L)=f(G(L))$.

For the complement, a closed reduced matrix group is a group scheme of
finite type over $L$, and a regular homomorphism between reduced matrix
groups is a homomorphism of group schemes, because the identities
expressing it are identities of regular maps on reduced varieties that
hold on $L$-points ([lem-wf-affine-nullstellensatz-vanishing],
[lem-wf-affine-product-reduced]). Applying the argument above to
$f=\varphi$, the set $S=\varphi(G(L))$ is the set of $L$-points of the
closure $J$ of $\varphi(G)$, which with its reduced structure is a
closed subgroup of $K$. In particular $S$ is a closed subgroup of
$K(L)$.
