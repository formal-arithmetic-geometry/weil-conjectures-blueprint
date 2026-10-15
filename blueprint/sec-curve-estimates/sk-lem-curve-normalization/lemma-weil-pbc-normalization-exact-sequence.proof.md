+++
kind  = "proof"
of    = "lemma-weil-pbc-normalization-exact-sequence"
+++
Let $v:U^\nu\to U$. Define $\alpha$ as

$$
j_!\underline{\mathbf F_\ell}
\xrightarrow{j_!\eta}
j_!v_*\underline{\mathbf F_\ell}
\xrightarrow{\beta_{\nu,j}}
\nu_*j^\nu_!\underline{\mathbf F_\ell},
$$

where $\eta$ is the unit of $v^{-1}\dashv v_*$ and $\beta$ is the comparison
map already constructed. At $\bar x\in U$, its stalk is the diagonal

$$
\mathbf F_\ell\longrightarrow
\bigoplus_{\bar z\in\nu^{-1}(\bar x)}\mathbf F_\ell,\qquad
a\longmapsto(a)_{\bar z};
$$

outside $U$, both stalks are zero. Normalization is surjective, so the
diagonal is injective. Over the dense open where $\nu$ is an isomorphism it
is an isomorphism. Therefore the cokernel $Q$ is supported on the finite
nonnormal locus, with stalk the quotient of the displayed finite sum by its
diagonal. This proves exactness and constructibility.

After an algebraically closed extension, $X^\nu$ remains smooth and normal
and is the normalization of the reduced base-changed curve. The unit stalk
map remains the diagonal, while the base-change rectangle for $\beta$
identifies the two pulled-back comparison maps. Thus the short exact
sequence pulls back to the primed sequence. Naturality of the connecting
homomorphism follows by applying compatible injective resolutions. For an
open $W\subset X$, finite base change replaces $\nu$ by
$\nu^{-1}W\to W$ and gives the same stalk diagonals, proving compatibility
with open restriction.

Finally $H^q(X,Q)=0$ for $q>0$, and
$H^0(X,Q)$ is the finite direct sum of its stalks; both statements persist
after base change. Exact finite direct image and Leray identify
$H^q(X,\nu_*j^\nu_!\mathbf F_\ell)$ with
$H^q(X^\nu,j^\nu_!\mathbf F_\ell)$. Hence the displayed long exact
sequence transfers vanishing, finiteness, field-extension isomorphisms, and
open-restriction surjectivity from the normalized term to
$j_!\mathbf F_\ell$: in degrees at least two the maps are isomorphisms, and
in degrees zero and one the finite sequence

$$
0\to H^0(j_!\mathbf F_\ell)\to H^0(\nu_*j^\nu_!\mathbf F_\ell)
\to H^0(Q)\to H^1(j_!\mathbf F_\ell)\to
H^1(\nu_*j^\nu_!\mathbf F_\ell)\to0
$$

gives the comparison by a five-lemma diagram.

The normalization $\nu:X^\nu\to X$ is a finite morphism, hence has
exact direct image by [lemma-weil-pbc-finite-direct-image-exact], and $\nu$ is
an isomorphism over the normal locus, so that $X^\nu\to X$ is an
isomorphism over the open part of the extension by zero
[def-weil-pbc-extension-by-zero] outside the finite nonnormal locus. The map
$j_!\mathbf F_\ell\to\nu_*j^\nu_!\mathbf F_\ell$ is the diagonal finite-fibre
map: at a geometric point $\bar x\in U$ the target stalk is the product of
$\mathbf F_\ell$ over the finite geometric fibre of the normalization, computed
with the finite stalk formula, and the map is the adjoint of the unit; it is
injective with cokernel $Q$ supported on the finite nonnormal locus, and
exactness of the sequence follows from exactness of the two direct images and
the stalkwise computation. The cokernel $Q$ is constructible: it is
supported on the finite set of nonnormal points, i.e. it is the direct image
of a sheaf with finite stalks on this finite set of closed points. Naturality
of the sequence in the algebraically closed extension: the compatibilities of
[lemma-weil-pbc-finite-pushforward-extension-zero] (with the datum of
[def-weil-pbc-finite-open-comparison]) and of the finite direct
image under pullback along $X_{k'}\to X$ transport the construction, and the
constant-sheaf invariance supplied by
[thm-sc-main] makes the boundary maps and the
restrictions to opens compatible with *field extension*.
