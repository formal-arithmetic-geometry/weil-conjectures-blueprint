+++
kind  = "proof"
of    = "sk-prop-hilbert90"
+++
Three steps, none of which is specific to curves.

*(i) $H^1$ classifies torsors.* For any abelian sheaf $G$ on
$X_{\Et}$ one has
$H^1(X_{\Et},G)=\mathrm{Ext}^1_{\mathrm{Ab}(X_{\Et})}(\Z_X,G)$,
because $\mathrm{Hom}(\Z_X,-)=\Gamma(X,-)$ (a map out of $\Z_X$ is
its value on $1$), so the two functors have the same derived
functors; and an extension
$0\to G\to E\xrightarrow{\pi}\Z_X\to0$ corresponds to the
$G$-torsor $\pi^{-1}(1)$, with inverse
$T\mapsto\coprod_{n\in\Z}T^{\otimes n}$ (contracted products).

*(ii) $\mathbb G_m$-torsors are invertible modules.* The
assignments $\mathcal L\mapsto\underline{\mathrm{Isom}} (\mathcal O_X,\mathcal L)$ and
$T\mapsto(T\times\mathcal O_X)/\mathbb G_m$ are mutually inverse: a
trivialisation $\mathcal L|_U\cong\mathcal O_U$ gives
$\underline{\mathrm{Isom}}(\mathcal O_X,\mathcal L)|_U\cong \mathbb G_m|_U$ via $\varphi\mapsto\varphi(1)$, so the first is a
torsor, and $(T\times\mathcal O_X)/\mathbb G_m$ is locally
$(\mathbb G_m\times\mathcal O_X)/\mathbb G_m\cong\mathcal O_X$,
hence invertible.

*(iii) Étale $=$ Zariski for $\mathbb G_m$.* A
$\mathbb G_m$-torsor trivial on an étale cover is already trivial
on a Zariski cover: the associated quasi-coherent module descends by
faithfully flat descent for quasi-coherent modules, and an invertible
module is Zariski-locally trivial by definition. Cohomologically
this is Hilbert 90: in the  Cech-to-derived-functor spectral
sequence $\check H^p(\mathcal U,\underline H^q(\mathbb G_m)) \Rightarrow H^{p+q}(X_{\Et},\mathbb G_m)$ the relevant
$\check H^1$ over an étale covering of a local ring vanishes,
which kills the difference between the two topologies in degree $1$.

The last assertion is the case $X=\Spec K$: a field has no
nontrivial invertible modules.
