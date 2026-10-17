+++
kind = "proof"
of = "det-tf-transverse-corner-vanishing"
uses = ["det-tf-transverse-corner-constant"]
+++
*Stalk formula.* The strict localization $S$ is the limit of the affine
étale neighbourhoods of $z$, and $S-Y_S$ is the limit of their open
subschemes $V-Y$. By the stalk formula for an open direct image
([Stacks, Tag 03Q7](https://stacks.math.columbia.edu/tag/03Q7)) and the
commutation of cohomology with this limit, $(Rj_*i_!E)_z$ is
$R\Gamma(S-Y_S,i_!E)$, where $i_!E$ also denotes the restriction to
$S-Y_S$.

*Forgetting $A$.* The forgetful functor from $A$-module sheaves to
abelian sheaves is exact and conservative, and cohomology of module
sheaves agrees with the cohomology of the underlying abelian sheaves
([Stacks, Tag 03FD](https://stacks.math.columbia.edu/tag/03FD)). So it
suffices to show that the underlying complex of abelian groups is zero.

*Dévissage.* Using the truncation triangles of the bounded complex $E$
and exactness of $i_!$, it suffices to treat a single cohomology sheaf
$H$, a finite locally constant sheaf of abelian $\ell$-groups on the
connected scheme $S-(X_S\cup Y_S)$ whose monodromy factors through a
finite $\ell$-group $G$. The subsheaves $\ell^aH$ are stable under $G$,
and their quotients are $\mathbf F_\ell[G]$-modules. The augmentation
ideal $I$ of $\mathbf F_\ell[G]$ is nilpotent, $G$ being an
$\ell$-group, so the subsheaves $I^bN$ of such a quotient $N$ give a
finite filtration whose graded pieces are $\mathbf F_\ell$-vector spaces
with trivial $G$-action, that is, finite sums of copies of the constant
sheaf $\mathbf F_\ell$. Since $i_!$ and $R\Gamma(S-Y_S,-)$ are exact
functors, the triangles of these filtrations reduce the assertion to
$E=\mathbf F_\ell$.

*Constant coefficients.* The complement of the open subscheme
$S-(X_S\cup Y_S)$ in $S-Y_S$ is the closed subscheme $X_S-z$. The
open–closed sequence
$0\to i_!\mathbf F_\ell\to\mathbf F_\ell\to\iota_*\mathbf F_\ell\to0$,
with $\iota:X_S-z\hookrightarrow S-Y_S$, identifies
$R\Gamma(S-Y_S,i_!\mathbf F_\ell)$ with the fibre (the cone shifted by
$-1$) of the restriction map
$R\Gamma(S-Y_S,\mathbf F_\ell)\to R\Gamma(X_S-z,\mathbf F_\ell)$. This
map is an isomorphism by [det-tf-transverse-corner-constant], so the
fibre is zero.
