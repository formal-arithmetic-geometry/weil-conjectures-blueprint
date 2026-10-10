+++
kind  = "proof"
of    = "cor-fd-origin-stationary-phase"
+++
By hypothesis there is an isomorphism of Weil complexes
$\operatorname{FT}_\psi(j_{!*}\mathcal M[1])\cong j'_{!*}\mathcal M'[1]=j'_*\mathcal M'[1]$
([def-wf-middle-extension]); no other property of $\mathcal M$,
$\mathcal M'$ or $\psi$ is used. (Such a pair exists, with
$\mathcal M'$ irreducible, when $\psi$ is nontrivial and $\mathcal M$ is
irreducible and constituent-nonexceptional, by
[prop-a1-fourier-middle-extension]; for instance when $\mathcal M$ is
irreducible, unramified at infinity and not geometrically constant, by
[lem-a1-unramified-nonexceptional].)

The first identification is [lem-fd-stalk-at-origin]: the fiber of
the transform at the origin is $R\Gamma_c(\mathbf A^1,j_*\mathcal M[1])[1]$,
whose degree $-1$ part is $H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$,
while its degree $0$ part is
$H_c^2(\mathbf A^1_{k_0},j_*\mathcal M)$. This identification is
Frobenius-equivariant. Indeed, the Weil structure of
$\operatorname{FT}_\psi(K_0)$ is the one transported from those of
$K_0$ and of the kernel of [def-fd-transform] through $p_1^*$,
$\otimes$ and $p_{2,!}$, and the isomorphism of
[lem-fd-stalk-at-origin] at the rational point $0'$ is composed of
the base change isomorphism for $p_{2,!}$ along
$0'\hookrightarrow V^\vee$ and the trivialisation of the kernel on
the fibre $\mathbf A^1\times\{0'\}$ (the kernel of the zero function
$x\cdot0$ is the constant Weil sheaf). Both are natural isomorphisms
defined over $k_0$, so they commute with the Weil descent data, and the
stalk Frobenius $F_{0'}$ of the transform corresponds to the geometric
Frobenius on $R\Gamma_c(\mathbf A^1_{k_0},j_*\mathcal M)$.

For the second identification, the transformed object has the shape
$j'_*\mathcal M'[1]$ of [def-wf-middle-extension], a single
sheaf placed in degree $-1$; its fiber at the point $0'$ of the dual
line is therefore concentrated in degree $-1$, where it is the stalk
$(j'_*\mathcal M')_{0'}$, and the isomorphism of Weil complexes above
induces a Frobenius-equivariant isomorphism of the fibres at the
rational point $0'$. Comparing the two descriptions of the same fiber
gives $H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)\cong(j'_*\mathcal M')_{0'}$
equivariantly, and $H_c^2(\mathbf A^1_{k_0},j_*\mathcal M)=0$
because the degree $0$ part vanishes. If $0'\notin U'_0$, the
boundary-stalk description of
[lem-wf-boundary-stalk-invariants] gives
$(j'_*\mathcal M')_{0'}=\bigl(\mathcal M'_{\bar\eta}\bigr)^{I_{0'}}$,
Frobenius-equivariantly; if $0'\in U'_0$, the inertia $I_{0'}$ acts
trivially on the lisse sheaf $\mathcal M'$ and the stalk is
$\mathcal M'_{\bar\eta}=(\mathcal M'_{\bar\eta})^{I_{0'}}$. All
cohomology is in the compact-support convention of
[def-weil-ordinary-compact-cohomology].
